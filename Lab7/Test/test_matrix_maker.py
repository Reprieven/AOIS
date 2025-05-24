from matrix_maker import make_matrix, make_matrix_col
import unittest
class TestMakeMatrix(unittest.TestCase):
    def test_make_matrix(self):
        matrix = make_matrix(4)
        self.assertEqual(len(matrix),4)
        self.assertEqual(len(matrix[0]),4)
    
    def test_make_matrix_col(self):
        matrix = [[1, 0, 1, 1],
                  [0, 1, 1, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]
        matrix_col = [[1,0,0,0],
                      [0,1,0,0],
                      [1,1,0,0],
                      [1,1,1,0]]
        self.assertListEqual(make_matrix_col(matrix), matrix_col)
    