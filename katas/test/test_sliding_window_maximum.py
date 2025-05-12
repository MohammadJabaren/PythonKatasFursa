import unittest

from katas.sliding_window_maximum import max_sliding_window

class TestMaxSlideWindow(unittest.TestCase):

    def test_example_case(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3, 3, 5, 5, 6, 7])

    def test_window_size_two(self):
        nums = [9, 11, 3, 4, 8, 7]
        k = 2
        self.assertEqual(max_sliding_window(nums, k), [11, 11, 4, 8, 8])

    def test_window_size_one(self):
        nums = [1, -1]
        k = 1
        self.assertEqual(max_sliding_window(nums, k), [1, -1])

    def test_all_same(self):
        nums = [4, 4, 4, 4]
        k = 2
        self.assertEqual(max_sliding_window(nums, k), [4, 4, 4])

    def test_increasing_array(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3, 4, 5])

    def test_decreasing_array(self):
        nums = [5, 4, 3, 2, 1]
        k = 2
        self.assertEqual(max_sliding_window(nums, k), [5, 4, 3, 2])

    def test_k_equals_len(self):
        nums = [2, 1, 3]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3])

    def test_k_is_zero(self):
        nums = [1, 2, 3]
        k = 0
        self.assertEqual(max_sliding_window(nums, k), [])

    def test_empty_list(self):
        nums = []
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [])