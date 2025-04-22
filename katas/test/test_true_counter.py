import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):
    def test_true_counter(self):

        self.assertEqual(count_true_values([True,True,False,False,False,True,True]), 4)

