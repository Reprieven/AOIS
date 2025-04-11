import unittest
from BinToDecimal import bin_to_decimal
class TestBinToDecimal(unittest.TestCase):
    def test_convert_int_positive(self):
        bin = [0,1,1,1,0,1,1,0]
        self.assertEqual(bin_to_decimal(bin), 118)