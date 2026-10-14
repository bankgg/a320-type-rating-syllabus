---
name: syllabus-session-briefs
description: Add source-cited failure/abnormal procedure briefs (PF/PM handling modals) to one MFTD/FBS or FFS session of the A320 syllabus webpage (index.html), the way MFTD/FBS 8 was done. Use when the user asks to "add relevant information and procedures for the failures in MFTD 9", "do FFS 5 like MFTD 8", "add abnormal procedures to session X", or similar.
---

# Add failure-procedure briefs to a syllabus session

Reference implementations: **MFTD/FBS 8** (11 briefs) and **MFTD/FBS 9** (9 briefs, including 4 reused from MFTD 8 and the companion `eng-failure-cruise-strategy`). Look at it before starting: `PROCEDURE_GROUPS['mftd-8']` and `EXERCISE_BRIEFS` in `build_comparison.py`, the briefs in `abnormals/`, and the page at `index.html?session=mftd-8&view=exercises&brief=eng-1-2-fail`. The page design is already finished, including the procedure cue (dotted blue underline on Exercises and Schedule titles that open a brief). This skill adds content and mappings; do not restyle the modal or the cue.

## 1. Scope the session
- Normalise the request: "MFTD 9" → `mftd-9`, "FFS 5" → `ffs-5`.
- Read the session in `syllabus_sessions.json`: `exercises` (id, title, A/B assignment), the ordered `topics`, and any `conditional` items.
- Read `FAILURE_NUMBERS[sid]` (the orange failure-related exercise rows) and `FAILURE_SUMMARIES[sid]` (failure subjects in the summary line) in `build_comparison.py`.
- **Brief scope (user decision):** briefs cover **ECAM/QRH abnormal and emergency procedures only**. These get a brief:
  - ECAM alerts;
  - QRH or memory-item procedures (e.g. unreliable speed, emergency evacuation, engine relight);
  - failure handling that has no ECAM procedure, using FCTM technique, FCOM DSC and the QRH reset table (as with FMGC faults).
- **No brief for recovery manoeuvres** (OEI approach, go-around, landing, autoland). They stay plain orange rows.
- Group the briefs by the session's `FAILURE_SUMMARIES` subjects. A group may hold several briefs (e.g. Engine fire → on ground · RTO / in flight). A relight belongs with Engine failure.
- **Sessions without failure items:** if `FAILURE_SUMMARIES[sid]` is empty (currently `mftd-2`, `ffs-1`, `ffs-2`, `ffs-8`), there is nothing to add. Stop and tell the user so, listing the session's "Failures & systems" rows (normal-system demonstrations such as AP/FD logic or sidestick priority) and explaining why they get no brief. Do not create briefs or mappings for normal or demo exercises. Do not edit `FAILURE_SUMMARIES` / `FAILURE_NUMBERS` unless the user asks.
- Present the planned group → brief → exercise-row mapping in one short message before researching. Ask the user only if a subject is genuinely ambiguous.

## 2. Produce the briefs — reuse first
Briefs are **shared between sessions**: one `abnormals/<slug>.json` is one pop-up, identical wherever it appears. Only the "Practised by" badges and the optional session note differ per session. MFTD 8 and MFTD 9 share `emer-evac`, `eng-1-2-fail`, `eng-1-2-fire-in-flight` and `eng-1-2-fire-on-ground`.

For each failure item, decide in this order:
1. **Same procedure, same case → reuse unchanged.** Same ECAM/QRH title and same case (e.g. "Emergency evacuation"; "RTO, engine fire below V1"). Map the exercise to the existing slug. Do not edit the brief. Anything specific to this session's scenario (where it happens, what follows, demo vs full) goes into the **session note** (section 3).
2. **Same procedure, an extra case the session trains → companion brief.** For example, MFTD 9's engine fire happens in cruise and adds a drift-down. Keep the shared brief as it is and write a separate, session-neutral companion brief for the extra technique (`eng-failure-cruise-strategy`). Put it in the same group as its own tab.
3. **A genuinely different procedure or variant → new brief** with its own slug, via the **`a320-ecam-abnormal` skill**. That skill covers sources (FCOM, QRH, FCTM, PDP), HS-TX filtering, ordered PF/PM turns, company phraseology and `brief_kit.py`.
4. **Editing a shared brief** is only for corrections or additions that are true for **every** session using it (e.g. a source error, a missed callout). Before editing, list the sessions that use it, with `grep -n "<slug>" build_comparison.py`. After editing, rerun the check for **each** of those sessions (section 4).

**Briefs must be session-neutral.** No "MFTD"/"FFS" names, exercise numbers or scenario remarks anywhere in a brief's JSON. Phrase conditional cases as procedure conditions ("If the approach is discontinued …"). The build rejects any brief that names a session.

