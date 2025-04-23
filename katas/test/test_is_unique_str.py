import unittest
from katas.is_unique_str import is_unique

class TestUniqueStr(unittest.TestCase):
    def test_empty_string(self):

        self.assertEqual(is_unique(""), True)


    def test_unique_string(self):

        self.assertEqual(is_unique("ABC"), True)

    def test_repeated_string(self):

        self.assertEqual(is_unique("ABCDB"), False)

    def test_repeated_insensitive_string(self):

        self.assertEqual(is_unique("AbcB"),False)

    def test_repeated_number(self):

        self.assertEqual(is_unique("123ab1"), False)

    def test_unique_number(self):

        self.assertEqual(is_unique("ABCD1234"), True)