"""Authoring helpers for abnormals/<slug>.json briefs (schema a320-ecam-abnormal/3).

Write a small script (in the session scratchpad) that imports this module,
builds one dict per brief and calls write(). Example:

    import sys; sys.path.insert(0, '.claude/skills/a320-ecam-abnormal/scripts')
    from brief_kit import *
    p91 = R('FCOM', 'PRO-ABN-ELEC', 'P 91/122', 3216)
    write({
      'slug': 'elec-emer-config', 'title': 'ELEC EMER CONFIG', 'kind': 'ecam',
      'alert': {...}, 'effectivity': {...}, 'summary': '...', 'key_limits': [K(...)],
      'flow': [
        phase('ECAM actions',
              PF(say('ECAM ACTIONS', [CALLS, PDP_ECAM])),
              PM(ecam('GEN 1 + 2', 'OFF THEN ON', [p91]),
                 when('IF UNSUCCESSFUL', [ecam('BUS TIE', 'OFF', [p91])], [p91]))),
        phase('STATUS', *status_turns('ELEC')),
      ],
      'procedures': [...], 'status': {...} or None, 'qrh': [], 'tables': [],
      'background': [T(...)], 'technique': [], 'related': [], 'differences': [],
      'gaps': [], 'sources': [S(...)],
    })

Flow = phases of TURNS in time order. A new turn starts whenever the other
pilot acts or answers (PM "CONFIRM?" -> PF "CONFIRMED" -> PM acts).
Existing briefs: edit abnormals/<slug>.json directly, then run render_md.py.
"""
import json
import subprocess
from datetime import date
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
REPO = SKILL.parent.parent.parent
OUT = REPO / 'abnormals'
RENDER = SKILL / 'scripts' / 'render_md.py'
SCHEMA = 'a320-ecam-abnormal/3'


# ------------------------------------------------------------------ references
def R(book, code, page, pdf):
    """FCOM/FCTM: R('FCOM', 'PRO-ABN-ELEC', 'P 91/122', 3216); QRH: R('QRH', '18.01', '18.01A', 152)."""
    return {'book': book, 'code': code, 'page': page, 'pdf': pdf}


def P(module, code, pdf):
    """Airbus PDP tutorial slide: P('Engine failure after V1', 'XFTDA10ENGFTO01', 500)."""
    return R('PDP', module, code, pdf)


def S(book, section, pages, pdf, rev=''):
    """Sources table row."""
    return {'book': book, 'section': section, 'pages': pages, 'pdf': pdf, 'rev': rev}


def _ap(applies):
    return list(applies) if applies else ['all']


# ------------------------------------------------------------- simple entries
def T(text, refs, applies=None):
    return {'text': text, 'applies_to': _ap(applies), 'refs': refs}


def K(label, value, refs, applies=None):
    return {'label': label, 'value': value, 'applies_to': _ap(applies), 'refs': refs}


# ------------------------------------------------- verbatim procedure lines
def act(item, setting, refs, level=0, text='', applies=None):
    return {'kind': 'action', 'item': item, 'setting': setting, 'text': text, 'level': level,
            'applies_to': _ap(applies), 'refs': refs}


def cond(text, refs, level=0, applies=None):
    return {'kind': 'condition', 'text': text, 'level': level, 'applies_to': _ap(applies), 'refs': refs}


def info(text, refs, level=0, applies=None, kind='info'):
    return {'kind': kind, 'text': text, 'level': level, 'applies_to': _ap(applies), 'refs': refs}


def caution(text, refs, level=0, applies=None):
    return info(text, refs, level, applies, kind='caution')


def note(text, refs, level=0, applies=None):
    return info(text, refs, level, applies, kind='note')


def land_asap(colour, refs):
    return info(f'LAND ASAP ({colour})', refs, kind='land_asap')


# ------------------------------------------------------------- flow items
def say(text, refs, applies=None):
    """Exact spoken words (no quotes)."""
    return {'kind': 'callout', 'text': text, 'applies_to': _ap(applies), 'refs': refs}


def do(text, refs, applies=None):
    return {'kind': 'action', 'text': text, 'applies_to': _ap(applies), 'refs': refs}


def ecam(item, setting, refs, applies=None):
    return {'kind': 'ecam', 'item': item, 'setting': setting, 'applies_to': _ap(applies), 'refs': refs}


def when(text, children, refs, applies=None):
    return {'kind': 'condition', 'text': text, 'children': children, 'applies_to': _ap(applies), 'refs': refs}


def fnote(text, refs, applies=None):
    return {'kind': 'note', 'text': text, 'applies_to': _ap(applies), 'refs': refs}


# ------------------------------------------------------------- turns/phases
def turn(actor, *items):
    assert actor in ('PF', 'PM', 'BOTH'), actor
    return {'actor': actor, 'items': list(items)}


def PF(*items):
    return turn('PF', *items)


def PM(*items):
    return turn('PM', *items)


def BOTH(*items):
    return turn('BOTH', *items)


def phase(name, *turns):
    steps = [t for t in turns if t and t['items']]
    assert steps, f'phase {name!r} has no turns'
    return {'phase': name, 'steps': steps}


