from __future__ import annotations

import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from build_session import ROOT, SessionDataError, validate


class SessionDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mftd3 = yaml.safe_load((ROOT / "data/mftd_3.yaml").read_text(encoding="utf-8"))
        cls.mftd4 = yaml.safe_load((ROOT / "data/mftd_4.yaml").read_text(encoding="utf-8"))

    def test_example_covers_only_selected_unusual_exercises(self) -> None:
        data = validate(copy.deepcopy(self.mftd3))
        included = {item for scenario in data["scenarios"] for item in scenario["exercise_ids"]}
        self.assertEqual(included, {"mftd-3-e01", "mftd-3-e02", "mftd-3-e03", "mftd-3-e13"})
        self.assertTrue(data["scenarios"][1]["conditional"])

    def test_operational_action_requires_pdf_reference(self) -> None:
        data = copy.deepcopy(self.mftd3)
        data["scenarios"][0]["steps"][0]["refs"] = ["S1"]
        with self.assertRaisesRegex(SessionDataError, "official PDF source"):
            validate(data)

    def test_syllabus_items_must_all_be_accounted_for(self) -> None:
        data = copy.deepcopy(self.mftd3)
        data["excluded_items"].remove("mftd-3-e12")
        with self.assertRaisesRegex(SessionDataError, "exercise audit mismatch"):
            validate(data)

    def test_other_fleet_registration_is_rejected(self) -> None:
        data = copy.deepcopy(self.mftd3)
        data["scenarios"][0]["steps"][0]["applies_to"] = ["HS-TOA"]
        with self.assertRaisesRegex(SessionDataError, "HS-TX registrations"):
            validate(data)

    def test_timeline_starts_with_procedure_and_ends_with_handoff(self) -> None:
        data = validate(copy.deepcopy(self.mftd3))
        self.assertEqual(data["scenarios"][1]["manual_titles"], ["[MEM] LOSS OF BRAKING"])
        first = data["scenarios"][0]["steps"][0]
        self.assertEqual(first["kind"], "condition")
        self.assertIn("Before connecting", first["text"])
        procedure = data["scenarios"][0]["steps"][1]["procedure"]
        self.assertEqual([(row["item"], row["setting"]) for row in procedure[:2]], [("PACK 1", "OFF"), ("PACK 2", "OFF")])
        self.assertEqual(data["scenarios"][0]["flow_break_at"], 10)
        self.assertEqual(data["scenarios"][0]["layout"], "two-column")
        self.assertEqual(data["scenarios"][1]["layout"], "single")
        self.assertNotIn("flow_break_at", data["scenarios"][1])
        self.assertEqual(data["scenarios"][0]["steps"][-1]["kind"], "resume")
        self.assertEqual(data["scenarios"][1]["steps"][-1]["kind"], "resume")

    def test_references_are_combined_once_per_scenario(self) -> None:
        data = validate(copy.deepcopy(self.mftd3))
        refs = data["scenarios"][0]["display_refs"]
        self.assertEqual(refs[:2], ["M1", "M2"])
        self.assertEqual(len(refs), len(set(refs)))
        self.assertIn("F3", refs)

    def test_captain_handles_ground_contact_without_changing_braking_roles(self) -> None:
        data = validate(copy.deepcopy(self.mftd3))
        start_steps = data["scenarios"][0]["steps"]
        ground_exchange = start_steps[3]["utterances"]
        self.assertEqual([row["speaker"] for row in ground_exchange], ["Captain", "GND", "Captain"])
        self.assertEqual(start_steps[15]["actor"], "Captain")
        braking = data["scenarios"][1]["steps"]
        self.assertEqual(braking[2]["procedure"][1]["actor"], "PF")
        self.assertEqual(braking[4]["procedure"][0]["actor"], "PM")

    def test_empty_mftd2_creates_no_pdf(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "mftd2.pdf"
            result = subprocess.run(
                [sys.executable, str(ROOT / "build_session.py"), str(ROOT / "data/mftd_2.yaml"), "--out", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("SKIPPED mftd-2", result.stdout)
            self.assertFalse(output.exists())

    def test_mftd4_continuation_keeps_cues_with_actions(self) -> None:
        data = validate(copy.deepcopy(self.mftd4))
        fuel = data["scenarios"][0]
        self.assertEqual((fuel["flow_break_at"], fuel["page_break_at"], fuel["continuation_flow_break_at"]), (8, 14, 22))
        fuel["page_break_at"] = 13
        with self.assertRaisesRegex(SessionDataError, "must not separate a condition"):
            validate(data)

    def test_rejects_unexpected_procedure_row_fields(self) -> None:
        data = copy.deepcopy(self.mftd4)
        row = data["scenarios"][1]["steps"][10]["procedure"][1]
        row["EGT)"] = None
        with self.assertRaisesRegex(SessionDataError, "unexpected fields"):
            validate(data)


if __name__ == "__main__":
    unittest.main()
