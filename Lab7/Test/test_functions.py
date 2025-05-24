from functions import f11, f9, f6, f4
import unittest
class TestFunctions(unittest.TestCase):
    def test_f11(self):
        first_row = [0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0]
        second_row = [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0]
        expected = [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
        self.assertListEqual(expected, f11(first_row,second_row))
    def test_f9(self):
        first_row = [0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0]
        second_row = [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0]
        expected = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1]
        self.assertListEqual(expected, f9(first_row,second_row))
    def test_f6(self):
        first_row = [0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0]
        second_row = [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0]
        expected = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0]
        self.assertListEqual(expected, f6(first_row,second_row))
    def test_f4(self):
        first_row = [0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0]
        second_row = [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0]
        expected = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertListEqual(expected, f4(first_row,second_row))
