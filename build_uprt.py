#!/usr/bin/env python3
"""Validate the FFS 8 UPRT storyboards and render uprt.html.

Source of truth: uprt_src/exercises.json (schema uprt-demo/1). The page shell is
uprt_src/template.html.j2; style.css and app.js are inlined as raw text so the
output is one self-contained file, like index.html.
"""

import json
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'uprt_src'
DATA = SRC / 'exercises.json'
SYLLABUS = ROOT / 'syllabus_sessions.json'
HTML_OUT = ROOT / 'uprt.html'
CACHE = ROOT / '.claude/skills/a320-ecam-abnormal/cache'

SCHEMA = 'uprt-demo/1'
ROWS = range(1, 22)
ANIMATED_ROWS = range(3, 22)
BOOKS = {'FCOM': 'fcom', 'FCTM': 'fctm', 'QRH': 'qrh', 'PDP': 'pdp'}
ACTORS = {'aircraft', 'instructor', 'trainee', 'ios'}
LAWS = {'normal', 'altn', 'direct'}
CONFS = {'clean', '1+F', '1', '2', '3', 'full'}
INIT_KEYS = {'alt', 'hdg', 'law', 'conf', 'gear', 'flaps', 'ap', 'fd', 'athr', 'bird',
             'spd_target', 'alt_target', 'hdg_target', 'baro', 'active', 'adc', 'ias', 'gamma', 'thr_max',
             'spd_managed', 'fd_spd', 'ils'}
# spd_managed: magenta (managed) speed target; fd_spd: SRS, the FD pitch bar flies this speed.
# thr_cmd: thrust lever position the engines follow whatever the levers (A.FLOOR / TOGA LK); ewd: an EWD memo;
# ewd_level: 'amemo' for an amber memo (A/THR OFF).
EVENT_KEYS = INIT_KEYS - {'ias', 'gamma', 'thr_max', 'ils'} | {'mw', 'mc', 'pb', 'fma', 'sound', 'thr_cmd', 'ewd', 'ewd_level'}
PART_KEYS = {'id', 'label', 'duration', 'illustrative', 'init', 'tracks', 'events', 'steps',
             'mode', 'abnormal_attitude'}
# Track ranges. Keyed attitudes stay just inside the abnormal attitude law thresholds
# with one ADR (user decision): below 40° up, above 20° down, below 125° bank. Physics
# parts (the nose-low upsets, user decision 2026-11-09) key load factor and bank only;
# their pitch follows from the flight path and may engage the abnormal attitude law.
TRACKS = {
    'pitch': (-19.99, 39.99), 'gamma': (-30, 30), 'bank': (-124.99, 124.99),
    'ias': (60, 400), 'n': (-1, 2.5), 'alpha': (-10, 25), 'beta': (-15, 15),
    'capt_x': (-1, 1), 'capt_y': (-1, 1), 'fo_x': (-1, 1), 'fo_y': (-1, 1),
    'rud': (-1, 1), 'tl1': (-1, 2), 'tl2': (-1, 2), 'n1_1': (15, 105), 'n1_2': (15, 105),
    'trim': (-4, 13.5), 'spdbrk': (0, 1), 'wind': (-60, 60),
}
PHYSICS_ONLY = {'wind'}
TOKENS = {'left', 'right', 'Left', 'Right', 'eng1', 'eng2'}


class Invalid(Exception):
    pass


def fail(where, msg):
    raise Invalid(f'{where}: {msg}')


def load_cache_meta():
    meta = {}
    for book, name in BOOKS.items():
        path = CACHE / f'{name}.json'
        if path.exists():
            meta[book] = json.loads(path.read_text(encoding='utf-8'))['meta']
    return meta


