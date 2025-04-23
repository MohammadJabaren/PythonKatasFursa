import unittest

from pymacaroons.utils import equals

from katas.list_diff import find_difference

class TestDiffList(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(find_difference([]) , -1)

    def test_array_with_one_element(self):
        self.assertEqual(find_difference([1]) , -1)

    def test_max_negative_min_negative(self):
        self.assertEqual(find_difference([-11 , -4 ,-1 ,-6,-2]) , 10)

    def test_max_positive_min_negative(self):
        self.assertEqual(find_difference([1,5,100,19,-5,-11]) , 111)

    def test_max_positive_min_positive(self):
        self.assertEqual(find_difference([1,5,2,15,20,3,11]) , 19)