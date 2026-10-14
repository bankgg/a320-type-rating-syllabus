#!/usr/bin/env python3
"""Review and freeze the exercise mapping in syllabus_sessions.json.

This curation step is deliberately separate from rendering. The HTML/PDF builder
reads only the reviewed JSON and never guesses whether two topics are equivalent.
"""

import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'syllabus_sessions.json'


def normalize(t):
    t = t.lower().replace('–', '-').replace('‑', '-').replace('one engine in-op', 'one engine inoperative')
    t = t.replace('takeoff', 'take-off').replace('go around', 'go-around')
    t = t.replace('oei', 'one engine inoperative')
    t = t.replace('3d (ils)', 'ils').replace('3d ils', 'ils').replace('2d loc', 'loc')
    t = re.sub(r'(\d)\+(\d)', r'\1plus\2', t)
    t = re.sub(r'\b(during|for|the|a|an|using|with|to|of|as)\b', ' ', t)
    return re.sub(r'[^a-z0-9]+', ' ', t).strip()


def similar(a, b):
    na, nb = normalize(a), normalize(b)
    if na == nb:
        return True
    if 'uprt recovery' in na and 'uprt recovery' in nb:
        for attitude in ('nose high', 'nose low'):
            if attitude in na and attitude in nb:
                return True
    protected = ('packs off', 'packs on', 'one engine inoperative', 'engine failure',
                 'engine fire', 'unreliable speed', 'manual', 'without fd', 'with fd',
                 'with ap', 'raw data', 'rnp', 'ils', 'vor', 'loc', '2d', '3d',
                 'lnav vnav', 'lnav minima', 'contaminated', 'overweight',
                 'crosswind', 'fuel leak', 'fuel imbalance', 'slats', 'flaps',
                 'adr', 'ir ', 'hyd g b', 'hyd g y', 'emergency', 'evacuation',
                 'go around', 'windshield', 'windshear', 'gear', 'cargo smoke',
                 'nose high', 'nose low', 'pump 1plus2', 'pump 1 2',
                 'conf 1 f', 'conf 2', 'conf 3', 'nav fpa', 'trk fpa',
                 'loc fpa', 'final app')
    if any((term in na) != (term in nb) for term in protected):
        return False
    return SequenceMatcher(None, na, nb).ratio() >= .89


def is_practice(t):
    n = normalize(t)
    if n.startswith('init '):
        return False
    if n.startswith('reposition final') and 'practice' not in n:
        return False
    if n in ('descend', 'cruise', 'engine start', 'taxiing'):
        return False
    special = ('fault', 'fail', 'fire', 'smoke', 'evacuation', 'stall', 'windshear', 'tcas',
               'depressur', 'emergency descent', 'unreliable', 'fuel leak', 'fuel imbalance',
               'gravity fuel', 'relight', 'hyd ', 'idg ', 'anti ice', 'elec ', 'fmg',
               'adr ', 'ir ', 'f ctl', 'slats', 'flaps', 'gear ', 'loss braking',
               'overweight', 'manual flight', 'roll rate', 'pitch change', 'yaw ',
               'fly by wire', 'jet engine', 'mach buffet', 'tuck under', 'egpws',
               'sdac', 'fwc', 'fcu', 'rmp', 'acp', 'apu', 'crossbleed', 'cross bleed',
               'air start', 'slippery', 'mode reversion', 'managed clb', 'thr logic',
               'a p logic', 'ground speed mini', 'contaminated', 'braking action',
               'approach to da', 'manual landing', 'cabin pressure',
               'structural damage', 'predictive', 'incapacitation')
    if any(k in n for k in special):
        return True
    if n.startswith('radar vectors') and 'approach' in n:
        return True
    if n.startswith(('preflight ', 'before take', 'after landing', 'taxi ', 'taxiing ',
                     'engine start', 'cockpit preparation', 'use checklist',
                     'performance calculation', 'follow sid', 'follow star',
                     'follow atc', 'radar vector', 'reposition', 'cruise', 'descend ',
                     'climb fl', 'climb to cleared', 'climb 10 000', 'procedures no ext')):
        return False
    return True

# Printed row numbers, one-based. These corrections were reviewed against the
# photographed A sheets and the extracted B syllabus.
INCLUDE = {
    'mftd-4': {'B': [4, 9]},  # manual engine start; FPV/FPD demo
    'mftd-9': {'A': [4]},     # manual engine start
}
EXCLUDE = {
    'ffs-1': {'B': [21]},   # routine engine shutdown/parking
    'ffs-2': {'B': [19]},   # RNAV STAR/radar-vector setup, not the RNP exercise
    'ffs-3': {'A': [18], 'B': [15]},  # setup for EGPWS, alert itself is retained
    'ffs-9': {'A': [8], 'B': [8]},    # routine climb to cleared FL
}

