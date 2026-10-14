#!/usr/bin/env python3
"""Index, search and read the A320 FCOM / FCTM / QRH PDFs in books/.

Stdlib only; text comes from poppler's `pdftotext -layout`.  Run with
`python3 -I manuals.py <command> ...`.  Commands:

  index                         build/refresh the per-book cache
  find  "<ECAM title>"          locate the procedure in every book
  show  <book> <pdf-pages>      print pages with effectivity banners
  section <book> <code>         page range + headings of a section code
  grep  <book|all> <regex>      list pages whose text matches
  refs  <book> <pdf-pages>      cross-references on those pages
  render <book> <pdf-pages>     PNG of each page (view with the Read tool)

<book> is fcom, fctm or qrh.  <pdf-pages> is like 3215-3218 or 152,154.
Effectivity policy: blocks applicable only to HS-TO* aircraft are DROPPED;
ALL and any list containing an HS-TX* registration are KEPT.
"""
import difflib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REPO = SKILL_DIR.parent.parent.parent
BOOKS_DIR = Path(os.environ.get('A320_BOOKS', REPO / 'books'))
CACHE_DIR = SKILL_DIR / 'cache'
CACHE_VERSION = 11

BOOKS = {
    'fcom': ('A320FAM_FCOM_14JUL26_compressed.pdf', 'FCOM'),
    'fctm': ('A320FAM_FCTM_14JUL26.pdf', 'FCTM'),
    'qrh': ('A320FAM_QRH_14JUL26.pdf', 'QRH'),
    'pdp': ('Airbus Tutorial PDP Jan 2024.pdf', 'PDP'),
}

# Airbus "Tutorials (UPRT included) / Flow Patterns / Cockpit Panels" (Jan 2024):
# a slide deck, A320/A330 generic. Each module's opening slide carries a footer
# code; pages up to the next code belong to that module. Titles are ours.
PDP_MODULES = {
    'XFTDN1USETUTO01': 'How to use the tutorials', 'XFTDO1FRSTFFS01': 'First FFS session',
    'XFTDN1GOLDRUL01': 'Golden rules', 'EFTDB0FLOWPAT01': 'Flow patterns',
    'XFSNN1E00NAVC01': 'IFR charts / navigation', 'XFSNN1E00CPLN01': 'Cockpit panels',
    'EFTDB1COCKPRE01': 'Cockpit preparation', 'XFTDB1ENGSTAR01': 'Engine start',
    'EFTDB1TAXI00001': 'Taxi', 'EFTDB2TAKEOFF01': 'Takeoff', 'XFTDN2CLIMB0001': 'Climb',
    'XFTDN2CRUISE001': 'Cruise', 'XFTDN3DESCENT01': 'Descent', 'XFTDN12DAPPRO01': '2D approach',
    'XFTDN13DAPPRO01': '3D approach', 'XFTDN4GOAROUN01': 'Go-around', 'EFTDN1LANDING01': 'Landing',
    'XFTDB1AFTLDGD01': 'After landing', 'XFTDN1000AUTO01': 'Automation', 'XFTDN1CIRCLNG01': 'Circling',
    'XFTDN3GSABOVE01': 'Glide slope from above', 'XFTDN40GSMINI01': 'Ground speed mini',
    'XFTDN20ILSRAW01': 'ILS raw data', 'XFSNB10000LVO00': 'Low visibility operations',
    'XFTDN1000PROT01': 'Flight envelope protections', 'XFTDN2000BIRD01': 'Bird (FPV)',
    'XFTDN6ECAM00001': 'Management of abnormal operations', 'XFTDN1USESUMM01': 'Use of summary',
    'XFTDA1ALENGFO01': 'All engine flameout', 'EFTDA1DUALFM001': 'Dual FMGC failure',
    'XFTDA7EMERDES01': 'Emergency descent', 'XFTDA1EMREVAC01': 'Emergency evacuation',
    'XFTDA10ENGFTO01': 'Engine failure after V1', 'EFTDA1ENGFCRZ01': 'Engine failure in cruise',
    'EFTDN1RCFGLAW01': 'Reconfiguration laws', 'XFTDA1INCAPAC01': 'Crew incapacitation',
    'XFTDN1LOWENER01': 'Low energy', 'XFTDA6REJECTO01': 'Rejected takeoff',
    'XFTDA1SMOKE0001': 'Smoke', 'XFTDA4STALLRC01': 'Stall recovery',
    'XFTDA6UNRASPD01': 'Unreliable speed indication (and UPRT)', 'XFTDN3WINDSHR01': 'Windshear',
}
PDP_FOOT = re.compile(r'\b([A-Z0-9]{9,})\s+[–-]\s+(?:[A-Z0-9\-]+\s+[–-]\s+)?([A-Z]{3} \d{4})')

