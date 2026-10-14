#!/usr/bin/env python3
"""Render the reviewed A320 session comparison as a static webpage."""

import argparse
import importlib.util
import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'syllabus_sessions.json'
HTML_OUT = ROOT / 'index.html'
BRIEFS_DIR = ROOT / 'abnormals'
BRIEF_SCHEMA = ROOT / '.claude/skills/a320-ecam-abnormal/scripts/render_md.py'

SETUP_FIELDS = [
    ('FROM / TO', 'From / to'), ('ALTN', 'Alternate'), ('FLT NBR', 'Flight number'),
    ('COST INDEX', 'Cost index'), ('CRZ FL', 'Planned cruise'), ('FLAPS', 'Flaps'),
    ('ZFW (t)', 'ZFW (t)'), ('ZFWCG (%MAC)', 'ZFWCG (%MAC)'),
    ('T/O FUEL (t)', 'Take-off fuel (t)'), ('TOW (t)', 'TOW (t)'),
    ('TRIP FUEL (t)', 'Trip fuel (t)'), ('T/O CG (%MAC)', 'Take-off CG (%MAC)'),
    ('ROUTE', 'Route'),
]
WEATHER_FIELDS = [
    ('airport', 'Airport'), ('runway', 'Runway'), ('wind', 'Wind'),
    ('visibility', 'Visibility'), ('ceiling', 'Ceiling'),
    ('temperature_c', 'Temp °C'), ('qnh', 'QNH'),
    ('runway_condition', 'RWY cond.'), ('anti_ice', 'Anti-ice'),
]
CATEGORIES = [
    'Takeoff & departure', 'Approaches & go-arounds', 'Landing',
    'Failures & systems', 'Flight handling',
]

# Presentation-only review of failure scenarios and their explicit recovery.
# Category names also include ordinary demonstrations; they are not a reliable
# failure flag. Keep this mapping separate from the reviewed training facts.
FAILURE_NUMBERS = {
    'mftd-3': (1, 2, 3, 13),
    'mftd-4': (4, 5, 6, 7, 8, 9, 18),
    'mftd-5': (1, 6, 8, 9, 10, 13, 14, 15, 16, 17),
    'mftd-6': (2, 3, 4, 7, 8, 9, 10),
    'mftd-7': (2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13),
    'mftd-8': (1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19),
    'mftd-9': (1, 5, 6, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19),
    'ffs-3': (1,),
    'ffs-4': (3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19),
    'ffs-5': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 19),
    'ffs-6': (3, 4, 6, 8, 9, 11, 13, 15, 16, 17, 18, 19),
    'ffs-7': (2, 5, 6, 7, 9, 10, 12, 13, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26),
    'ffs-9': (3, 4, 5, 6, 7, 12, 13, 14, 15),
    'ffs-10': (1, 4, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19),
}
FAILURE_IDS = {
    f'{sid}-e{number:02d}'
    for sid, numbers in FAILURE_NUMBERS.items() for number in numbers
} | {'ffs-7-apu-fire'}

