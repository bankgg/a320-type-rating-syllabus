# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static, self-contained syllabus webpage (`index.html`) comparing Trainee A and Trainee B across 18 A320 simulator sessions (MFTD/FBS 2–9, FFS 1–10). Failure rows can open source-cited ECAM/QRH handling briefs in a dialog. The audience is an A320 type-rating trainee who studies on an 11" iPad in landscape, mostly in **Chrome for iPad** (Safari too). Both browsers run on WebKit, then phone, then desktop. Hosted on GitHub Pages from `main` (`bankgg/a320-type-rating-syllabus`).

`PRODUCT.md` (scope, audience, principles) and `DESIGN.md` (visual system) are authoritative for product and design decisions; read them before UI work.

## Commands

```sh
python3 -m pip install -r requirements.txt   # Jinja2 only
python3 build_comparison.py                  # validate data + briefs, write index.html
python3 -m http.server 8765 --bind 127.0.0.1 # preview: /index.html?session=mftd-8&view=exercises&brief=elec-emer-config

# validate + re-render one brief (JSON -> .md); the build runs the same validation
python3 -I .claude/skills/a320-ecam-abnormal/scripts/render_md.py abnormals/<slug>.json

# browser checks for one session: Chromium + WebKit, iPad 1194x834 and phone 390x844, ~5 min
sh .claude/skills/syllabus-session-briefs/scripts/run_check.sh <session-id>   # e.g. mftd-9
```

`run_check.sh` fetches the needed system libraries (libasound for Chromium; about 50 for WebKit, including a libbacktrace stub) into the skill's `cache/` without root. It pins `playwright==1.63.0` to match the cached `chromium-1243` / `webkit-2359` browsers. A run without WebKit counts as a failure. Screenshots land in `.claude/skills/syllabus-session-briefs/cache/shots/<sid>/`; look at them.

## Architecture

**Never edit `index.html` directly**; it is regenerated. The pipeline is:

1. `syllabus_sessions.json` holds reviewed, frozen session facts: exercises with ids `<sid>-eNN` and A/B assignment, ordered `topics` per trainee (each topic lists its `exercise_ids`), setup, weather and conditionals. `curate_sessions.py` is the separate, one-off step that froze the A/B exercise mapping. The renderer never infers equivalence. Don't change syllabus facts.
2. `build_comparison.py` holds hand-curated presentation mappings, validates everything and builds the view model:
   - `FAILURE_NUMBERS` / `FAILURE_IDS`: which exercise rows are orange (failure or recovery).
   - `FAILURE_SUMMARIES`: the failure subjects in each session's summary line. An empty tuple means "No failure exercises" (mftd-2, ffs-1, ffs-2, ffs-8).
   - `PROCEDURE_GROUPS[sid]`: `(summary label, ((slug, tab_label[, session_note]), …))`. The label must equal a `FAILURE_SUMMARIES` entry exactly.
   - `EXERCISE_BRIEFS`: exercise id → brief slug. Schedule topics link automatically through their `exercise_ids`, and a linked row gets the dotted-underline "opens a procedure" cue.

   The build loads every `abnormals/*.json` through `render_md.validate`. It rejects any brief that mentions MFTD/FFS/FBS, because briefs are session-neutral and shared.
3. `comparison_template.html.j2` is one file holding all CSS and JS inline:
   - **Routing:** query-string state `?session=<sid>&view=exercises|topics&brief=<slug>` (`view=topics` is the visible "Schedule" tab, kept for bookmarks), with browser history; legacy hash bookmarks are migrated.
   - **Dialog:** one shared native `<dialog>` serves both Setup & conditions and the briefs. The `<dialog>` is a transparent full-screen layer holding a scrolling `.dialog-card`, so a tap whose target is the dialog itself means "outside". Panels are moved into the card and back out on close. Focus is deliberately not returned to the opener, because it left a focus ring on iPad.
   - **Jump bar:** the Flow/Manuals/Detail bar tracks the scroll position.
   - **No JavaScript:** the page renders every session, setup and brief in document order.

## Procedure briefs (`abnormals/`)

- **Format:** `abnormals/<slug>.json` (schema `a320-ecam-abnormal/3`) is the source of truth; `<slug>.md` is rendered from it. The slug is the ECAM title lower-cased with non-alphanumerics replaced by `-`.
- **Sharing:** one JSON gives an identical pop-up in every session that uses it. Per-session context goes only in the `session_note` in `PROCEDURE_GROUPS`. An extra case gets a separate companion brief (e.g. `eng-failure-cruise-strategy`). Edit a shared brief only for corrections true for every session, then rerun `run_check.sh` for each session that uses it (`grep -n "<slug>" build_comparison.py`).
- **Skills:** create briefs with the project skills, not by hand.
  - `a320-ecam-abnormal` builds one brief, using `scripts/manuals.py` to search the PDFs and `scripts/brief_kit.py` to author it.
  - `syllabus-session-briefs` does a whole session: scope, reuse, mapping and checks.
- **Scope:** ECAM/QRH abnormals only. Recovery manoeuvres (one-engine-inoperative approach, go-around, autoland) stay plain rows.
- **Sources:** only `books/`: THA FCOM/FCTM/QRH (14 JUL 26) plus the Airbus PDP tutorial slides. Read the slides visually; their text extraction is scrambled. Every fact carries a locator.
- **Aircraft:** HS-TX registrations only. Never use HS-TO-only content; show HS-TX splits as `applies_to` branches.
- **ECAM flow rules,** which `render_md.py` enforces:
  - Every ECAM procedure that reaches STATUS uses `brief_kit.status_turns`: PM "STATUS" → PF "STOP ECAM" → PM ECAM ACTIONS STOP → PF "CONTINUE ECAM" → PM read, "REMOVE STATUS ?" → PF "REMOVE STATUS" → PM "ECAM ACTIONS COMPLETE" (FCTM AOP-30-30, PDP PDF 426).
  - Exception: the procedure lists STATUS as NOT AVAIL (FWC 1+2 FAULT).
- **Company phraseology** overrides generic wording: "CABIN CREW, AT YOUR STATIONS"; "REMAIN SEATED, RESUME NORMAL DUTIES"; call sign "THA {XXX}". See `reference/abnormal-operations.md`.

## Repository rules

- **No PDFs in git,** ever (`*.pdf`, `books/` and `sessions/sources/` are gitignored). `.ignore` re-includes them for ripgrep-based search, so agents can still find them; don't hide them any other way. The FCOM is over 100 MB, which is too big to `Read` directly: use `manuals.py render fcom <pages>` and read the PNGs.
- **No screen-reader-only UI:** no `sr-only` / visually hidden text and no skip buttons (user decision). ARIA attributes the JS relies on (`role="tab"`, `aria-selected`, `aria-current`) stay.
- **Hover:** every `:hover` rule sits inside `@media (hover: hover)` so tapped controls don't stay highlighted on iPad.
- **Design docs:** the `.impeccable/` directory and `DESIGN.md` are maintained with the impeccable design skill. Keep `DESIGN.md` in step with shipped UI changes.

## `sessions/` (separate, deferred workflow)

`sessions/` builds per-session rehearsal PDFs from YAML (`build_session.py`, tests in `sessions/tests/`). It has its own complete instructions in `sessions/AGENTS.md`; read them before touching that directory. Its ECAM callout rule matches the briefs: the full STATUS exchange (with "STOP ECAM") whenever the STATUS page appears.
