"""Browser checks for a session's procedure briefs (run through run_check.sh).

Usage: check_session.py <session-id> <out-dir>
Prints a JSON report and writes screenshots to <out-dir>. Exit code 1 if any check fails.
"""
import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

SID, OUT = sys.argv[1], Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
REPO = Path(__file__).resolve().parents[4]
URL = (REPO / 'index.html').as_uri()
CHROME = str(Path.home() / '.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell')
VIEWPORTS = {'ipad': {'width': 1194, 'height': 834}, 'phone': {'width': 390, 'height': 844}}

CHECK = """() => {
  const d = document.querySelector('dialog');
  const scope = d && d.open ? d : document;
  const vis = e => e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden';
  const textNodes = e => Array.from(e.childNodes).some(n => n.nodeType === 3 && n.textContent.trim());
  const small = Array.from(scope.querySelectorAll('p, li, td, th, dd, dt, span, button, summary, h4, h5, h6, q'))
    .filter(e => vis(e) && textNodes(e) && parseFloat(getComputedStyle(e).fontSize) < 15.9)
    .map(e => e.className + ':' + e.textContent.trim().slice(0, 30));
  const targets = Array.from(scope.querySelectorAll('button, summary')).filter(vis)
    .filter(e => e.getBoundingClientRect().height < 43.5 && !e.classList.contains('summary-link'))
    .map(e => e.className + ':' + e.textContent.trim().slice(0, 30));
  const brief = d && d.open ? d.querySelector('.brief:not([hidden])') : null;
  return {docOverflow: document.documentElement.scrollWidth - innerWidth,
          dialogOpen: !!(d && d.open), dialogOverflow: d && d.open ? d.scrollWidth - d.clientWidth : 0,
          brief: brief ? brief.dataset.brief : null, small: small.slice(0, 8), targets: targets.slice(0, 8)};
}"""

report, failures = {}, []


def fail(msg):
    failures.append(msg)


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    for label, vp in VIEWPORTS.items():
        page = browser.new_page(viewport=vp)
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        page.goto(f'{URL}?session={SID}&view=exercises')
        page.wait_for_timeout(300)
        page.screenshot(path=str(OUT / f'{label}-exercises.png'))
        base = page.evaluate(CHECK)
        if base['docOverflow'] > 0 or base['small'] or base['targets']:
            fail(f'{label} session page: {base}')
        buttons = page.evaluate(f"""() => Array.from(document.querySelectorAll('#{SID} .brief-open, #{SID} .summary-link'))
            .map((b, i) => ({{i, brief: b.dataset.brief, kind: b.className}}))""")
        if not buttons:
            fail(f'{label}: no brief buttons in {SID}')
        seen = set()
        for b in buttons:
            # schedule-row buttons sit in the hidden tab panel; a JS click exercises them the same way
            page.evaluate(f"() => document.querySelectorAll('#{SID} .brief-open, #{SID} .summary-link')[{b['i']}].click()")
            page.wait_for_timeout(450)
            r = page.evaluate(CHECK)
            if not r['dialogOpen'] or r['brief'] != b['brief']:
                fail(f"{label}: button {b} opened {r['brief']}")
            if r['dialogOverflow'] > 0 or r['small'] or r['targets']:
                fail(f"{label} {b['brief']}: {r}")
            if b['brief'] not in seen:
                seen.add(b['brief'])
                page.screenshot(path=str(OUT / f"{label}-{b['brief']}.png"))
                h = page.evaluate("() => document.querySelector('dialog').scrollHeight")
                page.set_viewport_size({'width': vp['width'], 'height': min(h + 60, 12000)})
                page.wait_for_timeout(200)
                page.screenshot(path=str(OUT / f"{label}-{b['brief']}-full.png"))
                page.set_viewport_size(vp)
            page.keyboard.press('Escape')
            page.wait_for_timeout(450)
            after = page.evaluate("() => [document.querySelector('dialog').open, location.search]")
            if after[0] or 'brief=' in after[1]:
                fail(f"{label}: Escape did not close {b['brief']} ({after})")
        # deep links — every brief in the session, including companion tabs no row opens
        for slug in page.evaluate(f"() => Array.from(document.querySelectorAll('#{SID} .brief')).map(b => b.dataset.brief)"):
            seen.add(slug)
        for slug in sorted(seen):
            page.goto(f'{URL}?session={SID}&view=exercises&brief={slug}')
            page.wait_for_timeout(400)
            if page.evaluate(CHECK)['brief'] != slug:
                fail(f'{label}: deep link {slug} failed')
        report[label] = {'briefs': sorted(seen), 'buttons': len(buttons), 'errors': errors}
        if errors:
            fail(f'{label} console/page errors: {errors}')
        page.close()
    # setup dialog on another session still works; no-JS reading order
    page = browser.new_page(viewport=VIEWPORTS['ipad'])
    other = 'mftd-5' if SID != 'mftd-5' else 'mftd-6'
    page.goto(f'{URL}?session={other}&view=exercises')
    page.wait_for_timeout(300)
    page.click(f'#{other} .open-setup')
    page.wait_for_timeout(400)
    if not page.evaluate("() => document.querySelector('dialog').open"):
        fail('setup dialog did not open')
    page.close()
    ctx = browser.new_context(viewport=VIEWPORTS['ipad'], java_script_enabled=False)
    page = ctx.new_page()
    page.goto(URL)
    report['nojs_briefs'] = page.locator(f'#{SID} .procedure-briefs .brief').count()
    if report['nojs_briefs'] == 0:
        fail('no-JS: no briefs rendered')
    browser.close()

report['failures'] = failures
print(json.dumps(report, indent=1))
sys.exit(1 if failures else 0)
