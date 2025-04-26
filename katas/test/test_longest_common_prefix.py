import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestPrefixCommon(unittest.TestCase):

    def test_empty_array(self):

        self.assertEqual(longest_common_prefix([]), "")

    def test_one_empty_string_array(self):

        self.assertEqual(longest_common_prefix(["","b","b"]), "")

    def test_all_string_same(self):

        self.assertEqual(longest_common_prefix(["test","test","test","test"]), "test")

    def test_no_common_prefix(self):

        self.assertEqual(longest_common_prefix(["test","aa","tbb","t"]), "")

    def test_common_prefix(self):

        self.assertEqual(longest_common_prefix(["abc","abcde","abcdefg","abcd"]), "abc")