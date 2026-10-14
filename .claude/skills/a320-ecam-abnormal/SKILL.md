---
name: a320-ecam-abnormal
description: Build a detailed, source-cited handling plan (brief) for an A320 ECAM alert or abnormal/emergency procedure from the FCOM, FCTM, QRH and Airbus PDP tutorial PDFs in books/, filtered to HS-TX registrations, saved as abnormals/<slug>.json + .md. Use whenever the user's prompt is (or contains) an A320 ECAM alert or abnormal title such as "ELEC EMER CONFIG", "ENG 1 FIRE", "HYD G+Y SYS LO PR", "F/CTL ALTN LAW", "CAB PR EXCESS CAB ALT", asks how to handle / brief / study an A320 abnormal, or when another task (e.g. the syllabus-session-briefs skill adding failure procedures to the webpage) needs a brief.
---

# A320 ECAM abnormal → handling brief

Turn an ECAM alert (or QRH / memory-item procedure) title into a complete, cited plan for handling it, for **HS-TX** aircraft, built **only** from the four documents in `books/`:

| Key | Document | Authority |
|---|---|---|
| `fcom` | THA FCOM (14 JUL 26) | Procedures, limits, system description — authoritative |
| `qrh` | THA QRH (14 JUL 26) | Paper procedures, summaries, reset table, tables — authoritative |
| `fctm` | THA FCTM (14 JUL 26) | Techniques and task sharing — authoritative for technique |
| `pdp` | Airbus *Tutorials (UPRT included) / Flow Patterns / Cockpit Panels* (Jan 2024) | Slide deck: PF/PM task sharing, callouts, phase sequence, flow patterns. Generic A320/A330 — A320 content only; never takes priority over FCOM/QRH for actions, settings or limits |

The brief is saved as `abnormals/<slug>.json` (source of truth, schema `a320-ecam-abnormal/3`) plus rendered `abnormals/<slug>.md`. The syllabus webpage renders the JSON directly (see the `syllabus-session-briefs` skill). This skill does not edit the webpage.

Run every command from the repository root:

```sh
M=".claude/skills/a320-ecam-abnormal/scripts/manuals.py"
python3 -I $M find "<ECAM TITLE>"
```

`manuals.py` needs `pdftotext`/`pdftoppm` (poppler). The first call indexes the PDFs into `cache/` (~10 s).

## Before starting
- **Reuse.** `ls abnormals/` — briefs are shared between syllabus sessions (one JSON = one identical pop-up everywhere). If the same procedure and case already has a brief, reuse it unchanged. Edit it only for corrections true for every session that uses it (`grep -n "<slug>" build_comparison.py` lists them). For an extra case a session trains (e.g. drift-down after an engine fire in cruise), write a separate companion brief instead of extending the shared one.
- Read [reference/abnormal-operations.md](reference/abnormal-operations.md) every time: FCTM/FCOM/PDP task sharing and callouts, plus the **company (THAI) phraseology** that overrides generic wording.