# Equivalent practice rows that differ in wording, or compound printed rows
# that represent the same exercise. Meaningfully different variants stay apart.
MERGE = {
    'mftd-3': [('A', 12, 'B', 10)],
    'mftd-5': [('A', 8, 'B', 6), ('A', 12, 'B', 10), ('A', 11, 'B', 8)],
    'mftd-6': [('A', 7, 'B', 10), ('A', 7, 'B', 11)],
    'mftd-7': [('A', 8, 'B', 5), ('A', 8, 'B', 6)],
    'mftd-8': [('A', 6, 'B', 13), ('A', 10, 'B', 18)],
    'mftd-9': [('A', 7, 'B', 6)],
    'ffs-1': [('A', 21, 'B', 18)],
    'ffs-2': [('A', 4, 'B', 8), ('A', 14, 'B', 18), ('A', 22, 'B', 26)],
    'ffs-3': [('A', 3, 'B', 3), ('A', 11, 'B', 8), ('A', 14, 'B', 11),
              ('A', 16, 'B', 13), ('A', 20, 'B', 17), ('A', 21, 'B', 18),
              ('A', 25, 'B', 22)],
    'ffs-4': [('A', 9, 'B', 9)],
    'ffs-5': [('A', 5, 'B', 4), ('A', 14, 'B', 11)],
    'ffs-6': [('A', 4, 'B', 4), ('A', 11, 'B', 7), ('A', 12, 'B', 16),
              ('A', 17, 'B', 16), ('A', 10, 'A', 12), ('A', 21, 'B', 11)],
    'ffs-7': [('A', 3, 'B', 3), ('A', 4, 'B', 4), ('A', 11, 'B', 22),
              ('A', 15, 'B', 10), ('A', 18, 'B', 14), ('A', 19, 'B', 16)],
    'ffs-9': [('A', 19, 'B', 20)],
}

BLOCK = {
    'ffs-4': {(('A', 10), ('B', 10))}, # structural damage suspected vs no damage
}

# A printed row can cover two exercises. The second group receives the same
# source row without joining the two distinct exercises together.
EXTRA_REF = {
    'ffs-1': [(('A', 22), ('B', 18))],   # B combines autoland and manual landing practice
    'ffs-7': [(('A', 10), ('B', 22))],  # B combines overweight ILS and landing
}

NOTES = {
    ('mftd-3', 'A12'): 'B specifies LNAV/VNAV minima.',
    ('mftd-8', 'A6'): 'A specifies LOC/FPA; B does not specify a guidance mode.',
    ('mftd-9', 'A7'): 'A specifies packs OFF; B does not specify a packs setting.',
    ('ffs-2', 'A4'): 'B also covers stall warning or stall avoidance devices.',
    ('ffs-2', 'A14'): 'A combines this with RNAV STAR or radar vectors; B lists that setup separately.',
    ('ffs-3', 'A3'): 'A specifies use during engine start; B lists use of engine anti-ice.',
    ('ffs-3', 'A20'): 'B specifies a 200 ft DH/A.',
    ('ffs-3', 'A21'): 'B places landing windshear close to minima.',
    ('ffs-3', 'A25'): 'B adds more crosswind landing practice if time permits.',
    ('ffs-5', 'A5'): 'A repositions to FL350 after restart.',
    ('ffs-7', 'A4'): 'A also includes an ARS demonstration at 210 kt.',
    ('ffs-7', 'A11'): 'B combines the overweight landing with manual ILS.',
    ('ffs-7', 'A15'): 'A specifies that RNP degradation leads to a go-around; B lists degradation or system malfunction.',
    ('ffs-7', 'A19'): 'A specifies the engine inoperative before passing 1,000 ft AAL.',
    ('ffs-6', 'A10'): 'A repeats this landing across hydraulic and flap-fault scenarios.',
    ('ffs-10', 'A24'): 'B specifies a reasonable speed below V1.',
}

