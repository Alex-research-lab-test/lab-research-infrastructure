"""Validate Codex metadata without executing project code or touching datasets."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).resolve().parents[1] / "tools" / "check_codex.py"


class CodexMetadataTests(unittest.TestCase):
    def run_check(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, content in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(CHECKER), str(root)],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_accepts_native_agents_and_skill(self):
        result = self.run_check({
            ".codex/agents/reviewer.toml": (
                'name = "reviewer"\ndescription = "Review code"\n'
                'developer_instructions = "Do not edit files."\n'
            ),
            ".agents/skills/reproduce/SKILL.md": (
                "---\nname: reproduce\ndescription: Reproduce a paper\n---\n"
                "Use the author-provided evidence.\n"
            ),
        })
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_missing_skill_description(self):
        result = self.run_check({
            ".agents/skills/reproduce/SKILL.md": "---\nname: reproduce\n---\nRead evidence.\n"
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("description", result.stdout + result.stderr)

    def test_rejects_ineffective_agent_sandbox_setting(self):
        result = self.run_check({
            ".codex/agents/reviewer.toml": (
                'name = "reviewer"\ndescription = "Review"\n'
                'developer_instructions = "Read only"\nsandbox_mode = "read-only"\n'
            ),
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("sandbox_mode", result.stdout + result.stderr)

    def test_rejects_duplicate_agent_names(self):
        agent = 'name = "reviewer"\ndescription = "Review"\ndeveloper_instructions = "Read only"\n'
        result = self.run_check({
            ".codex/agents/one.toml": agent,
            ".codex/agents/two.toml": agent,
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate", result.stdout + result.stderr)

    def test_rejects_malformed_toml(self):
        result = self.run_check({".codex/agents/reviewer.toml": 'name = "unterminated\n'})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reviewer.toml", result.stdout + result.stderr)

    def test_rejects_missing_native_configuration(self):
        result = self.run_check({})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
