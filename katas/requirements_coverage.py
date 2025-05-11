from itertools import combinations
from typing import List


def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    """
    In software testing, it's often required to select a minimal set of test cases that cover all the requirements.
    You are given a set of test cases and their associated covered requirements.
    Your task is to select the minimal subset of test cases such that all requirements are covered.

    For example, you have the following test cases and requirements they cover:

    test_cases = [
        [1, 2, 3],   # Test case 0 covers requirements 1, 2, 3
        [1, 4],      # Test case 1 covers requirements 1, 4
        [2, 3, 4],   # Test case 2 covers requirements 2, 3, 4
        [1, 5],      # Test case 3 covers requirements 1, 5
        [3, 5]       # Test case 4 covers requirements 3, 5
    ]

    Args:
        test_cases: a list of test cases, where each test case is a list of requirements it covers.
                    Assume each requirement is covered by at least one test case.

    Returns:
        A list of indices of the minimal subset of test cases that covers all requirements
    """
    req = set(r for test in test_cases for r in test)

    for number_of_comp in range(1,len(test_cases)+1):
        for comb in combinations(range(len(test_cases)),number_of_comp):
            checkset = set()
            for i in comb:
                checkset.update(test_cases[i])
            if checkset == req:
                return list(comb)
    return []


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
