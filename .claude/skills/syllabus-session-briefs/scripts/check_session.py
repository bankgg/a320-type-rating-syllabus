"""Browser checks for a session's procedure briefs (run through run_check.sh).

Chromium runs the full suite; WebKit (the engine of every iPad browser, Safari and Chrome alike)
runs the touch interaction suite when run_check.sh provides WEBKIT_RUN.

Usage: check_session.py <session-id> <out-dir>
Prints a JSON report and writes screenshots to <out-dir>. Exit code 1 if any check fails.
"""
import json
import os
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
  const card = d && d.querySelector('.dialog-card');
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
          dialogOpen: !!(d && d.open), dialogOverflow: d && d.open ? card.scrollWidth - card.clientWidth : 0,
          brief: brief ? brief.dataset.brief : null, small: small.slice(0, 8), targets: targets.slice(0, 8)};
}"""

report, failures = {}, []


def fail(msg):
    failures.append(msg)


def interactions(browser, name, vp, touch):
    """iPad/phone use: tap a row, interact inside the dialog, then tap outside or the close button.
    The dialog must close, drop ?brief=, and leave no focus ring behind."""
    page = browser.new_context(viewport=vp, has_touch=touch, is_mobile=touch).new_page()
    press = lambda loc: (loc.tap if touch else loc.click)()
    state = """() => { const a = document.activeElement;
        return {open: document.querySelector('dialog').open, url: location.search,
                ring: a && a !== document.body && a.matches(':focus-visible') ? a.className || a.tagName : null}; }"""

    def outside():
        (page.touchscreen.tap if touch else page.mouse.click)(3, vp['height'] // 2)
        page.wait_for_timeout(700)

    def expect_closed(case):
        r = page.evaluate(state)
        if r['open'] or 'brief=' in r['url'] or r['ring']:
            fail(f'{name} {case}: {r}')

    def open_row():
        page.goto(f'{URL}?session={SID}&view=exercises')
        page.wait_for_timeout(300)
        press(page.locator(f'#{SID} .brief-open').first)
        page.wait_for_timeout(600)
        if not page.evaluate(state)['open']:
            raise RuntimeError(f'row did not open the dialog: {page.evaluate(state)}')

    def in_card(selector):
        loc = page.locator(f'dialog .brief:not([hidden]) {selector}').first
        if loc.count():
            loc.scroll_into_view_if_needed()
            press(loc)
            page.wait_for_timeout(400)

    def scroll_card():
        page.evaluate("() => { const c = document.querySelector('.dialog-card'); c.scrollTop = c.scrollHeight; }")
        page.wait_for_timeout(300)

    def open_setup():
        page.goto(f'{URL}?session={SID}&view=exercises')
        page.wait_for_timeout(300)
        press(page.locator(f'#{SID} .open-setup'))
        page.wait_for_timeout(600)
        if not page.evaluate(state)['open']:
            raise RuntimeError('setup dialog did not open')

    scenarios = (
        ('outside tap, fresh', [open_row, outside]),
        ('outside tap after More detail', [open_row, lambda: in_card('details summary'), lambda: in_card('details summary'), outside]),
        ('outside tap after jump', [open_row, lambda: page.locator('dialog .jump:visible').count() and press(page.locator('dialog .jump:visible').last), lambda: page.wait_for_timeout(600), outside]),
        ('outside tap after scrolling', [open_row, scroll_card, outside]),
        ('close button', [open_row, lambda: press(page.locator('dialog .close-brief:visible').first), lambda: page.wait_for_timeout(700)]),
        ('setup, outside tap', [open_setup, outside]),
    )
    for case, steps in scenarios:
        try:
            for step in steps:
                step()
            expect_closed(case)
        except Exception as error:  # a stuck step is a failure, not a crash
            fail(f'{name} {case}: {str(error).splitlines()[0]}')
    page.context.close()


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
        # Procedure cue: in both tabs only rows that open a brief carry the dotted blue underline, and each tab's key says so
        for view, panel, text, name in (('exercises', 'exercises', '.exercise-title', 'exercises'), ('topics', 'topics', '.topic-text', 'schedule')):
            page.goto(f'{URL}?session={SID}&view={view}')
            page.wait_for_timeout(300)
            page.screenshot(path=str(OUT / f'{label}-{name}.png'), full_page=True)
            cue = page.evaluate(f"""() => {{
                const panel = document.getElementById('{SID}-panel-{panel}');
                const rows = Array.from(panel.querySelectorAll('{text}'));
                const style = e => getComputedStyle(e).textDecorationStyle + (getComputedStyle(e).textDecorationLine.includes('underline') ? '' : ':none');
                const key = panel.querySelector('.brief-key');
                return {{linked: rows.filter(e => e.closest('.brief-open')).map(e => [e.textContent.slice(0, 40), style(e)]),
                         plain: rows.filter(e => !e.closest('.brief-open')).map(e => [e.textContent.slice(0, 40), style(e)]),
                         key: !!(key && key.getClientRects().length)}};
            }}""")
            bad = [t for t, s in cue['linked'] if s != 'dotted'] + [t for t, s in cue['plain'] if s == 'dotted']
            if not cue['linked'] or bad or not cue['key']:
                fail(f"{label} {name} cue: linked={len(cue['linked'])} key={cue['key']} wrong={bad}")
            report[f'{label}-{name}'] = {'linked': [t for t, _ in cue['linked']]}
        page.goto(f'{URL}?session={SID}&view=exercises')
        page.wait_for_timeout(300)
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
                h = page.evaluate("() => document.querySelector('.dialog-card').scrollHeight + 40")
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
    for label, vp in VIEWPORTS.items():
        interactions(browser, f'chromium {label}', vp, touch=False)
    browser.close()
    if os.environ.get('WEBKIT_RUN'):
        webkit = p.webkit.launch(executable_path=os.environ['WEBKIT_RUN'])
        for label, vp in VIEWPORTS.items():
            interactions(webkit, f'webkit {label}', vp, touch=True)
        webkit.close()
        report['webkit'] = 'checked'
    else:
        fail('WebKit not available: iPad (Safari/Chrome) behaviour was not checked')

report['failures'] = failures
print(json.dumps(report, indent=1))
sys.exit(1 if failures else 0)
