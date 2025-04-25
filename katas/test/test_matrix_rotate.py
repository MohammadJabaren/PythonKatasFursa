import unittest
from katas.matrix_rotate import rotate_matrix

class TestRotateMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(rotate_matrix([]),[])

    def test_1x1_matrix(self):
        self.assertEqual(rotate_matrix([[1]]), [[1]])

    def test_3x3_matrix(self):
        input_matrix = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
        expected_output = [[7, 4, 1],
                           [8, 5, 2],
                           [9, 6, 3]]
        self.assertEqual(rotate_matrix(input_matrix),expected_output)
    def test_4x4_matrix(self):
        input_matrix = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]]
        expected_output = [[13, 9, 5, 1],
                           [14, 10, 6, 2],
                           [15, 11, 7, 3],
                           [16, 12, 8, 4]]
        self.assertEqual(rotate_matrix(input_matrix),expected_output)

