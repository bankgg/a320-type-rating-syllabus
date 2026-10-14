# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Trainee pilots preparing for A320 type-rating simulator sessions. Their main job is to find the relevant session, understand their assigned exercises and sequence, and compare Trainee A and Trainee B requirements before training.

## Product Purpose

Provide a single English webpage for studying the A/B simulator syllabus. Success means a trainee can locate a session, distinguish shared and trainee-specific exercises, and understand its ordered topics, flight setup, weather, and conditional alternatives without reconstructing the comparison from separate source documents.

This product record covers the whole workspace. The active product direction is the syllabus comparison webpage; Source-traced abnormal-procedure briefs are now part of the webpage for MFTD/FBS 8, MFTD/FBS 9, FFS 3 and FFS 4: tapping a failure opens a cited PF/PM handling brief built from the FCOM, FCTM and QRH in `books/` (HS-TX only) by the project skill `.claude/skills/a320-ecam-abnormal`. Other sessions gain briefs through the project skill `.claude/skills/syllabus-session-briefs` (same scope, mapping and checks as MFTD/FBS 8); the separate rehearsal-PDF workflow under `sessions/` remains deferred. The comparison is web-only; PDF generation is no longer required.

## Positioning

The comparison brings the reviewed Trainee A and Trainee B syllabus into one session-based reference. It preserves each trainee's ordered topics while identifying shared exercises, meaningful differences, and conditional applicability. The mapping is curated before rendering rather than inferred by the webpage.

## Operating Context

- Primary device: an 11-inch iPad in landscape orientation.
- Secondary device: mobile phones. Desktop is the last priority.
- Use: digital study and preparation for simulator sessions.
- Hosting target: GitHub Pages. Online access is acceptable; offline availability is not a current requirement.
- Language: English, retaining the syllabus terminology.

## Capabilities and Constraints

- The syllabus covers 18 sessions: MFTD/FBS 2–9 and FFS 1–10.
- The webpage scope includes the course overview, combined exercises, A/B exercise differences, ordered trainee topics, flight setup, departure and arrival weather, and conditional alternatives.
- Preserve reviewed syllabus facts, topic order, exercise identifiers, trainee applicability, unspecified values, and resolved source discrepancies. Do not invent missing training content or silently equate meaningfully different exercises.
- The syllabus establishes scheduling and training content; it does not establish operational technique.
- The existing webpage uses static HTML/CSS rendered from curated JSON with Python and Jinja2. Retain this tooling for the current scope.
- Existing session authoring retains its own manual citations, HS-TX applicability, crew-role rules, and source checks under `sessions/AGENTS.md`. Those constraints remain relevant when deferred procedure work resumes.
- The standalone artifact is `index.html`, targeting the GitHub repository `bankgg/a320-type-rating-syllabus`; GitHub Pages configuration has not been specified. The webpage uses one selected session, grouped numbered MFTD/FBS and FFS buttons, Overview and Previous/Next controls, a compact airport/runway strip and two detail tabs: Exercises and Schedule (published ordered topics). The selected detail tab persists when changing sessions. Session and overview-entry descriptions combine actual A/B failure and emergency subjects with bullet-dot separators and no trainee attribution, omitting ordinary exercises and recovery variants; sessions without failure subjects say No failure exercises. All exercise-count captions are omitted; repeat notation such as ×2 and Session X of 18 progress remain. Schedule topic text uses one dark color for both routine and exercise entries; number and status metadata retain their separate emphasis. Shared Schedule rows omit redundant Both labels; all-shared schedules such as FFS 8 and FFS 10 omit the A/B status column on both tables while retaining each full published sequence. Shared setup/weather values continue to use explicit Both labels where needed. The visible Schedule label retains the internal topics view identifier for bookmark compatibility. Complete flight setup, departure and arrival weather, and full routes appear in a native Setup & conditions dialog. Both trainees receive equal priority; shared values appear once. Blue rows and explicit A/B status identify differences; orange identifies failure-related exercises and recovery across categories and linked ordered topics, with rectangular row outlines formed by top/bottom borders and outer side edges without internal vertical dividers. Adjacent failure rows share one orange divider; isolated rows keep a complete single-pixel outline. Query-string bookmarks and browser history preserve session/view selection, with one-time migration of legacy hash bookmarks. Navigation uses buttons without internal anchor jumps. Complete reading remains available without JavaScript. The visual direction is a light briefing matrix for daylight study, retaining static Python/Jinja2 tooling without a runtime Node or server requirement.

## Evidence on Hand

- `syllabus_sessions.json`: curated session data and A/B exercise mapping used by the comparison builder.
- `syllabus_b_extracted.json`: extracted Trainee B syllabus material.
- `comparison_template.html.j2` and `build_comparison.py`: existing comparison template, rendering logic, and content checks.
- `index.html`: standalone generated comparison webpage and repository entry point. The original supplied source HTML remains at `sessions/sources/A320_Trainee_A_vs_B_Syllabus_Comparison.html`.
- `sessions/AGENTS.md` and `sessions/README.md`: source-traced session authoring rules, established constraints, and reviewed project-specific resolutions.
- `sessions/data/`: existing session audits and procedure workflows.
- `sessions/sources/`: supplied FCOM, QRH, MEL, and FCTM manuals for source-traced procedure work.
- `books/`: the FCOM, FCTM and QRH (14 JUL 26) and the Airbus PDP tutorial slide deck (Jan 2024; generic A320/A330 task sharing and callouts, read visually) used by the `a320-ecam-abnormal` skill.
- `abnormals/`: generated procedure briefs (`<slug>.json` source of truth, rendered `<slug>.md`), mapped to exercises in `build_comparison.py`.

## Product Principles

1. Preserve source fidelity: presentation changes must keep reviewed training facts and their meaning intact.
2. Make trainee distinctions explicit: shared, unique, mixed, and conditional content must remain understandable.
3. Organize study around the actual session: help trainees locate requirements and follow their published sequence.
4. Prioritize tablet study: judge reading and navigation on the 11-inch landscape iPad first, then mobile, then desktop.
5. Keep the active scope focused: the webpage is a syllabus comparison with source-cited procedure briefs for mapped failures; briefs never add facts beyond `books/`, and PDF output is not required.

## Accessibility & Inclusion

Support comfortable reading and touch navigation on the primary iPad and on mobile phones. Convey trainee applicability and conditional content in text as well as any visual styling. No additional product-specific accessibility standard has been established.