TITLES = {
    ('mftd-5', 'A15'): 'Emergency evacuation procedure review',
    ('mftd-4', 'B9'): 'FPV (bird) and FPD demonstration',
    ('mftd-6', 'B9'): 'Removal of smoke/fumes',
    ('mftd-8', 'A6'): '2D LOC approach to MDH/A',
    ('mftd-9', 'A7'): 'Instrument takeoff',
    ('mftd-9', 'A12'): 'Overweight landing procedures with LOC/DME vectors',
    ('ffs-1', 'A22'): 'Manual landing practice ×2',
    ('ffs-2', 'A14'): 'Procedural instrument flying and manoeuvring',
    ('ffs-3', 'A3'): 'Use of engine anti-ice',
    ('ffs-3', 'A20'): 'ILS approach with glide-slope interception from above',
    ('ffs-4', 'A9'): 'Tuck under and Mach buffet in Normal and Alternate law',
    ('ffs-5', 'A5'): 'Engine relight in flight',
    ('ffs-6', 'A10'): 'Landing with partial/no flaps or slats',
    ('ffs-7', 'A4'): 'Takeoff at maximum mass in crosswind',
    ('ffs-7', 'A15'): '3D RNP approach to LNAV/VNAV minima with degraded RNP',
    ('ffs-7', 'A18'): 'APU AUTO (EMER) SHUT DOWN',
    ('ffs-7', 'A19'): 'ILS approach manually with FD, one engine inoperative',
}

OVERVIEW = [
    'Packs OFF and managed-climb/FMGC work for A; packs ON for B.',
    'APU MEL and crossbleed start for A; ground-speed mini and braking for B.',
    'Fuel-feed/IDG/relight work for A; FMGC/FPV/cabin-pressure work for B.',
    'Hot start, cargo smoke and evacuation for A; engine/hydraulic/braking failures for B.',
    'Unreliable speed, ADR and fuel leak for A; start-valve and smoke for B.',
    'A adds relight/RNP and V2 takeoff failure; B adds fire and evacuation.',
    'A focuses on OEI approaches and RTO; B on FMGC resets and emergency electrical.',
    'Routes run in opposite directions; A focuses on engine fire/OEI, B on contamination and gear.',
    'A introduces RMP/ACP; B adds sidestick priority. Handling exercises overlap.',
    'A adds 3D RNP; both cover stalls, visual circuits and 2D RNP.',
    'A adds cold-weather preflight/taxi; arrival handling largely overlaps.',
    'IR faults and suspected damage for A; ADR faults and no-damage descent for B.',
    'Dual-engine failure/RNP for A; unreliable speed/manual ILS for B. Alternate branch depends on crew roles.',
    'A adds G+B hydraulics, flaps fault and RNP; B adds slats fault and gravity gear.',
    'Opposite routes; A focuses on FCU/overweight/severe damage, B on windshear/fuel leak/APU fire.',
    'The UPRT exercise sequence is the same for both trainees.',
    'Opposite routes; EDTO failures differ at EEP, ETOPS entry and ETP.',
    'The skill-test exercise sequence matches; departure and arrival weather differ.',
]


def is_exercise(session_id, side, number, text):
    if number in EXCLUDE.get(session_id, {}).get(side, []):
        return False
    if number in INCLUDE.get(session_id, {}).get(side, []):
        return True
    return is_practice(text)


def compatible(a, b):
    na, nb = normalize(a), normalize(b)
    # These names denote distinct systems/conditions despite similar wording.
    for term in ('sdac', 'fwc', 'no damage', 'structural damage', 'pump 1plus2',
                 'hyd g b', 'hyd g y', 'slats', 'flaps', 'nose high', 'nose low',
                 'without autopilot', 'max crosswind'):
        if (term in na) != (term in nb):
            return False
    return similar(a, b)


def category(text):
    n = normalize(text)
    if any(x in n for x in ('uprt', 'stall', 'roll rate', 'yaw ', 'pitch change',
                             'turns', 'manual flight', 'fly by wire', 'jet engine',
                             'visual circuit', 'holding procedure', 'mach buffet',
                             'tuck under', 'exercise ')):
        return 'Flight handling'
    if 'take off' in n or 'rto' in n or 'engine start' in n or 'start fault' in n:
        return 'Takeoff & departure'
    if 'approach' in n or 'go around' in n or 'discontinued approach' in n:
        return 'Approaches & go-arounds'
    if 'landing' in n or 'autoland' in n or 'loss braking' in n:
        return 'Landing'
    return 'Failures & systems'


