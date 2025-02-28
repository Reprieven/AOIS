import unittest
from Operations.Division import division
class DivisionTest(unittest.TestCase):
    def test_division_positive(self):
        dec1 = 103
        dec2 = 31
        expected = 3.3125
        self.assertEqual(division(dec1,dec2),expected)
    
    def test_division_zero(self):
        dec1 = 103
        dec2 = 0
        expected = "Inf"
        self.assertEqual(division(dec1,dec2),expected)
    
    def test_division_negative(self):
        dec1 = 103
        dec2 = -31
        expected = -3.3125
        self.assertEqual(division(dec1,dec2),expected)
    
    def test_division_double_negative(self):
        dec1 = -103
        dec2 = -31
        expected = 3.3125
        self.assertEqual(division(dec1,dec2),expected)
    
    