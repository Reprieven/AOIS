import unittest
from Operations.Multiplication import multiplication
class TestMultiplication(unittest.TestCase):
    def test_multiplication_positive(self):
        dec1 = 23
        dec2 = 104
        expected = 2392
        self.assertEqual(multiplication(dec1,dec2),expected)
    
    def test_multiplication_null(self):
        dec1 = 0
        dec2 = 104
        expected = 0
        self.assertEqual(multiplication(dec1,dec2),expected)
    
    def test_multiplication_negative(self):
        dec1 = -23
        dec2 = 104
        expected = -2392
        self.assertEqual(multiplication(dec1,dec2),expected)
    
    def test_multiplication_double_negative(self):
        dec1 = -23
        dec2 = -104
        expected = 2392
        self.assertEqual(multiplication(dec1,dec2),expected)
    
    