#!/usr/bin/env python3
"""Validate session data and render a source-traced A4 practice PDF."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from weasyprint import HTML


ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "templates"
DEFAULT_OUTPUT_DIR = ROOT / "output"
HS_TX = re.compile(r"^HS-TX[A-Z]$")


class SessionDataError(ValueError):
    pass


def required_text(value: object, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SessionDataError(f"{location} must be nonempty text")
    return value.strip()


def required_list(value: object, location: str) -> list:
    if not isinstance(value, list):
        raise SessionDataError(f"{location} must be a list")
    return value


def validate_refs(refs: object, sources: dict, location: str, *, operational: bool = False) -> None:
    keys = required_list(refs, f"{location}.refs")
    if not keys:
        raise SessionDataError(f"{location}.refs must contain at least one source")
    for key in keys:
        if key not in sources:
            raise SessionDataError(f"{location} cites unknown source {key!r}")
    if operational and not any(Path(sources[key]["path"]).suffix.lower() == ".pdf" for key in keys):
        raise SessionDataError(f"{location} needs an official PDF source")


def validate_applicability(value: object, location: str) -> None:
    if value is None or value == "all HS-TX":
        return
    registrations = required_list(value, location)
    if not registrations or any(not isinstance(x, str) or not HS_TX.fullmatch(x) for x in registrations):
        raise SessionDataError(f"{location} must list only HS-TX registrations")


def validate(data: dict) -> dict:
    if not isinstance(data, dict):
        raise SessionDataError("Session YAML must contain a mapping")
    session = data.get("session")
    if not isinstance(session, dict):
        raise SessionDataError("session must be a mapping")
    for field in ("id", "title", "focus", "effectivity", "syllabus_ref"):
        required_text(session.get(field), f"session.{field}")
    if session["effectivity"] != "HS-TX":
        raise SessionDataError("session.effectivity must be HS-TX")

    sources = data.get("sources")
    if not isinstance(sources, dict) or not sources:
        raise SessionDataError("sources must be a nonempty mapping")
    for key, source in sources.items():
        if not isinstance(source, dict):
            raise SessionDataError(f"sources.{key} must be a mapping")
        for field in ("title", "path", "locator", "applicability"):
            required_text(source.get(field), f"sources.{key}.{field}")
        source_path = ROOT / source["path"]
        if not source_path.is_file():
            raise SessionDataError(f"sources.{key}.path does not exist: {source_path}")
        if source_path.suffix.lower() == ".pdf":
            for field in ("issue", "effective"):
                required_text(source.get(field), f"sources.{key}.{field}")
        if source["applicability"] not in ("syllabus", "ALL", "HS-TX"):
            raise SessionDataError(f"sources.{key}.applicability must be syllabus, ALL, or HS-TX")
    if session["syllabus_ref"] not in sources:
        raise SessionDataError("session.syllabus_ref is not in sources")

    scenarios = required_list(data.get("scenarios"), "scenarios")
    seen_scenarios: set[str] = set()
    seen_exercises: set[str] = set()
    for n, scenario in enumerate(scenarios, 1):
        location = f"scenarios[{n}]"
        if not isinstance(scenario, dict):
            raise SessionDataError(f"{location} must be a mapping")
        scenario_id = required_text(scenario.get("id"), f"{location}.id")
        if scenario_id in seen_scenarios:
            raise SessionDataError(f"duplicate scenario id {scenario_id}")
        seen_scenarios.add(scenario_id)
        if scenario.get("trainee") not in ("A", "B", "Both"):
            raise SessionDataError(f"{location}.trainee must be A, B, or Both")
        required_text(scenario.get("title"), f"{location}.title")
        manual_titles = required_list(scenario.get("manual_titles"), f"{location}.manual_titles")
        if not manual_titles:
            raise SessionDataError(f"{location}.manual_titles must not be empty")
        for title in manual_titles:
            required_text(title, f"{location}.manual_titles entry")
        validate_refs(scenario.get("refs"), sources, location)
        validate_applicability(scenario.get("applies_to"), f"{location}.applies_to")
        for ref in required_list(scenario.get("mel_refs", []), f"{location}.mel_refs"):
            if ref not in sources or not Path(sources[ref]["path"]).suffix.lower() == ".pdf":
                raise SessionDataError(f"{location}.mel_refs must cite supplied PDF sources")
        exercise_ids = required_list(scenario.get("exercise_ids"), f"{location}.exercise_ids")
        if not exercise_ids:
            raise SessionDataError(f"{location}.exercise_ids must not be empty")
        for exercise_id in exercise_ids:
            required_text(exercise_id, f"{location}.exercise_ids entry")
            if exercise_id in seen_exercises:
                raise SessionDataError(f"exercise {exercise_id} appears in more than one scenario")
            seen_exercises.add(exercise_id)
        steps = required_list(scenario.get("steps"), f"{location}.steps")
        if not steps:
            raise SessionDataError(f"{location}.steps must not be empty")
        layout = scenario.get("layout")
        if layout not in ("single", "two-column"):
            raise SessionDataError(f"{location}.layout must be single or two-column")
        if layout == "two-column":
            split = scenario.get("flow_break_at")
            if not isinstance(split, int) or isinstance(split, bool) or not 0 < split < len(steps):
                raise SessionDataError(f"{location}.flow_break_at must split the ordered steps into two columns")
            if isinstance(steps[split - 1], dict) and steps[split - 1].get("kind") == "condition":
                raise SessionDataError(f"{location}.flow_break_at must not separate a condition from its following step")
            if "page_break_at" in scenario:
                page_split = scenario["page_break_at"]
                continuation_split = scenario.get("continuation_flow_break_at")
                if (
                    not isinstance(page_split, int)
                    or isinstance(page_split, bool)
                    or not isinstance(continuation_split, int)
                    or isinstance(continuation_split, bool)
                    or not split < page_split < continuation_split < len(steps)
                ):
                    raise SessionDataError(f"{location} continuation splits must preserve step order across two pages")
                if any(
                    isinstance(steps[index - 1], dict) and steps[index - 1].get("kind") == "condition"
                    for index in (page_split, continuation_split)
                ):
                    raise SessionDataError(f"{location} continuation splits must not separate a condition from its following step")
            elif "continuation_flow_break_at" in scenario:
                raise SessionDataError(f"{location}.continuation_flow_break_at requires page_break_at")
        elif "flow_break_at" in scenario:
            raise SessionDataError(f"{location}.flow_break_at is only used for two-column layouts")
        elif "page_break_at" in scenario or "continuation_flow_break_at" in scenario:
            raise SessionDataError(f"{location} continuation splits require a two-column layout")
        display_refs = list(scenario.get("mel_refs", []))
        for s, step in enumerate(steps, 1):
            step_location = f"{location}.steps[{s}]"
            if not isinstance(step, dict):
                raise SessionDataError(f"{step_location} must be a mapping")
            if step.get("kind") not in ("action", "callout", "caution", "condition", "resume"):
                raise SessionDataError(f"{step_location}.kind is unsupported")
            if step["kind"] == "action" and "procedure" in step:
                rows = required_list(step["procedure"], f"{step_location}.procedure")
                if not rows:
                    raise SessionDataError(f"{step_location}.procedure must not be empty")
                for r, row in enumerate(rows, 1):
                    if not isinstance(row, dict):
                        raise SessionDataError(f"{step_location}.procedure[{r}] must be a mapping")
                    unexpected = set(row) - {"item", "setting", "actor"}
                    if unexpected:
                        raise SessionDataError(f"{step_location}.procedure[{r}] has unexpected fields: {sorted(unexpected)}")
                    for field in ("item", "setting"):
                        required_text(row.get(field), f"{step_location}.procedure[{r}].{field}")
                    if "actor" in row:
                        required_text(row["actor"], f"{step_location}.procedure[{r}].actor")
            elif step["kind"] == "callout" and "utterances" in step:
                utterances = required_list(step["utterances"], f"{step_location}.utterances")
                if not utterances:
                    raise SessionDataError(f"{step_location}.utterances must not be empty")
                for u, utterance in enumerate(utterances, 1):
                    if not isinstance(utterance, dict):
                        raise SessionDataError(f"{step_location}.utterances[{u}] must be a mapping")
                    for field in ("speaker", "words"):
                        required_text(utterance.get(field), f"{step_location}.utterances[{u}].{field}")
            else:
                required_text(step.get("text"), f"{step_location}.text")
                if step["kind"] == "callout":
                    required_text(step.get("actor"), f"{step_location}.actor")
            if "detail" in step:
                required_text(step["detail"], f"{step_location}.detail")
            if "stage" in step:
                required_text(step["stage"], f"{step_location}.stage")
            if "branch_label" in step:
                required_text(step["branch_label"], f"{step_location}.branch_label")
                if "applies_to" not in step:
                    raise SessionDataError(f"{step_location}.branch_label requires applies_to")
            validate_refs(step.get("refs"), sources, step_location, operational=True)
            validate_applicability(step.get("applies_to"), f"{step_location}.applies_to")
            for ref in step["refs"]:
                if ref not in display_refs:
                    display_refs.append(ref)
        scenario["display_refs"] = display_refs
        if steps[0]["kind"] not in ("action", "condition"):
            raise SessionDataError(f"{location}.steps must begin with the first action or its trigger")
        if steps[-1]["kind"] != "resume":
            raise SessionDataError(f"{location}.steps must end with a normal-procedure handoff")

    excluded = required_list(data.get("excluded_items", []), "excluded_items")
    for exercise_id in excluded:
        required_text(exercise_id, "excluded_items entry")
        if exercise_id in seen_exercises:
            raise SessionDataError(f"exercise {exercise_id} is both included and excluded")
    syllabus_path = ROOT / sources[session["syllabus_ref"]]["path"]
    syllabus_text = syllabus_path.read_text(encoding="utf-8")
    syllabus_ids = set(re.findall(r'id="(' + re.escape(session["id"]) + r'-e\d+)"', syllabus_text))
    if not syllabus_ids:
        raise SessionDataError(f"no syllabus exercise IDs found for {session['id']}")
    accounted = seen_exercises | set(excluded)
    if accounted != syllabus_ids:
        missing = sorted(syllabus_ids - accounted)
        unknown = sorted(accounted - syllabus_ids)
        raise SessionDataError(f"exercise audit mismatch; missing={missing}, unknown={unknown}")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("session_file", type=Path, help="YAML session data")
    parser.add_argument("--out", type=Path, help="PDF output path")
    parser.add_argument("--check-only", action="store_true", help="validate without rendering")
    args = parser.parse_args()

    try:
        with args.session_file.open(encoding="utf-8") as handle:
            data = validate(yaml.safe_load(handle))
    except (OSError, yaml.YAMLError, SessionDataError) as exc:
        print(f"Session data error: {exc}", file=sys.stderr)
        return 2

    session = data["session"]
    if not data["scenarios"]:
        print(f"SKIPPED {session['id']}: no qualifying scenarios; no PDF created")
        return 0
    if args.check_only:
        print(f"VALID {session['id']}: {len(data['scenarios'])} scenarios")
        return 0

    output = args.out or DEFAULT_OUTPUT_DIR / f"{session['id']}_practice.pdf"
    output.parent.mkdir(parents=True, exist_ok=True)
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = environment.get_template("session.html")
    rendered = template.render(**data)
    HTML(string=rendered, base_url=str(ROOT)).write_pdf(output)
    print(f"CREATED {output} ({len(data['scenarios'])} scenarios)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
