# A320 SIM session PDF authoring

These are the complete project instructions for a new agent creating or revising a session in this directory. Use the supplied syllabus and manuals; do not rely on earlier chat context.

## Request, filenames, and output

1. Take the requested session and any optional user/instructor notes. Find the session's `<article class="session" id="...">` in `sources/A320_Trainee_A_vs_B_Syllabus_Comparison.html`. Normalize “MFTD/FBS N” to the HTML ID `mftd-N`, and “FFS N” to `ffs-N`. Use the HTML heading as `session.title`. Confirm the ID exists; do not infer it from the session's ordinal number.
2. Use the exact filename convention below. Keep `session.id` in the YAML equal to the hyphenated HTML ID. The builder derives the PDF name from that ID.

   | Request | `session.id` | YAML | PDF |
   | --- | --- | --- | --- |
   | MFTD/FBS 4 | `mftd-4` | `data/mftd_4.yaml` | `output/mftd-4_practice.pdf` |
   | FFS 1 | `ffs-1` | `data/ffs_1.yaml` | `output/ffs-1_practice.pdf` |

3. Deliver a reviewed YAML audit and its A4 PDF. If nothing qualifies under the scope below, save the YAML with `scenarios: []`, account for all IDs in `excluded_items`, run the builder, and report that it skipped the PDF. Do not create a placeholder PDF.
4. Start from `data/mftd_3.yaml` for populated YAML shape, `data/mftd_2.yaml` for an empty audit, and `templates/session.html`/`session.css` for the common appearance. Preserve other sessions. If a new scenario cannot fit legibly, make a reusable template improvement and verify existing output; avoid one-off session styling.

## Choose the syllabus content

1. Read the requested session's combined exercise list **and** its ordered Trainee A/B topic lists. Record every exercise ID (such as `ffs-1-e01`), trainee applicability, sequence, and any “if applicable” qualifier. The HTML establishes scheduling, not operational technique.
2. Include a malfunction, emergency, deferred-equipment case, or genuinely unusual circumstance, with only the directly linked actions and recovery needed to rehearse it. Exclude ordinary flight transitions, holding, routine approaches/go-arounds/autoland, packs-OFF takeoffs, and routine systems demonstrations even if the syllabus calls them exercises.
3. Group consecutive linked exercises into one scenario. Put every qualifying exercise ID in exactly one `scenarios[].exercise_ids` list; put every excluded ID in `excluded_items`. This audit stays in YAML, not in the PDF. Mark conditional syllabus events with `conditional: true`.
4. Existing scope decisions are examples, not defaults for other sessions: MFTD 2 has no qualifying item; MFTD 3 combines A e01/e02/e03 into the APU/alternate-start scenario and includes B e13 loss of braking conditionally. Its MEL case is 49-10-01A.

## Research and trace each workflow

1. Use the supplied FCOM, QRH, MEL, and FCTM PDFs in `sources/` for every operational action, callout, limit, and technique. The supplied QRH is `sources/A320FAM_QRH_14JUL26.pdf` (issue 14 JUL 2026; effective 07 SEP 2026); check it directly whenever an FCOM procedure refers to a QRH procedure. In `sources` record each cited PDF's filename/path, document title/code, printed page, PDF page, issue date, effective date, and applicability. Keep `refs` on **every** step even though the PDF displays a deduplicated manual-reference block only once below each workflow.
2. Filter procedures and values to **HS-TX registrations**; passages marked `ALL` may apply. If HS-TX registrations differ, add step-level `applies_to` lists and label the branches. Never import HS-TO-only data. If an exact simulator registration is supplied, retain only its branches. The PDF's general aircraft label is `A320`; keep effectivity details in YAML unless a branch must be identified.
3. For an MEL case, confirm the exact item suffix and matching operational procedure. Ask if a material A/B/C case distinction remains unresolved. In the PDF show the relevant MEL entry/procedure titles and references for reading, **not** a dispatch-basis or MEL-preparation section. Begin the workflow with the first applicable published cue and action.
4. If a required QRH or other referenced document is absent from `sources/`, report the gap and request it. Do not reconstruct missing procedures from memory. Surface conflicts between user notes, syllabus, and manuals; apply a user-approved resolution only to the fact it resolves.

