import unittest
from katas.semantic_version_comparator import compare_versions

class TestCompareVersion(unittest.TestCase):

    def test_version_less(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("2.3.4", "2.4.0"), -1)
        self.assertEqual(compare_versions("0.9", "1.0.0"), -1)
        self.assertEqual(compare_versions("1.2", "1.2.1"), -1)

    def test_version_greater(self):
        self.assertEqual(compare_versions("2.1.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.10.0.0.0.0.0", "1.2.0"), 1)
        self.assertEqual(compare_versions("3.0", "2.9.9.0.0.0.0"), 1)

    def test_version_equal(self):
        self.assertEqual(compare_versions("1.2.3", "1.2.3"), 0)
        self.assertEqual(compare_versions("1.2", "1.2.0"), 0)
        self.assertEqual(compare_versions("1.0.0", "1.0"), 0)
        self.assertEqual(compare_versions("0.0.0", "0"), 0)