Every brief must validate: `python3 -I .claude/skills/a320-ecam-abnormal/scripts/render_md.py abnormals/<slug>.json`.

## 3. Map them in `build_comparison.py`
- **`PROCEDURE_GROUPS[sid]`:** a list of `(label, (member, …))`. Each member is `(slug, tab_label)` or `(slug, tab_label, session_note)`.
  - `label` must equal one of `FAILURE_SUMMARIES[sid]` **exactly**; it becomes the tappable summary link.
  - Keep `tab_label` short and distinct (e.g. "On ground · RTO", "In flight", "Drift down"). Trainee badges are added automatically.
  - `session_note` holds this session's scenario context, shown in the pop-up as "In <session>: …". Examples: "Fire extinguished after the second agent." or "Fire in cruise (FL 290): after the fire drill, drift down using the standard strategy (see Drift down)." Take it only from the syllabus wording; never invent scenario details.
- **`EXERCISE_BRIEFS`:** map each failure-related exercise id (`<sid>-eNN`) that has a brief to its main slug. Each id must be in `FAILURE_IDS`.
  - Every group needs at least one exercise-mapped member.
  - Companion briefs need no exercise of their own; they inherit the group's trainees and open from the group's tabs.
- Schedule rows link automatically through their `exercise_ids`. Every linked row — an Exercises title or a Schedule topic — shows a dotted blue underline (the page's only "opens a procedure" cue, keyed in each table's key); an orange row with no mapped exercise stays plain. So the mapping **is** the cue: map every failure exercise that has an ECAM/QRH brief, and never map a recovery row just to make it tappable.
- Never edit `syllabus_sessions.json` facts or `index.html` directly. Rebuild with `python3 build_comparison.py`. Its validation fails clearly on bad labels, ids, unreachable groups, session-naming briefs or invalid briefs.

## 4. Verify (one batched round, one fix round, at most one confirm)
Run `sh .claude/skills/syllabus-session-briefs/scripts/run_check.sh <sid>`. It fetches, once and without root, `libasound` for the cached headless Chromium and ~50 system libraries for the cached WebKit, then runs [scripts/check_session.py](scripts/check_session.py) through `uv run --with playwright==1.63.0` (the version matching both cached browsers). It takes about 4–5 min. WebKit is the engine of **every iPad browser, Safari and Chrome alike** (the user mostly uses Chrome on iPad), so a run without WebKit counts as a failure.
- **Checks, at 1194×834 (iPad) and 390×844 (phone):** every `.brief-open` (exercise and schedule rows) and `.summary-link` opens the right brief; in both Exercises and Schedule, every linked title has the dotted underline, no plain title has it, and the table key is visible; no page or dialog overflow; no visible text under 16px; buttons and summaries at least 44px tall; Escape closes the dialog and clears `?brief=`; every `&brief=<slug>` deep link works; no console errors.
- **iPad interaction suite, in Chromium (mouse) and WebKit (touch), at both sizes:** open from a row, then close by tapping outside — fresh, after toggling More detail, after a jump-bar jump, after scrolling the card — and by the close button; the Setup dialog likewise. Each close must leave the dialog shut, `?brief=` cleared and **no focus ring** on the page.
- **Also checked:** the Setup dialog of another session still opens; every brief renders without JavaScript.
- **Output:** a JSON report (`failures` must be empty; exit code 1 otherwise; `<viewport>-exercises.linked` / `<viewport>-schedule.linked` list the underlined titles), plus full-page Exercises and Schedule screenshots and screenshots of each brief's first view and full height in `.claude/skills/syllabus-session-briefs/cache/shots/<sid>/`. **Look at the screenshots**: the flow turn order, condition indentation and HS-TX branch chips need human-eye review. In `*-exercises.png` and `*-schedule.png`, confirm the underlined titles are exactly the ECAM/QRH items and the remaining orange rows are recovery manoeuvres.
- **Shared-brief regression:** if you edited any shared brief or the template, rerun the check for every session that uses it (e.g. `mftd-8`), not only the new one.
- **Reuse check:** for each reused brief, confirm the content is identical in both sessions. Only the badges and the session note may differ.

## 5. Finish
- Update `PRODUCT.md` (which sessions have briefs) and the memory note about abnormal briefs.
- Report:
  - the groups and briefs per subject, marking each as **reused unchanged**, **companion** or **new** (and any shared brief that was corrected, with the sessions rechecked);
  - the rows now underlined in Exercises and Schedule (from the `linked` lists) and the orange rows left plain (recovery, no brief);
  - gaps and source conflicts found by the briefs;
  - the review URL (`python3 -m http.server 8765 --bind 127.0.0.1`, then `/index.html?session=<sid>&view=exercises`).
