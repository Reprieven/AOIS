import unittest
from Operations.SumBinary import sum_binary
from Operations.Sum import sum

class TestSumBinary(unittest.TestCase):
    def test_sum_positive(self):
        bin1 = [0, 0, 0, 1, 0, 0, 1, 0] #18
        bin2 = [0, 0, 0, 0, 0, 0, 1, 0] #2
        expected = [0, 0, 0, 1, 0, 1, 0, 0] #20
        self.assertEqual(sum_binary(bin1,bin2),expected)

    def test_sum_negative(self):
        bin1 = [1, 1, 1, 0, 1, 1, 0, 0] #-20
        bin2 = [1, 0, 0, 1, 1, 0, 0, 0] #-104
        expected = [1, 0, 0, 0, 0, 1, 0, 0] #-124
        self.assertEqual(sum_binary(bin1,bin2),expected)

class TestSum(unittest.TestCase):
    def test_sum_positive(self):
        dec1 = 18
        dec2 = 2
        expected = 20
        self.assertEqual(sum(dec1,dec2),expected)

    def test_sum_negative(self):
        dec1 = -20
        dec2 = -104
        expected = -124
        self.assertEqual(sum(dec1,dec2),expected)