def check_sources(sources):
    cache = load_cache_meta()
    for sid, src in sources.items():
        if 'book' in src:
            book = src['book']
            if book not in BOOKS:
                fail(sid, f'unknown book {book}')
            if not isinstance(src.get('pdf'), int) or not src.get('code'):
                fail(sid, 'manual sources need code and pdf page')
            meta = cache.get(book)
            if meta:  # The cache is local only; skip when absent.
                m = meta[src['pdf'] - 1]
                if m.get('code') != src['code']:
                    fail(sid, f"PDF {src['pdf']} is {m.get('code')}, not {src['code']}")
                if src.get('page') and m.get('page') is not None and src['page'] != f"{m['page']}/{m['of']}":
                    fail(sid, f"PDF {src['pdf']} is P {m['page']}/{m['of']}, not {src['page']}")
        elif src.get('kind') not in ('photo', 'decision'):
            fail(sid, 'source must be a manual, photo or decision')
        if not src.get('label'):
            fail(sid, 'source needs a label')


def check_refs(where, refs, sources):
    if not refs:
        fail(where, 'missing refs')
    for ref in refs:
        if ref not in sources:
            fail(where, f'unknown source {ref}')


def check_text(where, text):
    if not isinstance(text, str) or not text.strip():
        fail(where, 'empty text')
    if 'HS-TO' in text:
        fail(where, 'HS-TO content is not allowed (HS-TX only)')
    for token in re.findall(r'\{(\w+)\}', text):
        if token not in TOKENS:
            fail(where, f'unknown mirror token {{{token}}}')


def check_track(where, name, keys, duration):
    if name not in TRACKS:
        fail(where, f'unknown track {name}')
    lo, hi = TRACKS[name]
    if len(keys) < 2:
        fail(where, f'{name} needs at least two keys')
    last = -1.0
    for t, v in keys:
        if not (0 <= t <= duration):
            fail(where, f'{name} key t={t} outside 0..{duration}')
        if t <= last:
            fail(where, f'{name} key times must increase (t={t})')
        if not (lo <= v <= hi):
            fail(where, f'{name}={v} at t={t} outside {lo}..{hi}')
        last = t


def check_part(where, part, guidance_ids, sources):
    duration = part.get('duration')
    if not isinstance(duration, (int, float)) or duration <= 0:
        fail(where, 'duration must be positive')
    if not part.get('label') or not part.get('illustrative'):
        fail(where, 'part needs a label and an illustrative note')
    extra = set(part) - PART_KEYS
    if extra:
        fail(where, f'unknown part keys {sorted(extra)}')
    mode = part.get('mode', 'keyed')
    if mode not in ('keyed', 'physics'):
        fail(where, f'unknown mode {mode}')
    init = part.get('init') or {}
    extra = set(init) - INIT_KEYS
    if extra:
        fail(where, f'unknown init keys {sorted(extra)}')
    for key in ('alt', 'hdg', 'law', 'conf', 'gear', 'active'):
        if key not in init:
            fail(where, f'init needs {key}')
    if init['law'] not in LAWS or init['conf'] not in CONFS:
        fail(where, 'bad law or conf')
    if init.get('adc', 3) not in (1, 3):
        fail(where, 'adc is the number of valid air data computers: 1 (ADR 1+2 OFF) or 3')
    if 'ils' in init:
        ils = init['ils']
        # ILS raw data with the LS pushbutton pressed: ident and frequency as the PFD shows them, course (°),
        # glideslope angle (°) and the start distance to the touchdown point (NM).
        if (not isinstance(ils, dict) or set(ils) != {'ident', 'freq', 'crs', 'gs', 'dme'}
                or not isinstance(ils['ident'], str) or not isinstance(ils['freq'], str)
                or not 0 <= ils['crs'] < 360 or not 2.0 <= ils['gs'] <= 4.0 or not 0 < ils['dme'] < 40):
            fail(where, 'ils needs ident, freq, crs (0-359), gs (2-4°) and dme (NM)')
        if mode != 'physics':
            fail(where, 'ils is for physics parts only')
    if part.get('abnormal_attitude') and mode != 'physics':
        fail(where, 'only physics parts may go past the abnormal attitude law thresholds')
    tracks = part.get('tracks') or {}
    for name, keys in tracks.items():
        check_track(where, name, keys, duration)
    if mode != 'physics':
        for name in PHYSICS_ONLY & set(tracks):
            fail(where, f'{name} is for physics parts only')
        if 'thr_max' in init:
            fail(where, 'thr_max is for physics parts only')
    if mode == 'physics':
        for name in ('pitch', 'gamma', 'ias', 'alpha'):
            if name in tracks:
                fail(where, f'physics parts do not key {name}: it follows from n, bank and thrust')
        if 'n' not in tracks or 'bank' not in tracks or 'ias' not in init:
            fail(where, 'physics parts need n and bank tracks and an initial ias')
        if tracks['n'][0][0] != 0 or tracks['n'][-1][0] != duration:
            fail(where, 'the n track must cover the whole part')
    else:
        if 'ias' in init or 'gamma' in init:
            fail(where, 'initial ias and gamma are for physics parts only')
        if 'bank' not in tracks or 'ias' not in tracks:
            fail(where, 'tracks need bank and ias')
        if 'pitch' not in tracks and 'gamma' not in tracks:
            fail(where, 'tracks need pitch or gamma')
    # The pitch-mode load factor comes from the pitch rate divided by cos(bank),
    # which is meaningless near 90° of bank: those keys need an n override.
    if 'pitch' in tracks and 'gamma' not in tracks:
        n_keys = tracks.get('n') or []
        lo = n_keys[0][0] if n_keys else None
        hi = n_keys[-1][0] if n_keys else None
        for t, v in tracks['bank']:
            if abs(v) > 65 and not (lo is not None and lo <= t <= hi):
                fail(where, f'bank {v}° at t={t} needs an n override')
    if 'gamma' in tracks and 'pitch' in tracks:
        fail(where, 'use either pitch or gamma, not both')
    for i, ev in enumerate(part.get('events') or []):
        if not (0 <= ev['t'] <= duration):
            fail(f'{where} event {i}', 'time outside the part')
        extra = set(ev.get('set', {})) - EVENT_KEYS
        if extra:
            fail(f'{where} event {i}', f'unknown keys {sorted(extra)}')
    last = -1.0
    for i, step in enumerate(part.get('steps') or []):
        sw = f'{where} step {i}'
        if not (0 <= step['t'] <= duration) or step['t'] < last:
            fail(sw, 'steps must be in time order inside the part')
        last = step['t']
        if step.get('actor') not in ACTORS:
            fail(sw, f"bad actor {step.get('actor')}")
        check_text(sw, step.get('text'))
        if step.get('g') and step['g'] not in guidance_ids:
            fail(sw, f"unknown guidance id {step['g']}")
        check_refs(sw, step.get('refs'), sources)
    if not part.get('steps') or part['steps'][0]['t'] != 0:
        fail(where, 'the first step must be at t=0')