# Short, combined A/B descriptions of the actual failure/emergency subjects.
# Recovery manoeuvres stay in the exercise list rather than repeating the same
# failure in the description. These labels preserve the reviewed terminology.
FAILURE_SUMMARIES = {
    'mftd-2': (),
    'mftd-3': ('APU inoperative (MEL)', 'Loss of braking (conditional)'),
    'mftd-4': ('Fuel pump low pressure', 'Engine failure', 'IDG oil low pressure/overheat', 'Cabin pressure system fault'),
    'mftd-5': ('Hot start', 'Slats fault/locked', 'Cargo smoke', 'Emergency evacuation', 'Engine failure', 'Hydraulic reservoir low level', 'Loss of braking'),
    'mftd-6': ('Unreliable speed', 'Cabin pressure failure', 'ADR faults', 'Fuel leak', 'Start valve fault', 'Air conditioning smoke'),
    'mftd-7': ('Engine failure', 'Engine fire', 'APU fire', 'Emergency evacuation'),
    'mftd-8': ('Engine failure', 'ANTI ICE STBY PITOT / STAT / AOA', 'Engine fire', 'Emergency evacuation', 'FMGC faults', 'SDAC/FWC faults', 'Unreliable speed', 'Emergency electrical configuration'),
    'mftd-9': ('Hot start', 'Engine fire', 'Emergency evacuation', 'Cabin pressure failure', 'Gear not downlocked', 'Engine failure with damage'),
    'ffs-1': (),
    'ffs-2': (),
    'ffs-3': ('ANTI ICE L(R) WINDOW',),
    'ffs-4': ('IR faults', 'Alternate/direct law', 'Mechanical backup', 'Cabin pressure failure', 'Radio altimeter faults', 'Cargo smoke', 'ADR faults', 'Emergency evacuation'),
    'ffs-5': ('Engine failure', 'Dual-engine failure', 'RNP degradation', 'Emergency electrical configuration', 'Unreliable speed'),
    'ffs-6': ('RNP degradation', 'Probe anti-ice', 'Hydraulic system low pressure', 'Flaps/slats faults', 'Stabilizer jam', 'Engine fire', 'Emergency evacuation'),
    'ffs-7': ('Crew incapacitation', 'FCU fault', 'Engine severe damage/separation', 'Fuel imbalance', 'RNP degradation', 'APU shutdown/fire', 'Loss of braking', 'Fuel leak', 'APU generator fault', 'Cabin smoke', 'Emergency evacuation', 'Engine failure'),
    'ffs-8': (),
    'ffs-9': ('IDG overheat', 'Navigation/FMGS failure', 'Engine failure', 'Fuel imbalance', 'Hydraulic reservoir low level', 'ADR faults', 'Duct leak / pack overheat', 'Cargo smoke'),
    'ffs-10': ('Engine start fault', 'Decompression', 'Hydraulic system failure', 'Flaps fault', 'Engine failure', 'Engine fire', 'Emergency evacuation'),
}


