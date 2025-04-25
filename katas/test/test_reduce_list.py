import unittest
from katas.reduce_list import reduce_array

class TestReduceList(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(reduce_array([]),[])

    def test_array_with_one_element(self):
        self.assertEqual(reduce_array([1]), [1])

    def test_number_array1(self):
        self.assertEqual(reduce_array([1,2,3,4,5,6,7,8,9]), [1,1,1,1,1,1,1,1,1])

    def test_number_array2(self):
        self.assertEqual(reduce_array([5,4,3,2]), [5,-1,-1,-1])

    def test_number_array3(self):
        self.assertEqual(reduce_array([10,12,20,1]), [10,2,8,-19])

