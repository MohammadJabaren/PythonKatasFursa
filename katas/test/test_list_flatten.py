import unittest
from katas.list_flatten import flatten_list

class TestFllatenList(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(flatten_list([]) , [])

    def test_flatten_array(self):
        self.assertEqual(flatten_list([1,2,3,4,5]) , [1,2,3,4,5])

    def test_single_nested_list(self):
        self.assertEqual(flatten_list([1,[2,3],4]) , [1,2,3,4])

    def test_deep_nested_list(self):
        self.assertEqual(flatten_list([1,[2,3,[4,5,[6,7,[8]]]],9,[10,[11,[12]]]]) , [1,2,3,4,5,6,7,8,9,10,11,12])

    def test_deep_empty_nested_list(self):
        self.assertEqual(flatten_list([[[[[[[]]]]], [[[]]]]]) , [])