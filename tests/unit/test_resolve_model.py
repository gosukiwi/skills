import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'skills/shared/scripts/resolve_model.py'


class ResolverTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / 'project'
        self.home = self.root / 'home'
        self.project.mkdir()
        self.home.mkdir()

    def config(self, text, home=False, legacy=False):
        path = (self.home if home else self.project) / '.agents'
        path.mkdir(exist_ok=True)
        (path / ('gosumode' if legacy else 'gosumode.toml')).write_text(text)

    def run_resolver(self, host='codex', tier='large'):
        return subprocess.run(
            [sys.executable, str(SCRIPT), '--host', host, '--tier', tier],
            cwd=self.project, env={**os.environ, 'HOME': str(self.home)},
            capture_output=True, text=True,
        )

    def resolve(self, **kwargs):
        result = self.run_resolver(**kwargs)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_host_override_preserves_reasoning(self):
        self.config('''[models]
large = "other-model"
[hosts.codex.models.large]
model = "gpt-6.1-sol"
reasoning_effort = "high"
''')
        self.assertEqual(self.resolve(), {'model': 'gpt-6.1-sol', 'reasoning_effort': 'high'})

    def test_codex_tiers_use_default_reasoning(self):
        self.config('[hosts.codex.models]\nsmall="gpt-6-luna"\nmedium="gpt-6.1-terra"\nlarge="gpt-6.1-sol"')
        for tier, model in [('small', 'gpt-6-luna'), ('medium', 'gpt-6.1-terra'), ('large', 'gpt-6.1-sol')]:
            with self.subTest(tier=tier):
                self.assertEqual(self.resolve(tier=tier), {'model': model})

    def test_host_tier_falls_back_to_flat(self):
        self.config('[models]\nlarge="flat"\n[hosts.codex.models]\nsmall="cheap"')
        self.assertEqual(self.resolve(), {'model': 'flat'})

    def test_other_host_mapping_is_not_used(self):
        self.config('[hosts.pi.models]\nlarge="pi-model"')
        self.assertEqual(self.resolve(), {})

    def test_home_fallback(self):
        self.config('[models]\nlarge="home"', home=True)
        self.assertEqual(self.resolve(), {'model': 'home'})

    def test_project_wins_whole(self):
        self.config('[models]\nsmall="project"')
        self.config('[models]\nlarge="home"', home=True)
        self.assertEqual(self.resolve(), {})

    def test_no_config_inherits_on_free_form_hosts(self):
        for host in ('codex', 'pi', 'cursor'):
            with self.subTest(host=host):
                self.assertEqual(self.resolve(host=host), {})

    def test_claude_code_ladder(self):
        for tier, model in [('small', 'haiku'), ('medium', 'sonnet'), ('large', 'opus')]:
            with self.subTest(tier=tier):
                self.assertEqual(self.resolve(host='claude-code', tier=tier), {'model': model})

    def test_empty_project_still_wins(self):
        self.config('')
        self.config('[models]\nlarge="home"', home=True)
        self.assertEqual(self.resolve(), {})

    def test_legacy_project_reports_migration_before_home(self):
        self.config('models:\n  large: old', legacy=True)
        self.config('[models]\nlarge="home"', home=True)
        result = self.run_resolver()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.assertIn('migrate', result.stderr.lower())

    def test_toml_replaces_legacy_in_same_directory(self):
        self.config('old', legacy=True)
        self.config('[models]\nlarge="new"')
        self.assertEqual(self.resolve(), {'model': 'new'})

    def test_invalid_config_errors_without_fallback(self):
        for text in ('[models', '[models]\nlarge=3', '[models.large]\nreasoning_effort="high"',
                     '[models.large]\nmodel="x"\nreasoning_efort="high"',
                     '[models]\nlarge=""', '[models]\nbig="x"',
                     '[hosts.codex]\nmodel="x"'):
            with self.subTest(text=text):
                self.config(text)
                self.config('[models]\nlarge="home"', home=True)
                result = self.run_resolver()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, '')
                self.assertIn('error:', result.stderr)

    def test_explicit_project_root(self):
        self.config('[models]\nlarge="project"')
        result = subprocess.run(
            [sys.executable, str(SCRIPT), '--host', 'codex', '--tier', 'large',
             '--project-root', str(self.project)], cwd=self.home,
            env={**os.environ, 'HOME': str(self.home)}, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {'model': 'project'})


if __name__ == '__main__':
    unittest.main()