## Non-negotiable rules
1. **Books only.** Every operational fact (action, setting, limit, speed, callout, role, technique) comes from `books/` and carries a locator: `[FCOM PRO-ABN-ELEC P 91/122, PDF 3216]`, `[QRH 18.01A, PDF 152]`, `[FCTM PR-AEP-ELEC P 1/2, PDF 400]`, `[PDP Engine failure after V1, PDF 500]`. No memory or general A320 knowledge — write "not found in the supplied manuals" under Gaps instead. Never invent callout wording: quote only words a source (or the company phraseology list) gives; otherwise describe the action.
2. **HS-TX only.** `manuals.py show` marks each block KEEP/DROP. Never use DROP (HS-TO-only) content; list its locators under Gaps. `ALL` and lists containing an HS-TX registration are kept.
3. **HS-TX splits.** When HS-TX registrations differ (e.g. HS-TXA..TXO vs HS-TXP..TXU), one brief: common content once, differing content as labelled branches (`applies_to`), plus the `differences` table. Use the exact ranges each source gives — related procedures may split differently. `differences` stays empty when nothing differs (the page then hides that section).
4. **Verbatim where it matters.** ECAM/QRH lines, STATUS lines, summary lines and callouts are quoted exactly; your synthesis (phase plan, who does what) stays visibly separate and still cites each fact.
5. **Flow = turns in time order.** Each phase is a sequence of turns (one pilot's consecutive actions). Start a new turn whenever the other pilot acts or answers, so exchanges read in order (PM "ENGINE MASTER 1 OFF — CONFIRM?" → PF "CONFIRMED" → PM acts; PF "CONTINUE ECAM" → PM reads STATUS → PM "REMOVE STATUS ?" → PF "REMOVE STATUS"). Take the order from the PDP slide rows and the FCTM AOP-30-30 table; keep STOP ECAM / CONTINUE ECAM at their real points (e.g. engine failure after V1: STOP ECAM once the engine is secured, before EO ACC ALT; CONTINUE ECAM after MCT; STOP ECAM again at STATUS). **Every ECAM procedure that reaches STATUS uses the full exchange — build it with `brief_kit.status_turns`, never by hand:** PM "STATUS" → PF "STOP ECAM" → PM ECAM ACTIONS STOP → PF considers the acceleration flow, normal C/L, resets, additional procedures → PF "CONTINUE ECAM" → PM reads STATUS → "REMOVE STATUS ?" → PF "REMOVE STATUS" → PM "ECAM ACTIONS COMPLETE" (FCTM AOP-30-30 P 3/6, PDP PDF 426). Brief-specific STATUS content goes in the PM read turn. `render_md.py` rejects a partial exchange, and an ECAM brief with a STATUS section that never reaches it unless its procedure says STATUS is NOT AVAIL (FWC 1 + 2 FAULT).
6. **PDP is a presentation.** Its extracted text is scrambled: use `find` / `grep pdp` / `section pdp <words>` only to locate slides, then **view every slide you cite** with `Read` (`books/Airbus Tutorial PDP Jan 2024.pdf`, `pages`, ≤20 per call). If PDP and FCOM/FCTM differ, follow FCOM/FCTM and record the difference under Gaps.
7. **Look at graphics.** Extracted text loses layout (flight-phase inhibition charts, indentation under "IF …", STATUS columns, SYS REMAINING and pitch/thrust tables, diagrams). View them: FCOM is over the Read tool's 100 MB limit → `python3 -I $M render fcom <pages>` then `Read` the PNGs; QRH / FCTM / PDP → `Read` the PDF with `pages`. Always view the FCOM procedure pages themselves — indentation decides which actions are conditional; the title colour gives the alert level (red warning / amber caution).
8. **Surface conflicts.** Quote both sides with locators when sources disagree; never silently pick one. Company phraseology substitutions are listed under Gaps too.
9. **Resets follow QRH 02.01A.** Show a reset only when the procedure requests it or the QRH reset table lists *that exact alert* — a single-unit entry such as "FWS FWC 1(2) FAULT" does not cover the dual failure (covered dual cases are named, e.g. "NAV FLS 1(2) (1+2) FAULT"). Otherwise state RESET NOT AUTHORIZED in flight (and the on-ground rule), even if the syllabus says "and reset"; put the other alert's reset under `related`, never in the flow.
10. **Session-neutral.** A brief describes the procedure, not a syllabus scenario: never name a session (MFTD/FFS), an exercise number or a training scenario in any field. Write conditional cases as procedure conditions; scenario context belongs in the session note in `build_comparison.py` (see the `syllabus-session-briefs` skill). The page build rejects briefs that name a session.

## Workflow
1. **Resolve** — `find "<title>"`: FCOM PRO-ABN table-of-contents matches, FCOM procedure variants with effectivity (KEEP/DROP), QRH entries, FCTM chapter, DSC chapter suggestions, PDP tutorial modules, other mentions. Titles match loosely (`ENG 1 FIRE` → `ENG 1(2) FIRE (IN FLIGHT)` / `(ON GROUND)`). Ask one short question only if several different procedures fit and intent is unclear; confirm fuzzy matches. Some syllabus items have no ECAM procedure (e.g. FMGC faults → FCTM technique + DSC + QRH reset table): build the brief from those and say so under Gaps.
2. **FCOM procedure** — `show fcom <pages>` for every KEEP variant, then `render` and view them. Diff HS-TX variants (usually only STATUS/footnotes differ). Capture annunciations (trigger, inhibited phases from the chart), procedure (LAND ASAP colour, conditions, actions, layer-2 notes, cautions), STATUS (limitations, APPR PROC, INOP SYS, footnotes) and associated procedures.
3. **QRH** — `show qrh <pages>` (or `section qrh <chapter>`): QRH procedure, summary, SYS REMAINING, reset table (02.xx), OPS tables. View tables with `Read`.
4. **FCTM + PDP** — read the FCTM system chapter (`section fctm PR-AEP-<SYS>`) and any other headings `find` lists; view the PDP module slides and take the PF/PM sequence and callouts from them.
5. **System description** — `section fcom DSC-xx`, then `show` only the subsections that explain the failure and the controls the crew uses.
6. **References one level deep** — `refs fcom <pages>` lists "Refer to …" / `[QRH]` / `PROC:` lines; summarise each procedure the crew must apply or consider (HS-TX variant, cited) under `related`. Don't recurse further.
7. **Write** — author with the helper library [scripts/brief_kit.py](scripts/brief_kit.py) (refs `R`/`P`, entries `T`/`K`, verbatim lines `act`/`cond`/`note`/`caution`/`land_asap`, flow items `say`/`do`/`ecam`/`when`/`fnote`, turns `PF`/`PM`/`BOTH`, `phase`, and standard sequences `ecam_start_turns`, `status_turns`, `confirm_turns`, `qrh_order_turns`) in a scratchpad script, then `write(brief)`. It saves the JSON and runs `render_md.py`, which validates the schema and writes the Markdown. Edit existing briefs in their JSON directly, then run `python3 -I .claude/skills/a320-ecam-abnormal/scripts/render_md.py abnormals/<slug>.json`. Field rules: [reference/output-format.md](reference/output-format.md).
8. **Self-check** — re-open each cited page and compare every ECAM line, limit and number; confirm no DROP content leaked; read the flow top to bottom and confirm the turn order matches the PDP / AOP-30-30 sequence; confirm company phraseology is applied; confirm every section is present or marked "Not covered by the supplied manuals".

Print the Markdown in chat when the user asked for the brief itself; when it feeds another task, summarise and list open gaps.

## Reference files
- [reference/abnormal-operations.md](reference/abnormal-operations.md) — FCTM AOP-20/30/40, FCOM PRO-ABN-ABN-00, PDP task sharing and callouts, company phraseology (always load).
- [reference/source-map.md](reference/source-map.md) — editions, locator formats, effectivity groups, system → FCOM/FCTM/DSC/QRH chapter map, PDP module page ranges.
- [reference/output-format.md](reference/output-format.md) — JSON schema v3 and the rendered Markdown layout.

## `manuals.py` commands
| Command | Purpose |
|---|---|
| `index` | Build/refresh the cache (automatic on first use or when a PDF changes) |
| `find "<title>"` | Locate the alert in all four documents |
| `show <book> <pages> [--all-fleets]` | Pages with locator lines and KEEP/DROP banners (HS-TO-only text omitted unless `--all-fleets`) |
| `section <book> <code or words>` | Page range + headings for a code (`PR-AEP-ELEC`, `DSC-24`, `AOP-30`, QRH `18`); PDP by module words (`section pdp rejected`) |
| `refs <book> <pages>` | Cross-references on those pages |
| `render <book> <pages> [--dpi N]` | PNG per page in `cache/render/` for `Read` (needed for the FCOM) |
| `grep <book\|all> <regex>` | Pages whose lines match a regex |

`<book>` is `fcom`, `fctm`, `qrh` or `pdp`; `<pages>` are physical PDF pages, e.g. `3215-3222` or `152,154`.
