"""Browser checks for uprt.html, the FFS 8 UPRT animation page (run through run_check.sh uprt).

Chromium and WebKit (the engine of Safari and Chrome on iPad) at iPad landscape sizes and phone.
For every animated row and part it seeks to each step through window.uprt, checks the PFD display
rules against the frame state, and screenshots the PFD at each step. Also checks overflow, 16px
HTML text, 44px targets, console errors, Mirror, Play and the no-JavaScript text.

Usage: check_uprt.py <out-dir> [--all-shots]
Prints a JSON report; exit code 1 if any check fails.
"""
import json
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(sys.argv[1])
ALL_SHOTS = '--all-shots' in sys.argv
OUT.mkdir(parents=True, exist_ok=True)
# Step times change between runs; stale shots would mix into a review. Only this check's own files go.
for old in [*OUT.glob('chromium-*.png'), *OUT.glob('webkit-*.png')]:
    old.unlink()
REPO = Path(__file__).resolve().parents[4]
URL = (REPO / 'uprt.html').as_uri()
CHROME = str(Path.home() / '.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell')
VIEWPORTS = {'ipad': {'width': 1194, 'height': 834}, 'ipad-chrome': {'width': 1194, 'height': 744},
             'phone': {'width': 390, 'height': 844}}

LAYOUT = """() => {
  const vis = e => e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden'
    && !e.closest('[hidden]');
  const own = e => Array.from(e.childNodes).some(n => n.nodeType === 3 && n.textContent.trim());
  const small = Array.from(document.querySelectorAll('p, li, td, th, dd, dt, span, button, q, a, output, select, cite, h1, h2, h3'))
    .filter(e => !e.closest('svg') && vis(e) && own(e) && parseFloat(getComputedStyle(e).fontSize) < 15.9)
    .map(e => e.className + ':' + e.textContent.trim().slice(0, 30));
  const targets = Array.from(document.querySelectorAll('button, select, a.control, input'))
    .filter(vis).filter(e => e.getBoundingClientRect().height < 43.5 || e.getBoundingClientRect().width < 43.5)
    .map(e => (e.id || e.className) + ':' + e.textContent.trim().slice(0, 20));
  return {overflow: document.documentElement.scrollWidth - innerWidth, small: small.slice(0, 8), targets: targets.slice(0, 8)};
}"""

