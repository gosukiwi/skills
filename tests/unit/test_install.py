import os
from pathlib import Path
import pty
import select
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'bin/install'


class InstallPromptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name) / 'home'
        self.home.mkdir()

    def run_interactive(self, *inputs):
        master, slave = pty.openpty()
        proc = subprocess.Popen(
            ['/bin/bash', str(SCRIPT)],
            stdin=slave,
            stdout=slave,
            stderr=slave,
            env={**os.environ, 'HOME': str(self.home)},
            preexec_fn=os.setsid,
            close_fds=True,
        )
        os.close(slave)

        out = bytearray()
        idx = 0
        try:
            while True:
                ready, _, _ = select.select([master], [], [], 5.0)
                if not ready:
                    proc.kill()
                    self.fail(f'timed out waiting for prompt; output={out.decode(errors="replace")!r}')
                try:
                    chunk = os.read(master, 4096)
                except OSError:
                    break
                if not chunk:
                    break
                out.extend(chunk)
                text = out.decode('utf-8', errors='replace')
                if idx == 0 and 'Choose ' in text:
                    os.write(master, (inputs[0] + '\n').encode())
                    idx += 1
                elif idx < len(inputs) and text.count('Path: ') >= idx:
                    os.write(master, (inputs[idx] + '\n').encode())
                    idx += 1
        finally:
            os.close(master)

        rc = proc.wait(timeout=5)
        return rc, out.decode('utf-8', errors='replace')

    def installed_targets(self):
        candidates = {
            'claude': self.home / '.claude/skills',
            'agents': self.home / '.agents/skills',
            'antigravity': self.home / '.gemini/antigravity-cli/skills',
            'custom': self.home / 'custom-skills',
        }
        return {name for name, path in candidates.items() if path.exists()}

    def test_empty_defaults_to_claude(self):
        rc, out = self.run_interactive('')
        self.assertEqual(rc, 0, out)
        self.assertEqual(self.installed_targets(), {'claude'})

    def test_comma_and_space_separated_subset(self):
        for choice in ('1,2', '1 2', '1, 2'):
            with self.subTest(choice=choice):
                home = Path(tempfile.mkdtemp(dir=self.temp.name))
                self.home = home
                rc, out = self.run_interactive(choice)
                self.assertEqual(rc, 0, out)
                self.assertEqual(self.installed_targets(), {'claude', 'agents'})

    def test_combines_preset_and_custom_path(self):
        rc, out = self.run_interactive('1,5', '~/custom-skills')
        self.assertEqual(rc, 0, out)
        self.assertEqual(self.installed_targets(), {'claude', 'custom'})

    def test_invalid_choices_fail_without_installing(self):
        for choice in ('1,9', ',', '1,*'):
            with self.subTest(choice=choice):
                rc, out = self.run_interactive(choice)
                self.assertNotEqual(rc, 0, out)
                self.assertEqual(self.installed_targets(), set())


if __name__ == '__main__':
    unittest.main()