# ------------------------------------------------------ shared source refs
AOP20 = R('FCTM', 'AOP-20', 'P 1–2/10', 68)
AOP3010 = R('FCTM', 'AOP-30-10', 'P 2/2', 79)
AOP3020 = R('FCTM', 'AOP-30-20', 'P 1/2', 80)
AOP3030a = R('FCTM', 'AOP-30-30', 'P 1/6', 82)
AOP3030b = R('FCTM', 'AOP-30-30', 'P 2/6', 83)
AOP3030c = R('FCTM', 'AOP-30-30', 'P 3/6', 84)
AOP3030d = R('FCTM', 'AOP-30-30', 'P 4/6', 85)
AOP3030e = R('FCTM', 'AOP-30-30', 'P 5/6', 86)
CALLS = R('FCOM', 'PRO-ABN-ABN-00', 'P 8/12', 2831)
PDP_ECAM = P('Management of abnormal operations', 'XFTDN6ECAM00001', 424)
PDP_STATUS = P('Management of abnormal operations', 'XFTDN6ECAM00001', 426)
PDP_QRH = P('Management of abnormal operations', 'XFTDN6ECAM00001', 427)
PDP_DONE = P('Management of abnormal operations', 'XFTDN6ECAM00001', 428)
PDP_STOP = P('Management of abnormal operations', 'XFTDN6ECAM00001', 430)
PDP_QRH_FROM_ECAM = P('Management of abnormal operations', 'XFTDN6ECAM00001', 431)
PDP_CONFIRM = P('Management of abnormal operations', 'XFTDN6ECAM00001', 432)


# ------------------------------------------------------- standard sequences
def ecam_start_turns(title, title_ref):
    """Detection → ECAM order (FCTM AOP-30-30 / PDP 423-424)."""
    return [BOTH(do('First to notice: MASTER WARNING / CAUTION reset', [AOP3030b, PDP_ECAM])),
            PM(say(title, [AOP3030b, title_ref, PDP_ECAM]),
               do('Confirm the failure on the SD page and overhead panel before acting', [AOP3030b, PDP_ECAM])),
            PF(say('ECAM ACTIONS', [CALLS, AOP3030c, PDP_ECAM]),
               fnote('PF now flies, navigates and communicates', [AOP20, PDP_ECAM]))]


def status_turns(system, extra_pause=()):
    """Clear the alert, then the STATUS sequence (FCTM AOP-30-30 table / PDP 424-426).
    `extra_pause` = flow items for the STOP ECAM pause (acceleration flow, relight, ...)."""
    pause = [do('Normal C/L as applicable; system resets only per QRH', [AOP3030d, PDP_STATUS])] + list(extra_pause)
    return [PM(say(f'CLEAR {system} ?', [CALLS, AOP3030c, PDP_ECAM])),
            PF(say(f'CLEAR {system}', [CALLS, AOP3030c, PDP_ECAM])),
            PM(say('STATUS', [AOP3030c, PDP_STATUS])),
            PF(say('STOP ECAM', [AOP3030c, PDP_STATUS])),
            PM(ecam('ECAM ACTIONS', 'STOP', [PDP_STATUS])),
            PF(*pause, say('CONTINUE ECAM', [AOP3030c, PDP_STATUS])),
            PM(do('Read the whole STATUS page; preview APPR PROC workload', [AOP3030c, PDP_STATUS]),
               say('REMOVE STATUS ?', [AOP3030c, PDP_STATUS])),
            PF(say('REMOVE STATUS', [CALLS, AOP3030c, PDP_STATUS])),
            PM(say('ECAM ACTIONS COMPLETE', [CALLS, PDP_STATUS]))]


def confirm_turns(read_back, refs):
    """In-flight crosscheck of a guarded control / ENG MASTER / C/B (PDP 432, FCTM AOP-30-20).
    `read_back` is the line the PM reads; only PDP-given words are quoted (e.g. 'ENGINE MASTER 1 OFF')."""
    return [PM(say(f'{read_back} — CONFIRM?' if read_back else 'CONFIRM?', [PDP_CONFIRM] + refs)),
            PF(say('CONFIRMED', [PDP_CONFIRM]), fnote('After verifying the control the PM points to', [PDP_CONFIRM, AOP3020]))]


def qrh_order_turns(name):
    """QRH procedure ordered by the PF (PDP 427)."""
    return [PF(say(f'{name} PROCEDURE', [PDP_QRH])), PM(do('READ AND DO the QRH lines aloud', [PDP_QRH]))]


# -------------------------------------------------------------------- write
def write(d, render=True):
    """Fill schema/date, save abnormals/<slug>.json, validate and render the Markdown."""
    d.setdefault('schema', SCHEMA)
    d.setdefault('generated', date.today().isoformat())
    for key in ('qrh', 'tables', 'technique', 'related', 'differences', 'gaps'):
        d.setdefault(key, [])
    OUT.mkdir(exist_ok=True)
    path = OUT / f"{d['slug']}.json"
    path.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if render:
        subprocess.run(['python3', '-I', str(RENDER), str(path)], check=True)
    return path