# Source-traced abnormal-procedure briefs (abnormals/<slug>.json, produced by the
# a320-ecam-abnormal skill). Each group label is one of the session's
# FAILURE_SUMMARIES subjects; its briefs open in one dialog with a switcher.
PROCEDURE_GROUPS = {
    'mftd-8': [
        ('Engine failure', (('eng-1-2-fail', 'Engine failure', 'Trainee A: after V2 on takeoff. Trainee B: at go-around.'),
                            ('eng-relight-in-flight', 'Relight in flight'))),
        ('ANTI ICE STBY PITOT / STAT / AOA', (('anti-ice-stby-pitot-stat-aoa', 'Standby probe heat'),)),
        ('Engine fire', (('eng-1-2-fire-on-ground', 'On ground · RTO', 'Engine fire below V1, not extinguishable — leads to the evacuation.'),
                         ('eng-1-2-fire-in-flight', 'In flight', 'Fire extinguished after the second agent.'))),
        ('Emergency evacuation', (('emer-evac', 'Emergency evacuation'),)),
        ('FMGC faults', (('fmgc-failure', 'FMGC faults', 'Demo FMGC 1 and FMGC 2 failure, then FMGC 1+2 fault reset with the QRH System Reset table.'),)),
        ('SDAC/FWC faults', (('fws-sdac-1-2-fault', 'SDAC 1 + 2', 'Demonstration with reset.'), ('fws-fwc-1-2-fault', 'FWC 1 + 2', 'Demonstration with reset.'))),
        ('Unreliable speed', (('unreliable-speed-indication', 'Unreliable speed', 'Compare the QRH Unreliable Speed tables with the QRH Severe Turbulence table.'),)),
        ('Emergency electrical configuration', (('elec-emer-config', 'ELEC EMER CONFIG', 'Demonstration.'),)),
    ],
    'mftd-9': [
        ('Hot start', (('eng-1-2-start-fault', 'START FAULT · hot start', 'Followed by a manual engine start.'),)),
        ('Engine fire', (('eng-1-2-fire-in-flight', 'In flight', 'Fire in cruise (FL 290): after the fire drill, drift down using the standard strategy (see Drift down).'),
                         ('eng-failure-cruise-strategy', 'Drift down'),
                         ('overweight-landing', 'Overweight landing', 'Overweight landing with LOC/DME vectors after the engine fire.'),
                         ('eng-1-2-fire-on-ground', 'On ground · RTO', 'Engine fire below V1, not extinguishable — leads to the evacuation.'))),
        ('Emergency evacuation', (('emer-evac', 'Emergency evacuation'),)),
        ('Cabin pressure failure', (('cab-pr-excess-cab-alt', 'Excess cab alt · emer descent', 'Emergency descent with no structural damage.'),)),
        ('Gear not downlocked', (('l-g-gear-not-downlocked', 'GEAR NOT DOWNLOCKED', 'The approach is discontinued; the gear malfunction is removed after the go-around.'),)),
        ('Engine failure with damage', (('eng-1-2-fail', 'ENG FAIL · damage', 'Engine failure with damage, after the discontinued approach.'),)),
    ],
    'ffs-3': [
        ('ANTI ICE L(R) WINDOW', (('anti-ice-l-r-window', 'ANTI ICE L(R) WINDOW', 'At preflight on EXT PWR; probe/window heat ON for cold weather.'),)),
    ],
    'ffs-4': [
        ('IR faults', (('nav-ir-1-2-3-fault', 'Single IR', 'IR 1(2)(3) FAULT on the PM side, no ECAM.'),
                       ('nav-ir-1-2-1-3-2-3-fault', 'Dual IR', 'IR 1+2 (1+3) (2+3) FAULT, no ECAM.'))),
        ('Alternate/direct law', (('f-ctl-altn-law', 'ALTN LAW', 'ALTN LAW and DIR LAW handling, then tuck under and Mach buffet in Normal and Alternate law.'),
                                  ('f-ctl-direct-law', 'DIRECT LAW', 'Later, the crosswind landing is flown in DIR LAW.'))),
        ('Mechanical backup', (('mechanical-backup', 'Mechanical backup', 'Demonstration.'),)),
        ('Cabin pressure failure', (('cab-pr-excess-cab-alt', 'Excess cab alt · emer descent', 'Trainee A: structural damage suspected. Trainee B: no structural damage suspected.'),)),
        ('Radio altimeter faults', (('nav-ra-1-and-2-fault', 'RA 1+2 FAULT', 'Followed by the ILS approach with AP using LOC/FPA.'),)),
        ('Cargo smoke', (('smoke-aft-cargo-smoke', 'AFT CARGO SMOKE', 'Listed in the syllabus as AFT/BULK CRG SMOKE.'),
                         ('removal-of-smoke-fumes', 'Removal of smoke/fumes'))),
        ('ADR faults', (('nav-adr-1-2-3-fault', 'Single ADR'),
                        ('nav-adr-1-2-1-3-2-3-fault', 'Dual ADR'))),
        ('Emergency evacuation', (('emer-evac', 'Emergency evacuation', 'Due to the cargo fire.'),)),
    ],
}
# Exercise rows that open a brief. Recovery manoeuvres (OEI approach,
# go-around, autoland) are failure-related but have no ECAM/QRH brief.
EXERCISE_BRIEFS = {
    'mftd-8-e01': 'eng-1-2-fail', 'mftd-8-e18': 'eng-1-2-fail',
    'mftd-8-e02': 'eng-relight-in-flight', 'mftd-8-e03': 'anti-ice-stby-pitot-stat-aoa',
    'mftd-8-e08': 'eng-1-2-fire-on-ground', 'mftd-8-e19': 'eng-1-2-fire-in-flight',
    'mftd-8-e09': 'emer-evac', 'mftd-8-e12': 'fmgc-failure', 'mftd-8-e13': 'fmgc-failure',
    'mftd-8-e14': 'fws-sdac-1-2-fault', 'mftd-8-e15': 'fws-fwc-1-2-fault',
    'mftd-8-e16': 'unreliable-speed-indication', 'mftd-8-e17': 'elec-emer-config',
    'mftd-9-e01': 'eng-1-2-start-fault', 'mftd-9-e05': 'eng-1-2-fire-in-flight',
    'mftd-9-e06': 'overweight-landing', 'mftd-9-e11': 'eng-1-2-fire-on-ground',
    'mftd-9-e12': 'emer-evac', 'mftd-9-e14': 'cab-pr-excess-cab-alt',
    'mftd-9-e16': 'l-g-gear-not-downlocked', 'mftd-9-e18': 'eng-1-2-fail',
    'ffs-3-e01': 'anti-ice-l-r-window',
    'ffs-4-e03': 'nav-ir-1-2-3-fault', 'ffs-4-e04': 'nav-ir-1-2-1-3-2-3-fault',
    'ffs-4-e05': 'f-ctl-altn-law', 'ffs-4-e06': 'mechanical-backup',
    'ffs-4-e08': 'cab-pr-excess-cab-alt', 'ffs-4-e19': 'cab-pr-excess-cab-alt',
    'ffs-4-e09': 'nav-ra-1-and-2-fault', 'ffs-4-e13': 'smoke-aft-cargo-smoke',
    'ffs-4-e14': 'removal-of-smoke-fumes', 'ffs-4-e16': 'emer-evac',
    'ffs-4-e17': 'nav-adr-1-2-3-fault', 'ffs-4-e18': 'nav-adr-1-2-1-3-2-3-fault',
}
ALERT_LABELS = {'warning': 'Red warning', 'caution': 'Amber caution', 'qrh': 'QRH procedure',
                'memory': 'Memory items', 'technique': 'Technique'}
