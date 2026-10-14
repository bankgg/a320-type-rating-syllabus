# A320 SIM practice PDF template

This workspace produces A4 procedure/callout flowcharts for **malfunctions and unusual circumstances** in the [A/B SIM syllabus](sources/A320_Trainee_A_vs_B_Syllabus_Comparison.html). Short procedures use one centered column; longer ones use two columns with a rounded connector. Published MEL or abnormal-procedure titles sit under each scenario title. Dark condition bars sit directly above the actions they govern. FCOM-style item/setting rows appear in sequence. Ground-contact callouts are assigned to the Captain as specified for this project. MEL cases show only entry/procedure references for manual reading.

## Build the example

Install [uv](https://docs.astral.sh/uv/) if it is unavailable, then run from this directory:

```sh
uv sync
uv run python build_session.py data/mftd_3.yaml
```

The result is `output/mftd-3_practice.pdf`. To validate data without rendering, add `--check-only`. Building `data/mftd_2.yaml` prints a skip message and produces no PDF because no MFTD 2 items meet the current scope.

## Make another session

1. Give the AI the target session ID and any instructor notes. The complete authoring instructions are in [AGENTS.md](AGENTS.md).
2. Review the selected exercise IDs, MEL references, HS-TX applicability, source citations, and single/two-column layout choice in the new YAML file. Syllabus IDs remain in the data audit and do not display under the PDF title.
3. Use underscores in the YAML filename and a hyphen in `session.id`: MFTD/FBS 4 is `data/mftd_4.yaml` with `session.id: mftd-4`, producing `output/mftd-4_practice.pdf`; FFS 1 is `data/ffs_1.yaml` with `session.id: ffs-1`. Run `UV_CACHE_DIR=/tmp/a320-uv-cache uv run python build_session.py data/mftd_4.yaml` (or the corresponding FFS filename) and inspect the PDF before use.

The editable layout is [session.html](templates/session.html) and [session.css](templates/session.css). `build_session.py` rejects missing citations, missing source files, unsupported trainee labels, duplicate exercise IDs, and non-HS-TX registration lists. The YAML retains citations for every step; the PDF gathers them once below each workflow. When manuals are replaced, recheck every affected step and update the cited edition and location before rebuilding.

Example request: “Create the MFTD/FBS 4 practice PDF using `AGENTS.md`. My instructor notes are: …”

The PDF is a rehearsal aid. The supplied manuals identify downloaded or printed copies as uncontrolled; consult current controlled manuals and the instructor briefing for operational use.