def validate(data):
    if data.get('schema') != SCHEMA:
        fail('exercises.json', f'schema must be {SCHEMA}')
    sources = data['sources']
    check_sources(sources)
    for i, rule in enumerate(data['rules']):
        check_text(f'rule {rule.get("id", i)}', rule.get('text'))
        check_refs(f'rule {rule.get("id", i)}', rule.get('refs'), sources)
    for i, note in enumerate(data['page_notes']):
        check_text(f'page note {i}', note.get('text'))
        check_refs(f'page note {i}', note.get('refs'), sources)

    syllabus = json.loads(SYLLABUS.read_text(encoding='utf-8'))
    sessions = syllabus['sessions'] if isinstance(syllabus, dict) else syllabus
    session = next(s for s in sessions if s['id'] == data['session'])
    exercise_ids = {e['id'] for e in session['exercises']}

    rows = [ex['row'] for ex in data['exercises']]
    if rows != list(ROWS):
        fail('exercises', f'rows must be 1..21 in order, got {rows}')
    pending = []
    for ex in data['exercises']:
        where = f"row {ex['row']}"
        if ex['exercise_id'] is not None and ex['exercise_id'] not in exercise_ids:
            fail(where, f"unknown exercise id {ex['exercise_id']}")
        if ex['row'] > 1 and ex['exercise_id'] != f"ffs-8-e{ex['row'] - 1:02d}":
            fail(where, 'row N maps to ffs-8-e(N-1)')
        if ex['source'] not in sources:
            fail(where, f"unknown source {ex['source']}")
        check_text(where, ex['title'])
        check_text(f'{where} form', ex['form']['title'])
        ids = [g['id'] for g in ex['guidance']]
        if len(ids) != len(set(ids)):
            fail(where, 'guidance ids must be unique')
        for g in ex['guidance']:
            check_text(f"{where} {g['id']}", g['text'])
            if g.get('source') and g['source'] not in sources:
                fail(where, f"unknown source {g['source']}")
        for i, note in enumerate(ex['notes']):
            check_text(f'{where} note {i}', note['text'])
            check_refs(f'{where} note {i}', note.get('refs'), sources)
        part_ids = [p['id'] for p in ex['parts']]
        if len(part_ids) != len(set(part_ids)):
            fail(where, 'part ids must be unique')
        for part in ex['parts']:
            check_part(f"{where} part {part['id']}", part, set(ids), sources)
            # ADR 1+2 OFF leaves one valid ADC, which lowers the abnormal attitude thresholds
            # to 40° up / 20° down (FCOM DSC-27-20-20 P 18/20).
            if 'ADR 1+2 OFF' in (ex['setup'] or '') and part['init']['law'] != 'normal' and part['init'].get('adc') != 1:
                fail(f"{where} part {part['id']}", 'ADR 1+2 OFF: set init adc to 1')
        if ex['row'] in ANIMATED_ROWS and not ex['parts']:
            pending.append(ex['row'])
        if ex.get('listed_only') and ex['parts']:
            fail(where, 'listed-only rows have no animation')
    return pending