SESSION_NAME = re.compile(r'\b(MFTD|FFS|FBS)\b')


def members(groups):
    """Group members are (slug, tab label) or (slug, tab label, session note)."""
    for _, entries in groups:
        for entry in entries:
            yield entry[0], entry[1], entry[2] if len(entry) > 2 else ''


def session_mentions(node, path=''):
    """Briefs are shared between sessions, so their text must not name one."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield from session_mentions(value, f'{path}.{key}')
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from session_mentions(value, f'{path}[{i}]')
    elif isinstance(node, str) and SESSION_NAME.search(node):
        yield path


def load_briefs():
    """Load every mapped brief, validated by the skill's own schema check."""
    spec = importlib.util.spec_from_file_location('render_md', BRIEF_SCHEMA)
    schema = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schema)
    briefs = {}
    for groups in PROCEDURE_GROUPS.values():
        for slug, _, _ in members(groups):
            path = BRIEFS_DIR / f'{slug}.json'
            assert path.exists(), f'missing brief {path}'
            brief = json.loads(path.read_text(encoding='utf-8'))
            schema.validate(brief)
            assert brief['slug'] == slug, path
            named = list(session_mentions(brief))
            assert not named, (f'{slug} names a session at {named}: keep briefs session-neutral and put '
                               'session context in the PROCEDURE_GROUPS note')
            briefs[slug] = brief
    return briefs


def ref_label(ref):
    if ref['book'] == 'QRH':
        return f"QRH {ref['page']} · PDF {ref['pdf']}"
    if ref['book'] == 'PDP':
        return f"PDP {ref['code']} · PDF {ref['pdf']}"
    return f"{ref['book']} {ref['code']} {ref['page']} · PDF {ref['pdf']}"