# ECAM / FCOM PRO-ABN system -> FCOM DSC chapters describing that system.
DSC_FOR_SYSTEM = {
    'A-ICE': ['DSC-30'], 'W_A_ICE': ['DSC-30'],
    'AIR': ['DSC-36', 'DSC-21'], 'BLEED': ['DSC-36'], 'COND': ['DSC-21'],
    'CAB_PR': ['DSC-21'], 'VENT': ['DSC-21'],
    'APU': ['DSC-49'], 'APUF': ['DSC-49', 'DSC-26'],
    'AUTO_FLT': ['DSC-22_10', 'DSC-22_30', 'DSC-22_40'],
    'AVNCS': ['DSC-21'], 'BRAKES': ['DSC-32'], 'NWS': ['DSC-32'],
    'LG': ['DSC-32'], 'WHEEL': ['DSC-32'],
    'COM': ['DSC-23'], 'DATALINK': ['DSC-46', 'DSC-23'],
    'CONFIG': ['DSC-31'], 'EIS': ['DSC-31'], 'FWS': ['DSC-31'],
    'RECORDER': ['DSC-31'], 'DOOR': ['DSC-52'],
    'ELEC': ['DSC-24'], 'C_B': ['DSC-24'],
    'ENG': ['DSC-70', 'DSC-26'], 'F_CTL': ['DSC-27'], 'FUEL': ['DSC-28'],
    'HYD': ['DSC-29'], 'NAV': ['DSC-34'], 'SURV': ['DSC-34'],
    'SMOKE': ['DSC-26', 'DSC-21'], 'OVERSPEED': ['DSC-27'],
    'T-O': ['DSC-31'], 'MISC': [], 'ABN': [], '90': [],
}

# FCOM PRO-ABN system name -> FCTM PR-AEP name where they differ.
FCTM_NAME = {'AUTO_FLT': 'AUTOFLT', 'BRAKES': 'BRK', 'NWS': 'BRK'}

FOOT_RE = re.compile(r'THA A320/A321 FLEET\s+(\S+) P (\d+)/(\d+)')
DATE_RE = re.compile(r'(\d{2} [A-Z]{3} \d{2})\s*$')
REG_RE = re.compile(r'HS-T[OX][A-Z]')
IDENT_RE = re.compile(r'^\s*Ident\.:\s*(\S+)(?:\s*/\s*(.+?))?\s*$')
APPL_RE = re.compile(r'^\s*Applicable to:\s*(.*)$')
BOILER = ('UNCONTROLLED IF DOWNLOADED OR PRINTED',)


# ---------------------------------------------------------------- indexing

def pdf_path(book):
    return BOOKS_DIR / BOOKS[book][0]


def extract_pages(book):
    out = subprocess.run(['pdftotext', '-layout', str(pdf_path(book)), '-'],
                         capture_output=True, text=True, check=True).stdout
    pages = out.split('\f')
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def page_meta(book, text):
    lines = text.splitlines()
    meta = {'code': None, 'page': None, 'of': None, 'date': None,
            'header': '', 'body_start': 0, 'body_end': len(lines)}
    nonempty = [i for i, l in enumerate(lines) if l.strip()]
    if not nonempty:
        return meta
    if book == 'pdp':  # slide deck: no headers; module code on opening slides only
        m = PDP_FOOT.search(text)
        if m:
            meta['code'], meta['date'] = m.group(1), m.group(2)
        return meta
    # header: up to the line naming the manual
    for i in nonempty[:10]:
        if re.search(r'OPERATING MANUAL|TECHNIQUES MANUAL|QUICK REFERENCE HANDBOOK', lines[i]):
            meta['body_start'] = i + 1
            break
    head = [lines[i] for i in nonempty if i < meta['body_start']]
    if book == 'qrh':
        # e.g. "ABNORMAL AND        18.01A" / "QUICK REFERENCE HANDBOOK   18 FEB 26"
        for l in head[1:3]:
            m = re.search(r'\s(\S+)\s*$', l)
            if m and re.search(r'\d', m.group(1)) and not DATE_RE.search(l):
                meta['code'] = m.group(1)
                break
        for l in head:
            m = DATE_RE.search(l)
            if m:
                meta['date'] = m.group(1)
        for i in reversed(nonempty):
            if 'THA A320/A321 FLEET' in lines[i]:
                meta['body_end'] = i
                break
    else:
        for i in reversed(nonempty[-6:]):
            m = FOOT_RE.search(lines[i])
            if m:
                meta.update(code=m.group(1), page=int(m.group(2)), of=int(m.group(3)),
                            body_end=i)
                if i + 1 < len(lines):
                    d = DATE_RE.search(lines[i + 1])
                    meta['date'] = d.group(1) if d else None
                break
    parts = []
    for l in head:
        s = re.sub(r'\s{2,}', ' / ', l.strip())
        if s in BOILER or not s:
            continue
        parts.append(s)
    meta['header'] = ' / '.join(parts)
    return meta


