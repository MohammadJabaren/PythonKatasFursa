import unittest
from katas.max_storage_capacity import max_storage_area

class TestMaxStorage(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_storage_area([6, 8, 5, 6, 1, 6]), 30)

    def test_basic_case(self):
        self.assertEqual(max_storage_area([1, 1]), 1)

    def test_equal_heights(self):
        self.assertEqual(max_storage_area([4, 4, 4, 4]), 12)

    def test_increasing_hieghts(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 6)

    def test_decreasing_heights(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 6)

    def test_another_example(self):
        self.assertEqual(max_storage_area([2, 3, 10, 5, 7, 8, 9]), 36)

    def test_empty_list(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_single_element(self):
        self.assertEqual(max_storage_area([10]), 0)