def collect_refs(node, out):
    if isinstance(node, dict):
        for ref in node.get('refs', []):
            label = ref_label(ref)
            if label not in out:
                out.append(label)
        for key, value in node.items():
            if key != 'refs':
                collect_refs(value, out)
    elif isinstance(node, list):
        for value in node:
            collect_refs(value, out)
    return out


def shown(value, *, unspecified=False):
    if value in ('', '–', '—', None):
        return 'Unspecified' if unspecified else '—'
    return str(value)


def validate(data):
    sessions = data['sessions']
    assert FAILURE_IDS <= {e['id'] for s in sessions for e in s['exercises']}
    assert len(sessions) == 18
    assert set(FAILURE_SUMMARIES) == {s['id'] for s in sessions}
    assert [s['id'] for s in sessions] == (
        [f'mftd-{n}' for n in range(2, 10)] + [f'ffs-{n}' for n in range(1, 11)]
    )
    assert sum(len(s['topics']['A']) for s in sessions) == 361
    assert sum(len(s['topics']['B']) for s in sessions) == 355
    for session in sessions:
        ids = {item['id'] for item in session['exercises']}
        assert len(ids) == len(session['exercises']), session['id']
        for side in ('A', 'B'):
            rows = session['topics'][side]
            assert [r['n'] for r in rows] == list(range(1, len(rows) + 1)), session['id']
            for row in rows:
                assert row['kind'] in ('exercise', 'routine')
                assert row['status'] in ('shared', 'unique', 'mixed')
                assert set(row['exercise_ids']) <= ids
                assert (row['kind'] == 'exercise') == bool(row['exercise_ids'])
        for item in session['exercises']:
            assert item['category'] in CATEGORIES, (session['id'], item['id'])
            assert item['A'] or item['B'] or item.get('conditional_for')
            for side in ('A', 'B'):
                assert all(1 <= n <= len(session['topics'][side]) for n in item[side])
    by_id = {s['id']: s for s in sessions}
    assert all(by_id['mftd-2']['setup'][side]['TRIP FUEL (t)'] == '2.7' for side in ('A','B'))
    assert all(by_id['mftd-2']['weather'][side]['departure']['runway'] == '18' for side in ('A','B'))
    assert all(by_id['mftd-6']['setup'][side]['T/O FUEL (t)'] == '10' and
               by_id['mftd-6']['setup'][side]['TOW (t)'] == '58' for side in ('A','B'))
    assert all(by_id['ffs-3']['weather'][side]['departure']['runway'] == '25L' and
               by_id['ffs-3']['weather'][side]['arrival']['airport'] == 'VTBS' for side in ('A','B'))
    assert all(by_id['ffs-4']['setup'][side]['CRZ FL'] == '9,000 ft' for side in ('A','B'))
    assert all(by_id['ffs-9']['setup'][side][field] == '—'
               for side in ('A','B') for field in ('ROUTE','CRZ FL','TRIP FUEL (t)'))
    for sid, groups in PROCEDURE_GROUPS.items():
        labels = [label for label, _ in groups]
        assert set(labels) <= set(FAILURE_SUMMARIES[sid]), (sid, set(labels) - set(FAILURE_SUMMARIES[sid]))
        slugs = [slug for slug, _, _ in members(groups)]
        assert len(slugs) == len(set(slugs)), sid
        session_ids = {e['id'] for e in by_id[sid]['exercises']}
        for label, entries in groups:  # every group is reachable from at least one exercise row
            assert any(EXERCISE_BRIEFS.get(eid) in {e[0] for e in entries} for eid in session_ids), (sid, label)
    mapped = {slug for groups in PROCEDURE_GROUPS.values() for slug, _, _ in members(groups)}
    for exercise_id, slug in EXERCISE_BRIEFS.items():
        sid = exercise_id.rsplit('-e', 1)[0]
        assert exercise_id in FAILURE_IDS, exercise_id
        assert exercise_id in {e['id'] for e in by_id[sid]['exercises']}, exercise_id
        assert slug in mapped, slug
    assert set(EXERCISE_BRIEFS.values()) <= mapped, set(EXERCISE_BRIEFS.values()) - mapped


