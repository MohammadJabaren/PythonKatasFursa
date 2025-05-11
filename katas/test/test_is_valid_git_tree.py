import unittest
from katas.is_valid_git_tree import is_valid_git_tree

class TestIsValidGitTree(unittest.TestCase):

    def test_valid_tree(self):
        tree = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_cycle(self):
        tree = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_multiple_roots(self):
        tree = {
            "A": ["B"],
            "C": ["D"],
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_disconnected_node(self):
        tree = {
            "A": ["B"],
            "B": [],
            "C": [],  # C is disconnected
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_single_node(self):
        tree = {
            "A": []
        }
        self.assertTrue(is_valid_git_tree(tree))