def root_of(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def join(parent, x, y):
    x, y = root_of(parent, x), root_of(parent, y)
    if x != y:
        parent[y] = x


def curate_session(s):
    sid = s['id']
    original_topics = {'A': list(s['topics']['A']), 'B': list(s['topics']['B'])}
    nodes = {}
    for side in 'AB':
        for n, text in enumerate(original_topics[side], 1):
            if is_exercise(sid, side, n, text):
                nodes[(side, n)] = text
    parent = {x: x for x in nodes}
    # Seed only the data compilation step; the final renderer has no matcher.
    keys = list(nodes)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if (a, b) in BLOCK.get(sid, set()) or (b, a) in BLOCK.get(sid, set()):
                continue
            if compatible(nodes[a], nodes[b]):
                join(parent, a, b)
    for sa, na, sb, nb in MERGE.get(sid, []):
        a, b = (sa, na), (sb, nb)
        assert a in nodes and b in nodes, (sid, a, b)
        join(parent, a, b)
    if sid in ('ffs-8', 'ffs-10'):
        for n in range(1, min(len(original_topics['A']), len(original_topics['B'])) + 1):
            a, b = ('A', n), ('B', n)
            if a in nodes and b in nodes:
                join(parent, a, b)
    groups = {}
    for key in keys:
        groups.setdefault(root_of(parent, key), set()).add(key)
    for anchor, extra in EXTRA_REF.get(sid, []):
        assert anchor in nodes and extra in nodes
        groups[root_of(parent, anchor)].add(extra)
    # Sort by the first A occurrence, then B-only items in B order.
    ordered = sorted(groups.values(), key=lambda g: (0, min(n for side, n in g if side == 'A'))
                     if any(side == 'A' for side, _ in g) else (1, min(n for _, n in g)))
    exercises = []
    for j, g in enumerate(ordered, 1):
        refs = {side: sorted(n for ss, n in g if ss == side) for side in 'AB'}
        first = ('A', refs['A'][0]) if refs['A'] else ('B', refs['B'][0])
        anchor = f'{first[0]}{first[1]}'
        title = TITLES.get((sid, anchor), nodes[first])
        note = NOTES.get((sid, anchor), '')
        exercises.append({'id': f'{sid}-e{j:02d}', 'title': title,
                          'category': category(title), 'A': refs['A'], 'B': refs['B'],
                          'note': note})
    # The FFS 5 emergency-electrical exercise appears in A's main and alternate
    # branches. B receives it only in the both-captains alternate branch.
    if sid == 'ffs-5':
        item = next(e for e in exercises if e['A'] == [16] and not e['B'])
        item['title'] = 'Emergency electrical configuration'
        item['conditional_for'] = 'B'
        item['condition'] = ('A performs this in either branch; if both trainees are co-pilots, '
                             'remove the malfunction after procedures. B performs it only '
                             'if both trainees are captains.')
    # B's printed line combines APU shutdown with an additional APU fire.
    if sid == 'ffs-7':
        shutdown_index = next(i for i, e in enumerate(exercises) if e['A'] == [18] and e['B'] == [14])
        exercises.insert(shutdown_index + 1,
                         {'id': 'ffs-7-apu-fire', 'title': 'APU fire',
                          'category': 'Failures & systems', 'A': [], 'B': [14],
                          'note': 'B combines this with APU emergency shutdown.'})
    s['exercises'] = exercises
    topic_groups = {'A': {}, 'B': {}}
    for e in exercises:
        for side in 'AB':
            for n in e[side]:
                topic_groups[side].setdefault(n, []).append(e['id'])
    for side in 'AB':
        rows = []
        other = 'B' if side == 'A' else 'A'
        for n, text in enumerate(original_topics[side], 1):
            gids = topic_groups[side].get(n, [])
            if gids:
                shared = any(next(e for e in exercises if e['id'] == gid)[other] for gid in gids)
                unique = any(not next(e for e in exercises if e['id'] == gid)[other] for gid in gids)
                status = 'mixed' if shared and unique else ('shared' if shared else 'unique')
                kind = 'exercise'
            else:
                status = ('shared' if sid in ('ffs-8', 'ffs-10') or
                          any(compatible(text, x) for x in original_topics[other]) else 'unique')
                kind = 'routine'
            rows.append({'n': n, 'text': text, 'kind': kind, 'status': status,
                         'exercise_ids': gids})
        s['topics'][side] = rows
    assert all(e['A'] or e['B'] or e.get('conditional_for') for e in exercises)
    assert all(row['exercise_ids'] for side in 'AB' for row in s['topics'][side]
               if row['kind'] == 'exercise'), sid


def main():
    data = json.loads(DATA.read_text())
    assert len(data['sessions']) == len(OVERVIEW) == 18
    for session, blurb in zip(data['sessions'], OVERVIEW):
        for side in 'AB':
            if session['topics'][side] and isinstance(session['topics'][side][0], dict):
                session['topics'][side] = [r['text'] for r in session['topics'][side]]
        session['overview'] = blurb
        curate_session(session)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('Curated', len(data['sessions']), 'sessions and',
          sum(len(s['exercises']) for s in data['sessions']), 'exercise groups')


if __name__ == '__main__':
    main()