def brief_view(brief, label, trainees, note=''):
    view = dict(brief)
    view['tab_label'] = label
    view['trainees'] = trainees
    view['session_note'] = note
    view['alert_label'] = ALERT_LABELS[brief['alert']['level']]
    view['procedure_refs'] = [collect_refs(proc, []) for proc in brief['procedures']]
    view['source_count'] = len(collect_refs(brief, []))
    # STATUS limitation lines written as "ITEM ....... VALUE" share the drawn leader.
    view['status_limits'] = []
    for line in (brief.get('status') or {}).get('limitations', []):
        item, sep, setting = line['text'].partition(' ....... ')
        view['status_limits'].append(
            {**line, 'kind': 'action', 'item': item, 'setting': setting, 'text': '', 'level': 0} if sep
            else {**line, 'kind': 'info', 'level': 0})
    return view


def procedure_view(session, briefs):
    sid = session['id']
    by_exercise = {e['id']: e for e in session['exercises']}
    groups = []
    for index, entry in enumerate(PROCEDURE_GROUPS.get(sid, ())):
        label = entry[0]
        group_exercises = [by_exercise[eid] for eid, s in EXERCISE_BRIEFS.items()
                           if eid in by_exercise and s in {m[0] for m in entry[1]}]
        items = []
        for slug, tab_label, note in members([entry]):
            exercises = [by_exercise[eid] for eid, s in EXERCISE_BRIEFS.items() if s == slug and eid in by_exercise]
            # a companion brief (no exercise row of its own) is practised by the group's trainees
            trainees = [side for side in ('A', 'B') if any(e[side] for e in (exercises or group_exercises))]
            items.append(brief_view(briefs[slug], tab_label, trainees, note))
        groups.append({'id': f'{sid}-procedures-{index + 1}', 'label': label, 'briefs': items})
    group_of = {b['slug']: g for g in groups for b in g['briefs']}
    session['procedure_groups'] = groups
    session['summary_items'] = [
        {'label': label, 'group': next((g for g in groups if g['label'] == label), None)}
        for label in FAILURE_SUMMARIES[sid]]
    for exercise in session['exercises']:
        slug = EXERCISE_BRIEFS.get(exercise['id'])
        exercise['brief'] = slug
        exercise['brief_group'] = group_of[slug]['id'] if slug else None
    for side in ('A', 'B'):
        for topic in session['topics'][side]:
            slug = next((EXERCISE_BRIEFS[e] for e in topic['exercise_ids'] if e in EXERCISE_BRIEFS), None)
            topic['brief'] = slug
            topic['brief_group'] = group_of[slug]['id'] if slug else None


