#!/usr/bin/env python3
"""Validate an abnormals/<slug>.json brief (schema a320-ecam-abnormal/2) and
render abnormals/<slug>.md next to it.

Usage: python3 -I render_md.py abnormals/<slug>.json [--check]
"""
import json
import sys
from pathlib import Path

SCHEMA = 'a320-ecam-abnormal/3'
LEVELS = {'warning': 'Red warning', 'caution': 'Amber caution', 'qrh': 'QRH procedure',
          'memory': 'Memory items', 'technique': 'Technique'}
LANES = ('PF', 'PM', 'BOTH')


def fail(msg):
    sys.exit(f'invalid brief: {msg}')


def check_refs(obj, where):
    refs = obj.get('refs')
    if not refs:
        fail(f'{where}: missing refs')
    for r in refs:
        if not {'book', 'code', 'page', 'pdf'} <= set(r):
            fail(f'{where}: bad ref {r}')


def validate(d):
    if d.get('schema') != SCHEMA:
        fail(f"schema must be {SCHEMA}")
    for key in ('slug', 'title', 'kind', 'alert', 'effectivity', 'summary', 'key_limits', 'flow',
                'procedures', 'background', 'sources'):
        if key not in d:
            fail(f'missing {key}')
    if d['alert']['level'] not in LEVELS:
        fail('alert.level')
    branches = set(d['effectivity'].get('branches') or []) | {'all'}

    def applies(obj, where):
        bad = set(obj.get('applies_to', ['all'])) - branches
        if bad:
            fail(f'{where}: unknown branch {bad}')

    for i, k in enumerate(d['key_limits']):
        check_refs(k, f'key_limits[{i}]')
        applies(k, f'key_limits[{i}]')

    def items(seq, where):
        for j, it in enumerate(seq):
            if it['kind'] not in ('callout', 'action', 'ecam', 'condition', 'note'):
                fail(f'{where}[{j}].kind')
            check_refs(it, f'{where}[{j}]')
            applies(it, f'{where}[{j}]')
            items(it.get('children', []), f'{where}[{j}].children')

    for i, ph in enumerate(d['flow']):
        if not ph.get('steps'):
            fail(f'flow[{i}] has no steps')
        for k, step in enumerate(ph['steps']):
            if step.get('actor') not in LANES:
                fail(f'flow[{i}].steps[{k}].actor')
            items(step['items'], f'flow[{i}].steps[{k}]')
    for i, p in enumerate(d['procedures']):
        for j, ln in enumerate(p['lines']):
            check_refs(ln, f'procedures[{i}].lines[{j}]')
            applies(ln, f'procedures[{i}].lines[{j}]')
    for key in ('background', 'technique', 'gaps'):
        for i, t in enumerate(d.get(key, [])):
            check_refs(t, f'{key}[{i}]')
    if d.get('status'):
        for key in ('limitations', 'info', 'appr_proc', 'inop_sys'):
            for i, t in enumerate(d['status'].get(key, [])):
                check_refs(t, f'status.{key}[{i}]')
    for i, q in enumerate(d.get('qrh', [])):
        for s in q['sections']:
            for j, t in enumerate(s['lines']):
                check_refs(t, f'qrh[{i}].{s["name"]}[{j}]')
    for i, t in enumerate(d.get('tables', [])):
        check_refs(t, f'tables[{i}]')
        if any(len(r) != len(t['columns']) for r in t['rows']):
            fail(f'tables[{i}] row width')


def ref(r):
    if r['book'] == 'QRH':
        return f"QRH {r['page']}, PDF {r['pdf']}"
    if r['book'] == 'PDP':
        return f"PDP {r['code']}, PDF {r['pdf']}"
    return f"{r['book']} {r['code']} {r['page']}, PDF {r['pdf']}"


def refs(rs):
    seen, out = set(), []
    for r in rs:
        k = ref(r)
        if k not in seen:
            seen.add(k)
            out.append(k)
    return '[' + '; '.join(out) + ']'


def branch(obj):
    a = obj.get('applies_to', ['all'])
    return '' if a == ['all'] else '**[' + ', '.join(a) + ']** '


def line_md(ln):
    pad = '  ' * ln.get('level', 0)
    if ln['kind'] == 'action':
        body = f"{ln['item']} …… {ln['setting']}" + (f" — {ln['text']}" if ln.get('text') else '')
    elif ln['kind'] == 'condition':
        body = f"**{ln['text']}**"
    elif ln['kind'] == 'caution':
        body = f"**CAUTION** {ln['text']}"
    elif ln['kind'] == 'land_asap':
        body = f"**{ln['text']}**"
    else:
        body = f"*{ln['text']}*"
    return f"{pad}- {branch(ln)}{body} {refs(ln['refs'])}"


def flow_md(it, depth=0):
    pad = '  ' * depth
    if it['kind'] == 'callout':
        body = f"“{it['text']}”"
    elif it['kind'] == 'ecam':
        body = f"{it['item']} …… {it['setting']}"
    elif it['kind'] == 'condition':
        body = f"**{it['text']}**"
    else:
        body = it['text']
    out = [f"{pad}- {branch(it)}{body} {refs(it['refs'])}"]
    for ch in it.get('children', []):
        out += flow_md(ch, depth + 1)
    return out


def render(d):
    a = d['alert']
    o = [f"# {d['title']} — handling plan (HS-TX)", '',
         '> Study aid built from uncontrolled copies of the THA A320/A321 FCOM, FCTM and QRH '
         '(14 JUL 26 edition) and the Airbus PDP tutorials (Jan 2024) in `books/`. Not for operational use. '
         f"Generated {d['generated']} with the `a320-ecam-abnormal` skill.", '']
    bits = [LEVELS[a['level']]]
    if a.get('land_asap', 'none') != 'none':
        bits.append(f"{a['land_asap']} LAND ASAP")
    bits.append('memory items' if a.get('memory_items') else 'no memory items')
    if a.get('qrh_summary'):
        bits.append('QRH summary')
    o += [f"**{' · '.join(bits)}**  ", f"**Applicability:** "
          + (', '.join(d['effectivity']['branches']) or 'all HS-TX')
          + (f" — {d['effectivity']['note']}" if d['effectivity'].get('note') else ''), '',
          d['summary'], '', '## 1. What it is']
    if a.get('trigger'):
        o.append(f"- **Trigger:** {a['trigger']} {refs(a['refs'])}")
    ph = a.get('inhibited_phases')
    o.append(f"- **Flight phase inhibition:** {'phases ' + ', '.join(map(str, ph)) if ph else 'none'} "
             f"{refs(a['refs'])}")
    o += [f"- {branch(t)}{t['text']} {refs(t['refs'])}" for t in d['background']]
    o += ['', '## 2. Key limits']
    o += [f"- {branch(k)}**{k['label']}:** {k['value']} {refs(k['refs'])}" for k in d['key_limits']]
    o += ['', '## 3. Flow (PF / PM)']
    for n, p in enumerate(d['flow'], 1):
        o.append(f"### {n}. {p['phase']}")
        for k, step in enumerate(p['steps'], 1):
            who = 'PF + PM' if step['actor'] == 'BOTH' else step['actor']
            o.append(f"**{n}.{k} {who}**")
            for it in step['items']:
                o += flow_md(it)
        o.append('')
    o.append('## 4. Procedure')
    for p in d['procedures']:
        o += [f"### {p['title']} ({p['source']})"] + [line_md(ln) for ln in p['lines']] + ['']
    if d.get('status'):
        s = d['status']
        o.append('## 5. STATUS')
        for key, name in (('limitations', 'Limitations'), ('info', 'Information'),
                          ('appr_proc', 'APPR PROC'), ('inop_sys', 'INOP SYS')):
            if s.get(key):
                o.append(f'**{name}**')
                o += [line_md(x) if 'kind' in x else f"- {branch(x)}{x['text']} {refs(x['refs'])}"
                      for x in s[key]]
        o.append('')
    if d.get('qrh') or d.get('tables'):
        o.append('## 6. QRH and reference tables')
        for q in d.get('qrh', []):
            o.append(f"### {q['title']}")
            for sec in q['sections']:
                o.append(f"**{sec['name']}**")
                o += [f"- {branch(t)}{t['text']} {refs(t['refs'])}" for t in sec['lines']]
        for t in d.get('tables', []):
            o += [f"### {t['title']} {branch(t)}", t.get('caption', ''), '',
                  '| ' + ' | '.join(t['columns']) + ' |', '|' + '---|' * len(t['columns'])]
            o += ['| ' + ' | '.join(r) + ' |' for r in t['rows']]
            o += [refs(t['refs']), '']
    if d.get('technique'):
        o += ['## 7. FCTM technique'] + [f"- {branch(t)}{t['text']} {refs(t['refs'])}" for t in d['technique']] + ['']
    if d.get('related'):
        o += ['## 8. Related procedures', '| Procedure | Why | Key actions | Ref |', '|---|---|---|---|']
        o += [f"| {r['title']} | {r['why']} | {'; '.join(r['key_actions'])} | {refs(r['refs'])} |" for r in d['related']]
        o.append('')
    o.append('## 9. HS-TX differences')
    if d.get('differences'):
        br = d['effectivity']['branches']
        keys = sorted({k for x in d['differences'] for k in x['values']})
        o += ['| Topic | ' + ' | '.join(keys) + ' | Ref |', '|' + '---|' * (len(keys) + 2)]
        o += [f"| {x['topic']} | " + ' | '.join(x['values'].get(k, '—') for k in keys) + f" | {refs(x['refs'])} |"
              for x in d['differences']]
    else:
        o.append('None — the content applies to every HS-TX registration.')
    o += ['', '## 10. Gaps and omissions'] + [f"- {t['text']} {refs(t['refs'])}" for t in d.get('gaps', [])]
    o += ['', '## Sources', '| Book | Section | Pages | PDF | Rev |', '|---|---|---|---|---|']
    o += [f"| {s['book']} | {s['section']} | {s['pages']} | {s['pdf']} | {s.get('rev', '')} |" for s in d['sources']]
    return '\n'.join(o) + '\n'


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    d = json.loads(path.read_text(encoding='utf-8'))
    validate(d)
    if '--check' in sys.argv:
        print(f'{path}: OK')
        return
    out = path.with_suffix('.md')
    out.write_text(render(d), encoding='utf-8')
    print(f'{path}: OK -> {out}')


if __name__ == '__main__':
    main()
