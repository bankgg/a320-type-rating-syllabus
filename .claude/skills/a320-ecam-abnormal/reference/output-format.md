# Output format (schema `a320-ecam-abnormal/3`)

The JSON file is the source of truth; the Markdown is rendered from it.

1. Write `abnormals/<slug>.json` at the repository root (schema below) — easiest with `scripts/brief_kit.py`, whose `write()` also runs step 2.
2. Validate and render: `python3 -I .claude/skills/a320-ecam-abnormal/scripts/render_md.py abnormals/<slug>.json` — it checks the schema, then writes `abnormals/<slug>.md`.
3. Print the Markdown in chat when the user asked for the plan itself; when the brief feeds another task (e.g. the syllabus webpage), summarise instead.

`<slug>` = title in lowercase, non-alphanumerics → `-` (e.g. `ENG 1(2) FIRE (IN FLIGHT)` → `eng-1-2-fire-in-flight`). Read an existing file before overwriting it.

The syllabus webpage (`build_comparison.py`) renders these files directly, so every field below has a visible home: keep text short, verbatim where the source is verbatim, and cited.

## Shared shapes

- `REF` = `{"book": "FCOM|FCTM|QRH|PDP", "code": "PRO-ABN-ELEC", "page": "P 91/122" | "18.01A", "pdf": 3216}` — for the PDP, `code` is the tutorial module title and `page` its footer code (`{"book": "PDP", "code": "Engine failure after V1", "page": "XFTDA10ENGFTO01", "pdf": 500}`)
- `APPLIES` = `["all"]` or branch labels from `effectivity.branches` (e.g. `["HS-TXP..TXU"]`)
- `TEXT` = `{"text": "...", "applies_to": APPLIES, "refs": [REF]}`
- `LINE` (procedure line) = `{"kind": "action|condition|info|caution|note|land_asap", "item": "GEN 1 + 2", "setting": "OFF THEN ON", "text": "...", "level": 0, "applies_to": APPLIES, "refs": [REF]}`
  - `action`: `item` + `setting` (verbatim ECAM/QRH line). `condition`: `text` such as "IF UNSUCCESSFUL:". Lines that depend on a condition get `level` + 1 (indentation as printed). `info`/`note`/`caution`: `text`.
- `FLOW ITEM` = `{"kind": "callout|action|ecam|condition|note", "text": "...", "item": "...", "setting": "...", "children": [FLOW ITEM], "applies_to": APPLIES, "refs": [REF]}`
  - `callout`: exact spoken words in `text` (no quotes). `ecam`: `item`/`setting` read from ECAM/QRH. `action`: a physical action or technique in plain words. `condition`: `text` + `children`.

## Top level

```json
{
  "schema": "a320-ecam-abnormal/3",
  "slug": "elec-emer-config",
  "title": "ELEC EMER CONFIG",
  "generated": "YYYY-MM-DD",
  "kind": "ecam | qrh | technique",
  "alert": {"level": "warning | caution | qrh | memory | technique", "land_asap": "red | amber | none",
            "memory_items": false, "qrh_summary": true,
            "trigger": "TEXT-like string", "inhibited_phases": [4, 8], "refs": [REF]},
  "effectivity": {"branches": ["HS-TXA..TXO", "HS-TXP..TXU"], "note": "..."},
  "summary": "Two or three plain sentences: what fails, what the crew does, what matters most.",
  "key_limits": [{"label": "MIN RAT SPEED", "value": "140 kt", "applies_to": APPLIES, "refs": [REF]}],
  "flow": [{"phase": "ECAM actions", "steps": [{"actor": "PF | PM | BOTH", "items": [FLOW ITEM]}]}],
  "procedures": [{"title": "ECAM procedure", "source": "FCOM PRO-ABN-ELEC", "lines": [LINE]}],
  "status": {"limitations": [TEXT], "info": [TEXT], "appr_proc": [LINE], "inop_sys": [TEXT]} | null,
  "qrh": [{"title": "ELEC EMER CONFIG SUMMARY", "sections": [{"name": "CRUISE", "lines": [TEXT]}]}],
  "tables": [{"title": "...", "caption": "...", "columns": ["FL", "..."], "rows": [["310", "..."]],
              "applies_to": APPLIES, "refs": [REF]}],
  "background": [TEXT],
  "technique": [TEXT],
  "related": [{"title": "...", "why": "...", "key_actions": ["..."], "refs": [REF]}],
  "differences": [{"topic": "...", "values": {"HS-TXA..TXO": "...", "HS-TXP..TXU": "..."}, "refs": [REF]}],
  "gaps": [TEXT],
  "sources": [{"book": "FCOM", "section": "PRO-ABN-ELEC", "pages": "P 90–98/122", "pdf": "3215–3223", "rev": "26 MAY 26"}]
}
```

### Field rules
- **alert.level** — `warning` (red ECAM), `caution` (amber ECAM), `qrh` (QRH/paper procedure without ECAM), `memory` (procedure starting with memory items), `technique` (FCTM/PDP technique with no ECAM or QRH procedure, e.g. the engine-out drift-down strategy). `inhibited_phases` from the FCOM chart (empty if none).
- **key_limits** — 3–6 numbers or limits a pilot must hold (speeds, pressures, times, flap setting). Values only from STATUS/procedure/QRH lines.
- **flow** — the phase-by-phase plan. Phases follow the real sequence (e.g. Detection → ECAM actions → Acceleration → Continue ECAM → STATUS → Approach). Inside a phase, `steps` are **turns in time order**: each turn is one crewmember's consecutive actions (`actor` PF, PM, or BOTH for shared items). A new turn starts whenever the other pilot acts or answers, so exchanges read in order — PM “ENGINE MASTER 1 OFF — CONFIRM?” → PF “CONFIRMED” → PM acts; PF “CONTINUE ECAM” → PM reads STATUS → PM “REMOVE STATUS?” → PF “REMOVE STATUS”. Use the PDP slide rows and the AOP-30-30 table for the order; the FCTM or procedure may assign CAPT/F/O — say so in the item text. Conditions wrap the items they govern (`children`). The page numbers turns as phase.turn (3.2). Whenever the flow reaches STATUS, the turns must be exactly `brief_kit.status_turns(system)` (PM "STATUS" → PF "STOP ECAM" → PM ECAM ACTIONS STOP → PF "CONTINUE ECAM" → PM "REMOVE STATUS ?" → PF "REMOVE STATUS" → PM "ECAM ACTIONS COMPLETE"); `render_md.py` enforces it.
- **procedures** — the verbatim ECAM/QRH procedure(s), in order, with `level` reproducing indentation. Several procedures are allowed (e.g. ENG FAIL then ENG SHUT DOWN).
- **status** — `null` for procedures without a STATUS page.
- **tables** — numeric reference tables worth seeing side by side (pitch/thrust, severe-turbulence N1, relight envelope description). Copy values exactly; never interpolate.
- **background / technique / related / differences / gaps** — as in the Markdown sections below; `differences` empty when every HS-TX registration is identical.

## Rendered Markdown (by `render_md.py`)
Header and disclaimer · 1 What it is · 2 Key limits · 3 Flow (PF / PM by phase) · 4 Procedure(s) · 5 STATUS · 6 QRH and tables · 7 FCTM technique · 8 Related procedures · 9 HS-TX differences · 10 Gaps and omissions · Sources.