def view_model(data, briefs):
    sessions = data['sessions']
    for session in sessions:
        sid = session['id']
        session['failure_summary'] = ' • '.join(FAILURE_SUMMARIES[sid]) or 'No failure exercises.'
        procedure_view(session, briefs)
        session['topics_different'] = any(
            row['status'] != 'shared'
            for side in ('A', 'B') for row in session['topics'][side])
        for exercise in session['exercises']:
            exercise['failure_related'] = exercise['id'] in FAILURE_IDS
        for side in ('A', 'B'):
            for topic in session['topics'][side]:
                topic['failure_related'] = bool(set(topic['exercise_ids']) & FAILURE_IDS)
        session['setup_rows'] = [
            {'label': label,
             'a': shown(session['setup']['A'][key], unspecified=sid == 'ffs-9' and key in ('ROUTE','CRZ FL','TRIP FUEL (t)')),
             'b': shown(session['setup']['B'][key], unspecified=sid == 'ffs-9' and key in ('ROUTE','CRZ FL','TRIP FUEL (t)')),
             'different': session['setup']['A'][key] != session['setup']['B'][key]}
            for key, label in SETUP_FIELDS
        ]
        session['setup_shared'] = not any(row['different'] for row in session['setup_rows'])
        session['route_row'] = session['setup_rows'][-1]
        session['setup_fields'] = session['setup_rows'][:-1]
        phases = []
        for phase, name in (('departure', 'Departure'), ('arrival', 'Arrival')):
            rows = []
            for key, label in WEATHER_FIELDS:
                a = shown(session['weather']['A'][phase][key])
                b = shown(session['weather']['B'][phase][key])
                rows.append({'label': label, 'a': a, 'b': b, 'different': a != b})
            phases.append({'name': name, 'rows': rows,
                           'shared': not any(row['different'] for row in rows)})
        session['weather_phases'] = phases
        setup_by_label = {row['label']: row for row in session['setup_rows']}
        runway = {
            side: ' / '.join(shown(session['weather'][side][phase]['runway'])
                             for phase in ('departure', 'arrival'))
            for side in ('A', 'B')
        }
        session['brief_setup'] = [
            setup_by_label['From / to'],
            {'label': 'Runways · dep / arr', 'a': runway['A'], 'b': runway['B'],
             'different': runway['A'] != runway['B']},
            setup_by_label['Planned cruise'], setup_by_label['TOW (t)'],
            setup_by_label['Take-off fuel (t)'],
        ]
        session['brief_conditions'] = []
        for phase, name in (('departure', 'Departure'), ('arrival', 'Arrival')):
            values = {
                side: ' · '.join(shown(session['weather'][side][phase][key])
                                  for key in ('wind', 'ceiling', 'runway_condition'))
                for side in ('A', 'B')
            }
            visibility = {side: shown(session['weather'][side][phase]['visibility'])
                          for side in ('A', 'B')}
            session['brief_conditions'].append({'name': name, 'rows': [
                {'label': 'Wind · ceiling · runway', 'a': values['A'], 'b': values['B'],
                 'different': values['A'] != values['B']},
                {'label': 'Visibility', 'a': visibility['A'], 'b': visibility['B'],
                 'different': visibility['A'] != visibility['B']},
            ]})
        session['brief_setup_different'] = any(row['different'] for row in session['brief_setup'])
        session['brief_conditions_different'] = any(
            row['different'] for phase in session['brief_conditions'] for row in phase['rows'])
        session['difference_count'] = sum(row['different'] for row in session['setup_rows']) + sum(
            row['different'] for phase in phases for row in phase['rows'])
        session['exercise_categories'] = [
            {'name': name, 'items': [e for e in session['exercises'] if e['category'] == name]}
            for name in CATEGORIES
            if any(e['category'] == name for e in session['exercises'])
        ]
    return sessions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    # Keep the previous invocation compatible; every build is now HTML-only.
    parser.add_argument('--html-only', action='store_true', help=argparse.SUPPRESS)
    parser.parse_args()
    data = json.loads(DATA.read_text(encoding='utf-8'))
    validate(data)
    sessions = view_model(data, load_briefs())
    # The template ends in .j2, so extension-based autoescape would leave
    # syllabus text such as "SLATS <1" as raw HTML.
    env = Environment(loader=FileSystemLoader(ROOT), autoescape=True)
    template = env.get_template('comparison_template.html.j2')
    html = template.render(sessions=sessions)
    html = '\n'.join(line if line.strip() else '' for line in html.split('\n'))
    HTML_OUT.write_text(html, encoding='utf-8')
    print(f'HTML: {HTML_OUT}')
    print(f'{len(sessions)} sessions · {sum(len(s["exercises"]) for s in sessions)} practice groups · '
          f'{sum(len(g["briefs"]) for s in sessions for g in s["procedure_groups"])} procedure briefs')


if __name__ == '__main__':
    main()
