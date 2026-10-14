# A320 SIM syllabus

A static English syllabus comparison for Trainee A and Trainee B, designed for study on an iPad in landscape. The page covers 18 sessions and keeps the reviewed exercise assignments, setup, conditions and ordered topics together.

Choose a session using the numbered **MFTD/FBS** and **FFS** buttons or **Previous / Next**. Its short description combines both trainees' failure subjects, separated by bullet dots. A compact strip shows the airports and runways. Use **Exercises** or **Schedule** to compare the trainees, and open **Setup & conditions** for the complete flight setup and weather. All schedule topic text uses the same dark color. Orange bordered rows identify failure-related exercises and recovery; blue rows and explicit labels identify A/B differences. Schedule omits redundant Both labels and hides the status column when the session has no trainee-specific differences. Course overview is the default.

The setup popup shows all values together on landscape iPad; smaller screens and enlarged text can scroll. Session and tab selection support browser back/forward. Old hash bookmarks remain supported without jumping within the page. With JavaScript disabled, every session and its complete setup and topics remain readable in course order.

## Build

```sh
python3 -m pip install -r requirements.txt
python3 build_comparison.py
```

The build produces `index.html`. Builds are web-only and require Jinja2. The previous `--html-only` flag remains accepted for existing commands.

## Preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open [the comparison page](http://localhost:8765/index.html?session=mftd-5&view=exercises). The generated HTML is self-contained and can be opened directly or hosted as a static page. Python is needed only to rebuild it; no server-side Python or Node runtime is needed to use the page.

## Project files

- `syllabus_sessions.json` contains the reviewed session data.
- `build_comparison.py` validates the data and derives presentation values, including the reviewed failure/recovery highlights.
- `comparison_template.html.j2` contains the responsive interface.
- `PRODUCT.md` records the audience and scope; `DESIGN.md` records the visual system.
- `abnormals/` holds the procedure briefs (JSON plus rendered Markdown). `PROCEDURE_GROUPS` and `EXERCISE_BRIEFS` in `build_comparison.py` map them to session failures; the build validates every brief.
- `.claude/skills/a320-ecam-abnormal/` is the Claude Code skill that builds a brief from an ECAM title using the FCOM, FCTM, QRH and Airbus PDP tutorial slides in `books/` (HS-TX only). Prompt an ECAM title such as `ELEC EMER CONFIG` to run it.
- `.claude/skills/syllabus-session-briefs/` is the Claude Code skill that adds failure-procedure briefs to a whole session (ask e.g. "add the failure procedures for MFTD 9"); it maps briefs in `build_comparison.py` and runs the browser checks in its `scripts/run_check.sh`.
- `sessions/README.md` documents the separate source-traced procedure workflow.

Edit the template and renderer, then rebuild the HTML. Direct edits to the generated page are replaced by the next build. The historical source webpage under `sessions/sources/` belongs to the separate procedure-authoring workflow.