RULES = """() => {
  const f = window.uprt.frame();
  const pfd = document.getElementById('pfd');
  const shown = sel => { const e = pfd.querySelector(sel); return !!e && e.getClientRects().length > 0 && getComputedStyle(e).display !== 'none'; };
  const text = sel => (pfd.querySelector(sel) || {}).textContent || '';
  const out = [];
  const manTrim = f.law === 'direct' || f.law === 'abnormal';
  if (manTrim && text('.f-trim') !== 'USE MAN PITCH TRIM') out.push('direct or abnormal attitude law without USE MAN PITCH TRIM');
  if (manTrim && !f.dc && !shown('.f-trim')) out.push('USE MAN PITCH TRIM hidden');
  if (f.law !== 'normal' && Math.abs(f.bank) > 45.5 && !shown('.m-bank')) out.push('BANK BANK missing');
  if (Math.abs(f.bank) < 44.5 && shown('.m-bank')) out.push('BANK BANK below 45°');
  if (f.stall !== shown('.m-stall')) out.push('STALL STALL message does not match the stall state');
  if (f.pitch > 30.5 && !shown('.arrows-up')) out.push('no red arrowheads beyond 30°');
  if (f.pitch < 29.5 && shown('.arrows-up')) out.push('red arrowheads below 30°');
  if ((Math.abs(f.bank) > 45.5 || f.pitch > 25.5 || f.pitch < -13.5) && !pfd.classList.contains('declutter')) out.push('not decluttered');
  if (f.dc && shown('.pfd-mark > div:last-child')) out.push('FPV shown while decluttered');
  if (f.law === 'normal' ? !shown('.prot-ok') : !shown('.prot-lost')) out.push('protection symbols do not match the law');
  // Abnormal attitude law: 40° up / 20° down with one valid ADC, else 50° / 30°; bank 125°.
  const [up, dn] = f.adc >= 2 ? [50, -30] : [40, -20];
  const beyond = f.pitch > up || f.pitch < dn || Math.abs(f.bank) > 125 || f.alpha > 40;
  if (beyond !== (f.law === 'abnormal')) out.push('abnormal attitude law does not match the attitude');
  // ECAM by priority: OVERSPEED above VMO + 4 kt / MMO + 0.006, VLE + 4 kt or VFE + 4 kt (FCOM PRO-ABN-OVERSPEED
  // P 1/2: VFE 230/215/200/185/177 kt for CONF 1/1+F/2/3/FULL); F/CTL DIRECT LAW while the abnormal attitude law is
  // on; F/CTL ALTN LAW after it (FCOM DSC-27-20-20 P 18/20); else an EWD memo (A.FLOOR).
  const ecam = document.querySelector('[data-read="ecam"]');
  const vfe = { '1': 230, '1+F': 215, '2': 200, '3': 185, full: 177 }[f.conf];
  const overWant = f.ias > 354 || f.mach > 0.826 || (f.gear === 'down' && f.ias > 284) || (vfe != null && f.ias > vfe + 4);
  if (overWant !== !!f.overspeed) out.push('OVERSPEED state does not match the speed');
  const ecamWant = f.overspeed ? 'ECAM: OVERSPEED' : f.law === 'abnormal' ? 'ECAM: F/CTL DIRECT LAW' : f.noprot ? 'ECAM: F/CTL ALTN LAW'
    : f.ecam && /memo$/.test(f.ecam.level) ? `EWD: ${f.ecam.text}` : '';
  // An amber EWD memo (A/THR OFF, FCOM DSC-22_30-50-40 P 2/4) uses the amber chip.
  if (f.ecam && f.ecam.level === 'amemo' && !ecam.classList.contains('ecam-amemo')) out.push('A/THR OFF memo chip is not amber');
  // Beta target (FCOM DSC-31-40 P 4/54): the sideslip index turns blue.
  const slipFill = (document.querySelector('.slip') || { getAttribute: () => '' }).getAttribute('fill');
  if (slipFill !== (f.btgt ? '#2fdcff' : '#ffe11a')) out.push(`sideslip index ${slipFill}, beta target ${!!f.btgt}`);
  if (f.btgt && !['1+F', '1', '2', '3'].includes(f.conf)) out.push('beta target outside CONF 1, 2 or 3');
  // Managed speed target magenta, selected cyan.
  if (f.spdTarget != null && shown('.s-target')) {
    const tf = document.querySelector('.s-target').getAttribute('fill');
    if (tf !== (f.spdManaged ? '#ff5cf0' : '#2fdcff')) out.push(`speed target ${tf}, managed ${!!f.spdManaged}`);
  }
  // ILS raw data with the LS pushbutton (FCOM DSC-31-40 P 40-41/54): one dot is 45 PFD units, centre (214, 243);
  // the glideslope index moves down when the aircraft is above it, the localizer index left when it is right of it.
  if (!f.dc && !!f.ils !== shown('.i-ils')) out.push('ILS scales do not match the LS state');
  if (f.ils) {
    const xy = sel => (((pfd.querySelector(sel) || { getAttribute: () => '' }).getAttribute('transform') || '').match(/-?[\d.]+/g) || []).map(Number);
    const cl = v => Math.max(-2, Math.min(2, v));
    const gy = xy('.i-gs')[1], lx = xy('.i-loc')[0];
    if (!(Math.abs(gy - (243 + cl(f.ils.gs) * 45)) < 0.6)) out.push(`glideslope index at y ${gy}, deviation ${f.ils.gs.toFixed(2)} dot`);
    if (!(Math.abs(lx - (214 - cl(f.ils.loc) * 45)) < 0.6)) out.push(`localizer index at x ${lx}, deviation ${f.ils.loc.toFixed(2)} dot`);
    // Beyond one dot for 2 s the glideslope scale would flash; the demonstrations stay inside it.
    if (Math.abs(f.ils.gs) >= 1) out.push(`glideslope deviation ${f.ils.gs.toFixed(2)} dot reaches one dot`);
  }
  // Radio height below 2 500 ft, the ground at sea level (FCOM DSC-31-40 P 32/54).
  if ((f.ra != null) !== (f.alt < 2500)) out.push('radio height state does not match the altitude');
  if (!f.dc && (f.ra != null) !== shown('.i-ra')) out.push('radio height display does not match the altitude');
  if (f.overspeed && !document.querySelector('[data-lamp="mw"]').classList.contains('lit')) out.push('MASTER WARN not lit in OVERSPEED');
  // Speed protection symbol (green =) in normal law only, at VMO + 6 kt / MMO + 0.01 (FCOM DSC-31-40 P 13/54).
  if (f.law !== 'normal' && shown('.s-hsp')) out.push('speed protection symbol outside normal law');
  if (f.law === 'normal' && Math.abs(f.vhsp - f.ias) < 35 && !shown('.s-hsp')) out.push('speed protection symbol missing near VMO');
  // A.FLOOR / TOGA LK box (FCOM DSC-22_30-80-20 P 4/36).
  const c1 = ((f.fma || {}).c1 || [])[0] || '';
  if (c1.endsWith('[]') !== shown('.f-box') && !f.dc) out.push('FMA box does not match column 1');
  if ((ecam.hidden ? '' : ecam.textContent) !== ecamWant) out.push(`ECAM chip "${ecam.hidden ? '' : ecam.textContent}", expected "${ecamWant}"`);
  const lawChip = document.querySelector('[data-read="law"]');
  if (f.noprot && f.law === 'altn' && lawChip.textContent !== 'Alternate law (no protection)') out.push('law chip does not show alternate law without reduced protection');
  if (!f.noprot && /no protection/.test(lawChip.textContent)) out.push('law chip shows no protection before any abnormal attitude law');
  const mcLit = document.querySelector('[data-lamp="mc"]').classList.contains('lit');
  const mwLit = document.querySelector('[data-lamp="mw"]').classList.contains('lit');
  if (f.law === 'abnormal' && !mcLit) out.push('MASTER CAUT not lit in the abnormal attitude law');
  // F/CTL ALTN LAW after the abnormal attitude law is a new amber caution (user decision).
  if (f.noprot && !mcLit) out.push('MASTER CAUT not lit with F/CTL ALTN LAW after the abnormal attitude law');
  // MASTER WARN flashes with the stall warning (PDP stall detection slide; user decision).
  if (f.stall && !mwLit) out.push('MASTER WARN not lit in the stall warning');
  if (!!f.mw !== mwLit) out.push('MASTER WARN lamp does not match the frame');
  for (const who of ['capt', 'fo']) {
    const fig = document.querySelector(`.ctl-stick[data-stick="${who}"]`);
    if (fig.classList.contains('pb-on') !== (f.pb === who)) out.push(`${who} takeover pushbutton light does not match the frame`);
  }
  // FD bars: FD on with HDG V/S (bird off); removed beyond 45° bank, 25° up or 13° down (FCOM DSC-22_30-20-40 P 1/2).
  if ((f.fd && !f.bird && !f.dc) !== shown('.fd')) out.push('FD bars do not match the FD, bird and declutter state');
  const g = document.querySelector('[data-read="gload"]');
  if (f.gload === g.hidden) out.push('G LOAD chip does not match');
  const stick = document.querySelector('.ctl-stick.active');
  if (f.active === 'capt' || f.active === 'fo') { if (!stick || stick.dataset.stick !== f.active) out.push('active sidestick not highlighted'); }
  return {t: f.t, pitch: +f.pitch.toFixed(1), bank: +f.bank.toFixed(1), ias: +f.ias.toFixed(1), n: +f.n.toFixed(2),
          alpha: +f.alpha.toFixed(1), alt: Math.round(f.alt), stall: f.stall, problems: out};
}"""

