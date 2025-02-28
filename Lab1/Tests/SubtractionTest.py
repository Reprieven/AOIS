import unittest
from Operations.Subtraction import subtraction
class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        dec1 = 56
        dec2 = 78
        expected = -22
        self.assertEqual(subtraction(56,78),expected)
        