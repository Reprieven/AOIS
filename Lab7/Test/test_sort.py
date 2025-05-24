import unittest
from typing import List
from matrix_maker import make_matrix_col
from find_by_index import find_word
from sort import compare_words, sort

class TestBinaryMatrixSorting(unittest.TestCase):
    
    def test_compare_words_binary(self):
        self.assertTrue(compare_words([0, 0, 1], [0, 1, 0]))  
        self.assertFalse(compare_words([0, 1, 0], [0, 0, 1]))  
        self.assertTrue(compare_words([0, 0, 0], [0, 0, 1]))   
        self.assertFalse(compare_words([1, 0, 0], [0, 1, 1])) 
        self.assertFalse(compare_words([1, 1, 1], [1, 1, 1]))  
        
    def test_sort_all_zeros(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = sort(matrix)
        self.assertEqual(result, matrix) 
        
    def test_sort_all_ones(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = sort(matrix)
        self.assertEqual(result, matrix)  