def classify(appl_text):
    """Return (scope, keep) for an 'Applicable to:' value."""
    if appl_text is None:
        return 'UNSPECIFIED', True
    regs = REG_RE.findall(appl_text)
    if not regs:
        if appl_text.strip().upper().startswith('ALL'):
            return 'ALL', True
        return 'UNSPECIFIED', True
    tx = sorted({r for r in regs if r.startswith('HS-TX')})
    if not tx:
        return 'HS-TO only', False
    order = 'ABCDEFGHJKLMNOPQRSTU'  # HS-TX fleet letters (no I)
    sfx = sorted({r[-1] for r in tx}, key=order.index)
    if ''.join(sfx) == order:
        label = 'all HS-TX'
    else:  # compress consecutive fleet letters into ranges
        parts, run = [], [sfx[0]]
        for c in sfx[1:]:
            if order.index(c) == order.index(run[-1]) + 1:
                run.append(c)
            else:
                parts.append(run)
                run = [c]
        parts.append(run)
        label = 'HS-' + ','.join(f'TX{r[0]}..TX{r[-1]}' if len(r) > 1 else f'TX{r[0]}'
                                 for r in parts)
    if len(tx) != len(set(regs)):
        label += ' (+HS-TO)'
    return label, True


def find_blocks(pages, metas):
    blocks = []
    current_appl = None
    for n, (text, meta) in enumerate(zip(pages, metas), start=1):
        lines = text.splitlines()
        lo, hi = meta['body_start'], meta['body_end']
        for i in range(lo, hi):
            m = IDENT_RE.match(lines[i])
            if not m:
                continue
            # applicability: just above (skipping blanks) or within 3 lines below
            appl, appl_idx = None, None
            j = i - 1
            while j >= lo and (not lines[j].strip()
                               or lines[j].strip().startswith(('HS-T', 'Criteria:'))):
                j -= 1
            for k in [j] + list(range(i + 1, min(i + 4, hi))):
                if k >= lo and APPL_RE.match(lines[k]):
                    appl_idx = k
                    appl = APPL_RE.match(lines[k]).group(1).strip()
                    q = k + 1
                    while q < hi and REG_RE.match(lines[q].strip() or 'x'):
                        appl += ' ' + lines[q].strip()
                        q += 1
                    break
            # title: first non-meta line above
            t = i - 1
            while t >= lo and (not lines[t].strip() or APPL_RE.match(lines[t])
                               or lines[t].strip().startswith(('Criteria:', 'HS-T'))):
                t -= 1
            title, parent, start = '', '', i
            cand_t = lines[t].strip() if t >= lo else ''
            if (cand_t and not IDENT_RE.match(lines[t]) and not cand_t[0].islower()
                    and not cand_t.endswith(('.', ':', ',', ';')) and '....' not in cand_t
                    and len(re.findall(r'[A-Za-z]', cand_t)) >= 3
                    and len(re.findall(r'[\d%°]', cand_t)) < 0.4 * len(cand_t.replace(' ', ''))):
                title = cand_t
                start = t
                p = t - 1
                while p >= lo and not lines[p].strip():
                    p -= 1
                if p >= lo:
                    cand = lines[p].strip()
                    bare = cand.replace("(Cont'd)", '').replace('(Cont’d)', '')
                    if (bare.isupper() and len(cand) < 90 and not cand.endswith(('.', ':'))
                            and not cand.startswith(('‐', '-', '•'))):
                        parent = cand
                if title.startswith('(') and parent:  # e.g. "ENG 1(2) FIRE" / "(IN FLIGHT)"
                    title, parent = parent + ' ' + title, ''
                    start = p
            if appl_idx is not None and appl_idx < start:
                start = appl_idx
            inherited = appl is None
            if appl is not None:
                current_appl = appl
            scope, keep = classify(current_appl)
            date = m.group(2)
            title, parent = re.sub(r'\s{2,}', '  ', title), re.sub(r'\s{2,}', '  ', parent)
            blocks.append({'pdf_page': n, 'line': start, 'ident': m.group(1), 'date': date,
                           'title': title, 'parent': parent, 'applicable': current_appl,
                           'inherited': inherited, 'scope': scope, 'keep': keep})
    return blocks


