import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from install import install
from validate import validate


class CollectionTools(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'skills'
        self.skill = self.source / 'example'
        self.skill.mkdir(parents=True)
        (self.skill / 'SKILL.md').write_text('---\nname: example\ndescription: An example skill.\n---\nInstructions.\n')
        self.destination = self.root / 'installed'

    def test_install_copies_references(self):
        (self.skill / 'references').mkdir()
        (self.skill / 'references' / 'guide.md').write_text('Guide')
        install(self.source, self.destination, ['example'])
        self.assertEqual((self.destination / 'example/references/guide.md').read_text(), 'Guide')

    def test_existing_install_preserved(self):
        install(self.source, self.destination, ['example'])
        installed = self.destination / 'example/SKILL.md'
        installed.write_text('User edits')
        with self.assertRaises(ValueError):
            install(self.source, self.destination, ['example'])
        self.assertEqual(installed.read_text(), 'User edits')

    def test_dry_run_and_invalid_selection_do_not_write(self):
        install(self.source, self.destination, ['example'], True)
        self.assertFalse(self.destination.exists())
        with self.assertRaises(ValueError):
            install(self.source, self.destination, ['example', '../outside'])
        self.assertFalse(self.destination.exists())

    def test_reject_symlinks(self):
        (self.skill / 'linked').symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            install(self.source, self.destination, ['example'])

    def test_validation_and_broken_link(self):
        self.assertEqual(validate(self.root), [])
        with (self.skill / 'SKILL.md').open('a') as handle:
            handle.write('[Missing](references/missing.md)\n')
        self.assertTrue(validate(self.root))

    def test_invalid_frontmatter(self):
        (self.skill / 'SKILL.md').write_text('---\nname: wrong-name\ndescription: Example\n---\nText\n')
        self.assertTrue(validate(self.root))


if __name__ == '__main__':
    unittest.main()
