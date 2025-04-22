import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):
    def test_true_counter(self):

        self.assertEqual(count_true_values([True,True,False,False,False,True,True]), 4)


    def test_empty_array(self):

        self.assertEqual(count_true_values([]), 0)

    def test_full_true_counter(self):

        self.assertEqual(count_true_values([True,True,True]), 3)

    def test_zero_true_counter(self):

        self.assertEqual(count_true_values([False,False]), 0)