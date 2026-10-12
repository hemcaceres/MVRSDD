"""Check fixture isolation and preservation, not skill behavior or discovery."""

import hashlib
import tempfile
import unittest
from pathlib import Path

from prepare_sdd_cases import SOURCE, prepare


def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class EvaluationPreparationTests(unittest.TestCase):
    def setUp(self):
        # Keep temporary evaluations inside the workspace for restricted environments.
        self.test_root = SOURCE / ".harness-test-sdd-unit"
        self.test_root.mkdir(exist_ok=True)

    def test_inputs_are_portable_and_isolated(self):
        with tempfile.TemporaryDirectory(dir=self.test_root) as directory:
            output = Path(directory) / "cases"
            cases = prepare(output)
            for case in cases:
                self.assertFalse(Path(case["workspace"]).is_absolute())
                self.assertFalse(Path(case["skill"]).is_absolute())
                self.assertTrue((output / case["workspace"]).is_dir())
                self.assertTrue((output / case["skill"]).is_file())
            self.assertEqual(
                (output / "approved/.agents/skills/sdd/SKILL.md").read_bytes(),
                (SOURCE / ".agents/skills/sdd/SKILL.md").read_bytes(),
            )
            self.assertEqual(
                (output / "approved/.claude/skills/sdd/SKILL.md").read_bytes(),
                (SOURCE / ".claude/skills/sdd/SKILL.md").read_bytes(),
            )
            # Evaluations are independent; a mutation cannot affect another case or source.
            original = (output / "unapproved/demo.py").read_bytes()
            (output / "approved/demo.py").write_text("changed\n", encoding="utf-8")
            self.assertEqual((output / "unapproved/demo.py").read_bytes(), original)
            self.assertFalse((output / "missing-harness/.harness").exists())
            # The copied harness README references ../VERSION; keep it resolvable.
            self.assertEqual((output / "approved/VERSION").read_bytes(),
                             (SOURCE / "VERSION").read_bytes())
            self.assertNotEqual(
                (output / "external-project/specs/index.md").read_bytes(),
                (output / "external-skill/specs/index.md").read_bytes(),
            )

    def test_existing_evaluation_is_preserved(self):
        with tempfile.TemporaryDirectory(dir=self.test_root) as directory:
            output = Path(directory) / "cases"
            prepare(output)
            (output / "approved/demo.py").write_text("user result\n", encoding="utf-8")
            before = hashes(output)
            with self.assertRaises(FileExistsError):
                prepare(output)
            self.assertEqual(hashes(output), before)


if __name__ == "__main__":
    unittest.main()