def payload_json(data):
    text = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    # Keep the JSON inert inside <script type="application/json">.
    return text.replace('</', '<\\/').replace('<!--', '<\\!--')


def view_model(data):
    sources = data['sources']
    used = set()
    for ex in data['exercises']:
        ex['animated'] = bool(ex['parts'])
        refs = [ex['source']] + [g['source'] for g in ex['guidance'] if g.get('source')]
        for note in ex['notes']:
            refs += note['refs']
        for part in ex['parts']:
            for step in part['steps']:
                refs += step['refs']
        ex['source_ids'] = list(dict.fromkeys(refs))
        used.update(ex['source_ids'])
        ex['group'] = 'Take-off (listed only)' if ex['row'] < 3 else (
            'Handling (rows 3–12)' if ex['row'] < 13 else 'Upset exercises (rows 13–21)')
    data['groups'] = []
    for ex in data['exercises']:
        if not data['groups'] or data['groups'][-1]['label'] != ex['group']:
            data['groups'].append({'label': ex['group'], 'members': []})
        data['groups'][-1]['members'].append(ex)
    for item in data['rules'] + data['page_notes']:
        used.update(item['refs'])
    order = list(sources)
    data['sources_used'] = [dict(sources[s], id=s) for s in order if s in used]
    return data


def source_label(src):
    """Short citation label; the JS refLabel() mirrors this."""
    if 'book' in src:
        page = f" P {src['page']}" if src.get('page') else ''
        return f"{src['book']} {src['code']}{page}, PDF {src['pdf']}"
    if src.get('kind') == 'decision':
        return 'Your decision'
    m = re.search(r'p\. (\d+) of', src['label'])
    if m:
        return f'Session guidance p. {m.group(1)} (photo)'
    return 'Topics form (photo)'


def build():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    pending = validate(data)
    payload = payload_json(data)
    model = view_model(json.loads(json.dumps(data)))
    env = Environment(loader=FileSystemLoader(SRC), autoescape=True)
    env.filters['source_label'] = source_label
    template = env.get_template('template.html.j2')
    html = template.render(
        data=model, payload=payload,
        css=(SRC / 'style.css').read_text(encoding='utf-8'),
        js=(SRC / 'app.js').read_text(encoding='utf-8'),
    )
    html = '\n'.join(line if line.strip() else '' for line in html.split('\n'))
    HTML_OUT.write_text(html, encoding='utf-8')
    animated = [ex['row'] for ex in data['exercises'] if ex['parts']]
    print(f'HTML: {HTML_OUT}')
    print(f'UPRT: {len(data["exercises"])} rows · animated rows {animated}'
          + (f' · not animated yet {pending}' if pending else ''))
    return HTML_OUT


def main():
    try:
        build()
    except Invalid as exc:
        sys.exit(f'uprt validation failed: {exc}')


if __name__ == '__main__':
    main()
