from find_by_index import find_word, find_address_col
import unittest
class TestFind(unittest.TestCase):
    def test_find_word(self):
        matrix = [[1, 0, 1, 1],
                  [0, 1, 1, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]
        self.assertListEqual(find_word(matrix, 0), [1,0,0,0])
        self.assertListEqual(find_word(matrix, 2), [0,0,1,1])

    def test_make_matrix_col(self):
        matrix = [[1, 0, 1, 1],
                  [0, 1, 1, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]
        self.assertListEqual(find_address_col(matrix, 0), [1,1,0,0])
        self.assertListEqual(find_address_col(matrix, 2), [0,0,1,1])
    