report, failures = {}, []


def fail(msg):
    failures.append(msg)


def run(browser, name, vp, touch):
    ctx = browser.new_context(viewport=vp, has_touch=touch, device_scale_factor=2 if name.endswith('ipad') else 1)
    page = ctx.new_page()
    errors = []
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(f'{URL}?row=13')
    page.wait_for_function('() => !!window.uprt')
    rep = report.setdefault(name, {})
    layout = page.evaluate(LAYOUT)
    rep['layout'] = layout
    if layout['overflow'] > 0:
        fail(f'{name}: horizontal overflow {layout["overflow"]}px')
    if layout['small']:
        fail(f'{name}: text below 16px {layout["small"]}')
    if layout['targets']:
        fail(f'{name}: targets below 44px {layout["targets"]}')
    page.screenshot(path=str(OUT / f'{name}-page.png'), full_page=False)
    rows = page.evaluate('() => window.uprt.rows()')
    rep['rows'] = [r['row'] for r in rows]
    # Every row (animated or not) fits the width: WebKit once let a long <select> option widen the page.
    for row in range(1, 22):
        page.evaluate(f"() => window.uprt.select({row}, '', 0)")
        over = page.evaluate('() => document.documentElement.scrollWidth - innerWidth')
        if over > 0:
            fail(f"{name}: row {row}: horizontal overflow {over}px")
    # The sticky toolbar would cover the top of element screenshots once the page scrolls.
    page.add_style_tag(content='.toolbar { position: static; }')
    shots = 0
    for r in rows:
        for part in r['parts']:
            page.evaluate(f"() => window.uprt.select({r['row']}, '{part['id']}', 0)")
            times = sorted(set(part['steps'] + [part['duration']]))
            for t in times:
                t = min(t + 0.05, part['duration'])
                page.evaluate(f'() => window.uprt.seek({t})')
                res = page.evaluate(RULES)
                for p in res['problems']:
                    fail(f"{name}: row {r['row']}{part['id']} t={t:.2f}: {p}")
                want = ALL_SHOTS or name.endswith('ipad') or (r['row'] == 13)
                if want:
                    path = OUT / f"{name}-row{r['row']}{part['id']}-{t:05.1f}.png"
                    # The flashing MASTER WARN is caught lit: infinite animations reset to their start.
                    page.locator('#stage').screenshot(path=str(path), animations='disabled')
                    shots += 1
            frames = page.evaluate('() => window.uprt.frames()')
            # Only parts that declare it may reach the abnormal attitude law (nose-low rows, user decision).
            abn = [f for f in frames if f['law'] == 'abnormal']
            if abn and not part['abnormal']:
                fail(f"{name}: row {r['row']}{part['id']}: abnormal attitude law at t={abn[0]['t']:.2f} in a part that does not declare it")
            if part['abnormal'] and not abn:
                fail(f"{name}: row {r['row']}{part['id']}: declares the abnormal attitude law but never reaches it")
    rep['shots'] = shots
    # Mirror flips the bank.
    page.evaluate("() => window.uprt.select(3, 'a', 5)")
    b0 = page.evaluate('() => window.uprt.frame().bank')
    page.click('#mirror')
    b1 = page.evaluate('() => window.uprt.frame().bank')
    if not (b0 < -10 and abs(b0 + b1) < 0.01):
        fail(f'{name}: Mirror did not flip the bank ({b0} -> {b1})')
    page.click('#mirror')
    # Play advances time.
    page.evaluate("() => window.uprt.select(13, 'a', 0)")
    page.click('#play')
    page.wait_for_timeout(700)
    page.click('#play')
    t = page.evaluate('() => window.uprt.state().t')
    if not t > 0.2:
        fail(f'{name}: Play did not advance ({t})')
    rep['played_to'] = round(t, 2)
    # A scrubber drag fires many input events; Safari throws past 100 history updates in 10 s.
    page.evaluate("""() => { window.uprt.select(17, 'a', 0); const s = document.getElementById('scrub');
      for (let i = 0; i < 150; i++) { s.value = String(i * 0.4); s.dispatchEvent(new Event('input', { bubbles: true })); } }""")
    t = page.evaluate('() => window.uprt.state().t')
    if abs(t - 59.6) > 0.05:
        fail(f'{name}: scrubber drag ended at t={t}, expected 59.6')
    if errors:
        fail(f'{name}: console errors {errors[:3]}')
    ctx.close()


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    ctx = browser.new_context(java_script_enabled=False, viewport=VIEWPORTS['ipad'])
    page = ctx.new_page()
    page.goto(URL)
    report['nojs_sheets'] = page.locator('.sheet').count()
    if report['nojs_sheets'] != 21 or not page.locator('#no-js-note').is_visible() or page.locator('#player').is_visible():
        fail('no-JS: expected 21 exercise sheets, the no-JS note and no player')
    ctx.close()
    for label, vp in VIEWPORTS.items():
        run(browser, f'chromium-{label}', vp, touch=False)
    browser.close()
    if os.environ.get('WEBKIT_RUN'):
        webkit = p.webkit.launch(executable_path=os.environ['WEBKIT_RUN'])
        for label, vp in VIEWPORTS.items():
            run(webkit, f'webkit-{label}', vp, touch=True)
        webkit.close()
        report['webkit'] = 'checked'
    else:
        fail('WebKit not available: iPad (Safari/Chrome) behaviour was not checked')

report['failures'] = failures
print(json.dumps(report, indent=1))
sys.exit(1 if failures else 0)
