import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""),0)

    def test_numbers_string(self):
        self.assertEqual(sum_of_digits("12345631"), 25)

    def test_mix_string(self):
        self.assertEqual(sum_of_digits("1Aca!23s5"), 11)

    def test_non_number_string(self):
        self.assertEqual(sum_of_digits("asdafA)$%##ddf"), 0)

