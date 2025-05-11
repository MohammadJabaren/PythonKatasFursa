import unittest
from katas.test_case_grouping import group_test_cases


def validate_grouping(test, sizes, groups):
    covered_indices = []

    for group in groups:
        expected_size = sizes[group[0]]

        # All in the group have the same requirement
        if not all(sizes[idx] == expected_size for idx in group):
            test.fail(f"Invalid group: not all test cases in {group} require size {expected_size}")

        # Group is the correct size
        if len(group) != expected_size:
            test.fail(f"Invalid group size: group {group} has size {len(group)}, expected {expected_size}")

        covered_indices.extend(group)

    # Check full coverage without duplicates
    if sorted(covered_indices) != list(range(len(sizes))):
        test.fail("Invalid: Not all test cases are covered exactly once")

class TestCaseGrouping(unittest.TestCase):

    def test_example_case(self):
        sizes = [1, 2, 3, 3, 3, 2]
        result = group_test_cases(sizes)
        validate_grouping(self, sizes, result)

    def test_simple_case(self):
        sizes = [2, 2, 1, 1]
        result = group_test_cases(sizes)
        validate_grouping(self, sizes, result)

    def test_all_singles(self):
        sizes = [1, 1, 1]
        result = group_test_cases(sizes)
        validate_grouping(self, sizes, result)

    def test_large_group(self):
        sizes = [4, 4, 4, 4]
        result = group_test_cases(sizes)
        validate_grouping(self, sizes, result)

    def test_invalid_input(self):
        sizes = [2, 2, 2]  # Not enough to form complete groups of 2
        with self.assertRaises(ValueError):
            group_test_cases(sizes)

    def test_mixed_valid_input(self):
        sizes = [3, 3, 3, 1, 2, 2]
        result = group_test_cases(sizes)
        validate_grouping(self, sizes, result)