TOC_LINE = re.compile(r'^\s*(\S.*?)\s*\.{4,}\s*(\S*)\s*$')


def parse_toc(book, pages, metas):
    entries = []
    if book == 'fcom':
        section = None
        for n, (text, meta) in enumerate(zip(pages, metas), start=1):
            if meta['code'] != 'PRO-ABN-PLP-TOC':
                continue
            for line in text.splitlines():
                m = re.match(r'^(PRO-ABN-\S+)\s+(.*)$', line.strip())
                if m:
                    section = m.group(1)
                    continue
                m = TOC_LINE.match(line)
                if m and section:
                    title = re.sub(r'\s{2,}', ' ', m.group(1)).strip()
                    entries.append({'title': title, 'section': section, 'toc_page': n})
    elif book == 'qrh':
        chapter = None
        for n, (text, meta) in enumerate(zip(pages, metas), start=1):
            if n > 60:
                break
            for line in text.splitlines():
                m = re.match(r'^(\S.*?)\s{3,}((?:ABN|NP|OPS|OEB)\S*)\s*$', line)
                if m and not TOC_LINE.match(line):
                    chapter = m.group(2) + ' ' + m.group(1).strip()
                    continue
                m = TOC_LINE.match(line)
                if m and re.match(r'^[0-9A-Z]{2,3}\.\d{2}[A-Z]$', m.group(2) or ''):
                    title = re.sub(r'\s{2,}', ' ', m.group(1)).strip()
                    entries.append({'title': title, 'code': m.group(2), 'chapter': chapter,
                                    'toc_page': n})
    return entries


def build(book):
    pdf = pdf_path(book)
    st = pdf.stat()
    pages = extract_pages(book)
    metas = [page_meta(book, p) for p in pages]
    if book == 'pdp':  # propagate the module code to the following slides
        current = None
        for m in metas:
            current = m['code'] or current
            m['code'] = current
            m['header'] = PDP_MODULES.get(current, current or '')
    data = {'version': CACHE_VERSION, 'book': book, 'pdf': str(pdf), 'size': st.st_size,
            'mtime': st.st_mtime, 'pages': pages, 'meta': metas}
    data['blocks'] = find_blocks(pages, metas)
    data['toc'] = parse_toc(book, pages, metas)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / f'{book}.json').write_text(json.dumps(data))
    return data


_LOADED = {}


def load(book):
    if book in _LOADED:
        return _LOADED[book]
    path = CACHE_DIR / f'{book}.json'
    st = pdf_path(book).stat()
    data = None
    if path.exists():
        data = json.loads(path.read_text())
        if (data.get('version') != CACHE_VERSION or data['size'] != st.st_size
                or data['mtime'] != st.st_mtime):
            data = None
    if data is None:
        print(f'(indexing {book} ...)', file=sys.stderr)
        data = build(book)
    _LOADED[book] = data
    return data


# ---------------------------------------------------------------- helpers

def locator(book, data, n):
    m = data['meta'][n - 1]
    name = BOOKS[book][1]
    if book == 'qrh':
        loc = f"{name} {m['code'] or '-'}"
    elif book == 'pdp':
        loc = f"PDP {PDP_MODULES.get(m['code'], m['code'])} ({m['code']})"
    else:
        loc = f"{name} {m['code']} P {m['page']}/{m['of']}" if m['code'] else f'{name} (no footer)'
    return f"{loc} | PDF p.{n}" + (f" | rev {m['date']}" if m['date'] else '')


def parse_range(spec, maxpage):
    out = []
    for part in spec.split(','):
        if '-' in part:
            a, b = part.split('-', 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return [p for p in out if 1 <= p <= maxpage]


def norm(s):
    s = s.upper().replace("(CONT'D)", '').replace('(CONT’D)', '')
    s = re.sub(r'\s*\+\s*', '+', s)
    s = re.sub(r'\s*/\s*', '/', s)
    s = re.sub(r'[^A-Z0-9+/()\-. ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def tokens(s):
    return norm(s).replace('/', ' / ').split()


def tok_match(q, c):
    if q == c:
        return True
    m = re.fullmatch(r'(\d)\((\d)\)', c)  # 1(2) matches 1 or 2
    if m and q in (m.group(1), m.group(2)):
        return True
    m = re.fullmatch(r'([A-Z]+)(\d)\((\d)\)', c)  # TR1(2)-style
    if m and q in (m.group(1) + m.group(2), m.group(1) + m.group(3)):
        return True
    return False


def score(query, cand):
    q, c = tokens(query), tokens(cand)
    if not q or not c:
        return 0
    if norm(query) == norm(cand):
        return 100
    if len(q) == len(c) and all(tok_match(a, b) for a, b in zip(q, c)):
        return 98
    # all query tokens appear in order in candidate
    i = 0
    for tok in c:
        if i < len(q) and tok_match(q[i], tok):
            i += 1
    if i == len(q):
        return 90 - min(20, 2 * (len(c) - len(q)))
    r = difflib.SequenceMatcher(None, norm(query), norm(cand)).ratio()
    return int(r * 70)


def blocks_for_title(data, query, threshold=85):
    hits = []
    for b in data['blocks']:
        s = max(score(query, b['title']), score(query, b['parent']) - 5)
        if s >= threshold:
            hits.append((s, b))
    if any(s >= 98 for s, _ in hits):  # exact title exists: ignore looser matches
        hits = [(s, b) for s, b in hits if s >= 95]
    return hits


def group_runs(book, data, hits):
    """Group matching blocks into runs: consecutive blocks (no other block in
    between) with the same effectivity, extended over following pages that
    carry no block of their own but still show the title (continuations)."""
    index = {id(b): k for k, b in enumerate(data['blocks'])}
    hits = sorted(hits, key=lambda h: index[id(h[1])])
    pages_with_blocks = {b['pdf_page'] for b in data['blocks']}
    runs = []
    for s, b in hits:
        k = index[id(b)]
        last = runs[-1] if runs else None
        if (last and b['scope'] == last['scope'] and k == last['k'] + 1
                and norm(b['title']) == norm(last['title'])):
            last.update(end=b['pdf_page'], k=k, score=max(last['score'], s))
        else:
            runs.append({'start': b['pdf_page'], 'end': b['pdf_page'], 'scope': b['scope'],
                         'keep': b['keep'], 'title': b['title'], 'parent': b['parent'],
                         'score': s, 'k': k})
    merged = []
    for r in runs:  # join a procedure with its (Cont'd) runs
        last = merged[-1] if merged else None
        if (last and r['scope'] == last['scope'] and r['start'] <= last['end'] + 1
                and norm(r['title']) == norm(last['title'])):
            last['end'] = max(last['end'], r['end'])
        else:
            merged.append(r)
    runs = merged
    key = norm(runs[0]['title'])[:15] if runs else ''
    for r in runs:
        p = r['end'] + 1
        while (p <= len(data['pages']) and p not in pages_with_blocks
               and key in norm(data['pages'][p - 1]) and p - r['start'] < 40):
            r['end'] = p
            p += 1
    return runs


def pro_abn_section(fcom, code):
    """'PRO-ABN-A-ICE' from 'PRO-ABN-A-ICE', 'PRO-ABN-ABN-00' -> 'PRO-ABN-ABN'."""
    if not code or not code.startswith('PRO-ABN-'):
        return None
    known = {e['section'] for e in fcom['toc']}
    best = max((k for k in known if code == k or code.startswith(k + '-')), key=len, default=None)
    return best or '-'.join(code.split('-')[:3])


# ---------------------------------------------------------------- commands

def cmd_index(_args):
    for book in BOOKS:
        d = load(book)
        print(f"{book}: {len(d['pages'])} pages, {len(d['blocks'])} blocks, "
              f"{len(d['toc'])} TOC entries -> {CACHE_DIR / (book + '.json')}")


def cmd_find(args):
    query = ' '.join(args)
    fcom, fctm, qrh = load('fcom'), load('fctm'), load('qrh')

    print(f'# find: {query!r}\n')
    # FCOM PRO-ABN table of contents -> section
    toc = sorted(((score(query, e['title']), e) for e in fcom['toc']), key=lambda x: -x[0])
    good = [e for s, e in toc if s >= 85] or [e for s, e in toc[:5] if s >= 50]
    print('## FCOM PRO-ABN table of contents matches')
    sections = []
    for e in good[:8]:
        print(f"  - {e['title']}  ->  {e['section']}")
        if e['section'] not in sections:
            sections.append(e['section'])
    if not good:
        print('  (none) — check spelling; nearest:', ', '.join(e['title'] for s, e in toc[:5]))

    exact = [e for s, e in toc if s >= 98] or [e for s, e in toc if s >= 85]
    titles = [query] + [e['title'] for e in exact[:4]]
    if not exact and good:
        titles.append(good[0]['title'])
        print(f"  (no close match; nearest is {good[0]['title']!r} — confirm with the user)")
    print('\n## FCOM procedure blocks (variants by effectivity)')
    hits, seen_ids = [], set()
    for t in titles:
        for s, b in blocks_for_title(fcom, t):
            code = fcom['meta'][b['pdf_page'] - 1]['code']
            if code and code.startswith('PRO-') and id(b) not in seen_ids:
                seen_ids.add(id(b))
                hits.append((s, b))
    for r in sorted(group_runs('fcom', fcom, hits), key=lambda r: r['start']):
        flag = 'KEEP' if r['keep'] else 'DROP'
        a, z = fcom['meta'][r['start'] - 1], fcom['meta'][r['end'] - 1]
        print(f"  [{flag}] {r['title']}  ({r['scope']})  {a['code']} P {a['page']}-{z['page']}/{a['of']}"
              f"  PDF {r['start']}-{r['end']}")
        sec = pro_abn_section(fcom, a['code'])
        if sec and sec.startswith('PRO-ABN') and sec not in sections:
            sections.append(sec)

    print('\n## QRH')
    qtoc = sorted(((score(query, e['title']), e) for e in qrh['toc']), key=lambda x: -x[0])
    for s, e in qtoc:
        if s < 80:
            break
        pages = [n for n, m in enumerate(qrh['meta'], 1)
                 if m['code'] and m['code'][:5] == e['code'][:5]]
        rng = f'PDF {pages[0]}-{pages[-1]}' if pages else ''
        print(f"  - TOC: {e['title']}  {e['code']}  ({e['chapter']})  {rng}")
    qhits = blocks_for_title(qrh, query)
    for r in group_runs('qrh', qrh, qhits):
        flag = 'KEEP' if r['keep'] else 'DROP'
        a, z = qrh['meta'][r['start'] - 1], qrh['meta'][r['end'] - 1]
        name = r['title'] if not r['parent'] else f"{r['parent']} > {r['title']}"
        print(f"  [{flag}] {name}  ({r['scope']})  {a['code']}-{z['code']}  PDF {r['start']}-{r['end']}")

    print('\n## FCTM')
    systems = [s[len('PRO-ABN-'):] for s in sections if s.startswith('PRO-ABN-')]
    for sysname in systems:
        code = 'PR-AEP-' + FCTM_NAME.get(sysname, sysname)
        pages = [n for n, m in enumerate(fctm['meta'], 1) if m['code'] == code]
        if pages:
            print(f'  - {code}: PDF {pages[0]}-{pages[-1]}  (system chapter; read it all)')
    fhits = blocks_for_title(fctm, query, threshold=80)
    for s, b in fhits[:10]:
        m = fctm['meta'][b['pdf_page'] - 1]
        print(f"  - heading: {b['title']}  ({b['scope']})  {m['code']} P {m['page']}  PDF {b['pdf_page']}")
    print('  - always: AOP-20, AOP-30 (see reference/abnormal-operations.md)')

    print('\n## FCOM DSC (system description) suggestions')
    for sysname in systems:
        for ch in DSC_FOR_SYSTEM.get(sysname, []):
            pages = [n for n, m in enumerate(fcom['meta'], 1)
                     if m['code'] and (m['code'] == ch or m['code'].startswith(ch + '-'))]
            if pages:
                hdr = fcom['meta'][pages[-1] - 1]['header']
                print(f'  - {ch}: PDF {pages[0]}-{pages[-1]}  [{hdr[:70]}]  -> `section fcom {ch}`')

    print('\n## PDP tutorials (Airbus technique slides; view with Read)')
    pdp = load('pdp')
    words = {w for w in re.findall(r'[A-Z]{3,}', norm(query)) if w not in ('FAULT', 'FAIL', 'PROC')}
    alias = {'ENG': 'engine', 'ELEC': 'elec', 'HYD': 'hydraulic', 'NAV': 'speed', 'FWS': 'ecam',
             'EVAC': 'evacuation', 'FMGC': 'fmgc', 'FIRE': 'fire', 'RELIGHT': 'flameout'}
    keys = {alias.get(w, w.lower()) for w in words}
    for c, t in PDP_MODULES.items():
        if any(k in t.lower() for k in keys) or c == 'XFTDN6ECAM00001':
            pages = [n for n, m in enumerate(pdp['meta'], 1) if m['code'] == c]
            if pages:
                print(f'  - {t} ({c}): PDF {pages[0]}-{pages[-1]}')
    pat2 = re.compile(re.escape(norm(query)))
    hits = [n for n, text in enumerate(pdp['pages'], 1) if pat2.search(norm(text))]
    if hits:
        print(f"  - slides mentioning {query!r}: PDF {', '.join(map(str, hits[:15]))}")

    print('\n## Other pages mentioning the title (by section; for cross-checks)')
    mention = titles[1] if len(titles) > 1 else query
    print(f'  (searching for {mention!r})')
    pat = re.compile(r'(?<![A-Z0-9])' + r'\s*'.join(re.escape(t) for t in norm(mention).split())
                     + r'(?![A-Z0-9])')
    for book, d in (('fcom', fcom), ('fctm', fctm), ('qrh', qrh)):
        by = {}
        for n, (text, m) in enumerate(zip(d['pages'], d['meta']), 1):
            if pat.search(norm(text)):
                if book == 'qrh':
                    key = (m['code'] or '?').split('.')[0]
                else:
                    key = '-'.join((m['code'] or '?').split('-')[:3])
                by.setdefault(key, []).append(n)
        if by:
            items = sorted(by.items(), key=lambda kv: kv[1][0])
            print(f'  {BOOKS[book][1]}: ' + '; '.join(
                f"{k} [PDF {','.join(map(str, v[:6]))}{'…' if len(v) > 6 else ''}]" for k, v in items[:25]))


def cmd_show(args):
    if len(args) < 2:
        sys.exit('usage: show <book> <pdf-pages> [--all-fleets]')
    book, spec = args[0], args[1]
    all_fleets = '--all-fleets' in args
    d = load(book)
    by_page = {}
    for b in d['blocks']:
        by_page.setdefault(b['pdf_page'], []).append(b)
    # block in force at start of each page = last block of earlier pages
    pages = parse_range(spec, len(d['pages']))
    prior = None
    if pages:
        for b in d['blocks']:
            if b['pdf_page'] < pages[0]:
                prior = b
            else:
                break
    for n in pages:
        meta = d['meta'][n - 1]
        lines = d['pages'][n - 1].splitlines()
        print(f"\n===== {locator(book, d, n)} =====")
        if meta['header']:
            print(f"      [{meta['header'][:150]}]")
        starts = {b['line']: b for b in by_page.get(n, [])}
        current = prior if (prior and prior['pdf_page'] != n) else None
        if current and not current['keep'] and not all_fleets:
            pass
        dropped = 0
        for i in range(meta['body_start'], meta['body_end']):
            if i in starts:
                if dropped:
                    print(f'      [... {dropped} lines omitted: HS-TO only ...]')
                    dropped = 0
                current = starts[i]
                flag = 'KEEP' if current['keep'] else 'DROP'
                inh = ' (inherited)' if current['inherited'] else ''
                print(f"  [[ {flag} | {current['title'] or '?'} | Ident {current['ident']}"
                      f" / {current['date']} | {current['scope']}{inh} ]]")
            if current and not current['keep'] and not all_fleets:
                if lines[i].strip():
                    dropped += 1
                continue
            if lines[i].strip():
                print(lines[i].rstrip())
        if dropped:
            print(f'      [... {dropped} lines omitted: HS-TO only ...]')
        if by_page.get(n):
            prior = by_page[n][-1]


def cmd_section(args):
    if len(args) < 2:
        sys.exit('usage: section <book> <code>')
    book, code = args[0], args[1]
    d = load(book)
    if book == 'qrh':
        pages = [n for n, m in enumerate(d['meta'], 1) if m['code'] and m['code'].startswith(code)]
    elif book == 'pdp':
        want = ' '.join(args[1:]).lower()
        codes = [c for c, t in PDP_MODULES.items() if c == args[1] or want in t.lower()]
        pages = [n for n, m in enumerate(d['meta'], 1) if m['code'] in codes]
        if pages:
            print(f'# PDP {", ".join(PDP_MODULES[c] + " (" + c + ")" for c in codes)}: PDF {pages[0]}-{pages[-1]}')
            print('Slides are graphical: view them with Read (pages=...) — the PDF is under 100 MB.')
            return
    else:
        pages = [n for n, m in enumerate(d['meta'], 1)
                 if m['code'] and (m['code'] == code or m['code'].startswith(code + '-')
                                   or m['code'].startswith(code + '_'))]
    if not pages:
        sys.exit(f'no pages with code {code}')
    print(f'# {BOOKS[book][1]} {code}: {len(pages)} pages, PDF {pages[0]}-{pages[-1]}')
    last_code = None
    seen = set()
    for b in d['blocks']:
        if b['pdf_page'] not in pages:
            continue
        m = d['meta'][b['pdf_page'] - 1]
        if m['code'] != last_code:
            print(f"\n## {m['code']}  [{m['header'][:100]}]")
            last_code = m['code']
        key = (norm(b['title']), b['scope'])
        if key in seen:
            continue
        seen.add(key)
        flag = '' if b['keep'] else '  DROP'
        pg = f"P {m['page']}" if m['page'] else m['code']
        title = b['title'] if not b['parent'] else f"{b['parent']} > {b['title']}"
        print(f"  - {title[:90]}  ({b['scope']}){flag}  {pg}  PDF {b['pdf_page']}")


def cmd_grep(args):
    if len(args) < 2:
        sys.exit('usage: grep <book|all> <regex>')
    books = list(BOOKS) if args[0] == 'all' else [args[0]]
    rx = re.compile(' '.join(args[1:]), re.I)
    for book in books:
        d = load(book)
        for n, text in enumerate(d['pages'], 1):
            ms = [l.strip() for l in text.splitlines() if rx.search(l)]
            if ms:
                print(f"{locator(book, d, n)}:  " + ' || '.join(x[:110] for x in ms[:3]))


REF_RX = re.compile(r'(Refer to [^\n]+|\[QRH\][^\n]+|\[MEM\][^\n]+|PROC\s*:[^\n]+|\bAPPLY\b[^\n]*PROC[^\n]*|'
                    r'^\s*[A-Z0-9 /+()\-]{4,}PROC[^\n]*\.{3,}[^\n]*)', re.M)


def cmd_refs(args):
    if len(args) < 2:
        sys.exit('usage: refs <book> <pdf-pages>')
    book, spec = args[0], args[1]
    d = load(book)
    seen = set()
    for n in parse_range(spec, len(d['pages'])):
        lines = d['pages'][n - 1].splitlines()
        for i, line in enumerate(lines):
            m = REF_RX.search(line)
            if not m:
                continue
            txt = line.strip()
            # join a wrapped continuation line
            nxt = next((l.strip() for l in lines[i + 1:i + 4] if l.strip()), '')
            if txt.count('(') > txt.count(')') or txt.endswith(('[QRH]', 'Refer to')):
                txt += ' ' + nxt
            key = re.sub(r'\.{3,}', '...', re.sub(r'\s+', ' ', txt))
            if key in seen:
                continue
            seen.add(key)
            print(f'{locator(book, d, n)}:  {key}')


def cmd_render(args):
    """Render pages to PNG (the Read tool cannot open PDFs over 100 MB, e.g. the FCOM)."""
    if len(args) < 2:
        sys.exit('usage: render <book> <pdf-pages> [--dpi N]')
    book, spec = args[0], args[1]
    dpi = int(args[args.index('--dpi') + 1]) if '--dpi' in args else 110
    out = CACHE_DIR / 'render'
    out.mkdir(parents=True, exist_ok=True)
    d = load(book)
    for n in parse_range(spec, len(d['pages'])):
        target = out / f'{book}-{n}-{dpi}.png'
        if not target.exists():
            stem = out / f'{book}-{n}-{dpi}'
            subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', str(dpi), '-png',
                            '-singlefile', str(pdf_path(book)), str(stem)], check=True)
        print(f'{target}   ({locator(book, d, n)})')


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return
    cmd, args = sys.argv[1], sys.argv[2:]
    {'index': cmd_index, 'find': cmd_find, 'show': cmd_show, 'section': cmd_section,
     'grep': cmd_grep, 'refs': cmd_refs, 'render': cmd_render}[cmd](args)


if __name__ == '__main__':
    main()
