import unittest
from Operations.FloatingSum import sum_ieee754

class TestFloatingSum(unittest.TestCase):
    def test_sum_ieee754(self):
        dec1 = 6.75
        dec2 = 7.875
        expected = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(sum_ieee754(dec1,dec2),expected)
