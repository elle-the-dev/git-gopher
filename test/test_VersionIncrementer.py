import unittest
from git_gopher.VersionIncrementer import VersionIncrementer

class TestVersionIncrementer(unittest.TestCase):
    def test_major(self):
        version = 'v2.3.4'
        version_incrementer = VersionIncrementer()
        new_version = version_incrementer.major(version)
        self.assertEqual(new_version, 'v3.0.0')

    def test_minor(self):
        version = '2.3.4'
        version_incrementer = VersionIncrementer()
        new_version = version_incrementer.minor(version)
        self.assertEqual(new_version, '2.4.0')

    def test_patch(self):
        version = '2.3.4'
        version_incrementer = VersionIncrementer()
        new_version = version_incrementer.patch(version)
        self.assertEqual(new_version, '2.3.5')