## Write the YAML and PDF workflow

1. Set `session.id`, `session.title`, `session.focus`, `session.effectivity: HS-TX`, and `session.syllabus_ref`. For each scenario set a unique `id`, `trainee` (`A`, `B`, or `Both`), `title`, source-backed `manual_titles` to appear beneath it, `exercise_ids`, syllabus `refs`, `layout`, and ordered `steps`. Add `mel_refs` and `conditional` when applicable. Follow the exact fields in `data/mftd_3.yaml`.
2. In `steps`, preserve published order and triggers: `condition` cues immediately touch the following step; `action` steps use FCOM-style `procedure: [{item, setting}]` rows where appropriate; `callout` steps use exact words with `actor`/`text` or ordered `utterances`; use `caution` only for applicable cautions. Keep text brief and executable. End every scenario with a `resume` step that hands back to the cited normal procedure.
3. Use an assigned PF/PM role when the source specifies it; otherwise use `Crew`. **Project-specific ground-contact resolution:** the user assigns all communication with GND to the **Captain**. Label cockpit `CLEAR TO START ?` and `STARTING ENG(S)__` as Captain, and the ground reply as `GND`, despite the FCOM standard-callout table's generic PF column. This resolution does not change other PF/PM roles, including loss of braking.
4. The template starts each scenario on a new PDF page. Set `layout: single` for a short workflow: the procedure and its references are centered in one column; omit `flow_break_at`. Set `layout: two-column` for a longer workflow and choose `flow_break_at` at a natural handoff, never between a condition and its action. For a workflow that needs two pages, also set `page_break_at` and `continuation_flow_break_at` to create two ordered two-column segments; place all three splits after actions or callouts. Keep the left column at least as tall as the right on each page so the rounded crossover connector joins cleanly. Use `branch_label` for a concise PDF label when a step has a long `applies_to` list; retain the complete registration list in YAML. Check the rendered arrows below their boxes. Do not display syllabus IDs or a rehearsal-aid footer notice.
5. Distinguish MEL deferrals, memory items, QRH actions, and ECAM alerts. When ECAM management is actually required, insert the applicable callouts at their real triggers: PF “ECAM ACTION” when required; PM “CLEAR __ (title of the system) ?” before clearing the current warning/caution or system page; PF “CLEAR __ (title of the system)” or “REMOVE STATUS” for the status page; PM “ECAM ACTIONS COMPLETE” after all applicable actions. Include PF “STOP ECAM”/“CONTINUE ECAM” only for an actual interruption/resumption. Use the procedure's real title and cite FCOM `PRO-ABN-ABN-00 P 8/12` (PDF p. 2831) in the relevant step refs. Do not attach this phraseology automatically to an MEL, memory item, or QRH-only procedure.

## Build, inspect, and deliver

From this directory, use the actual YAML filename:

```sh
UV_CACHE_DIR=/tmp/a320-uv-cache uv run python build_session.py data/mftd_4.yaml --check-only
UV_CACHE_DIR=/tmp/a320-uv-cache uv run python build_session.py data/mftd_4.yaml
```

Substitute `data/ffs_1.yaml` for FFS 1, and similarly for other session numbers. The builder writes `output/<hyphenated-session-id>_practice.pdf` unless `--out` is explicitly supplied. For an empty audit, it prints `SKIPPED` and creates no PDF. If changing the builder or shared template, also run `UV_CACHE_DIR=/tmp/a320-uv-cache uv run python -m unittest discover -s tests -v`.

Check `pdfinfo` for A4 and page count, `pdftotext` for extractable content, and visually inspect **every** page. Confirm there is no clipping, tiny type, broken row, misplaced arrow, broken crossover, or missing reference. Compare all included/excluded exercise IDs against the HTML; verify each procedure row, limit, condition, callout, role, manual title, and source locator against the cited PDF. Deliver the PDF and YAML, and report conditional exercises and any unresolved source gap.

The known MFTD 2 runway conflict was resolved by the user in favor of departure-conditions runway 18 over `VTCCR36`; MFTD 2 still produces no PDF.
