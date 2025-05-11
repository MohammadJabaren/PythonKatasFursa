import unittest

from katas.requirements_coverage import select_minimal_test_cases

class TestMinCases(unittest.TestCase):

    def test_example_case(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue([2,3])

    def test_single_test_case_covers_all(self):
        test_cases = [
            [1, 2, 3, 4, 5],
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

    def test_each_requirement_unique(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result ,[0, 1, 2, 3, 4])

    def test_multiple_minimal_solutions(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(len(result), 2)
        self.assertTrue([0, 1] == result or [1, 2] == result or [0, 2] == result)

    def test_empty_input(self):
        test_cases = []
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [])