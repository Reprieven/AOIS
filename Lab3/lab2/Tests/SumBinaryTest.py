import unittest
from SumBinary import sum_binary
class TestSumBinary(unittest.TestCase):
    def test_sum_positive(self):
        bin1 = [0, 0, 0, 1, 0, 0, 1, 0] #18
        bin2 = [0, 0, 0, 0, 0, 0, 1, 0] #2
        expected = [0, 0, 0, 1, 0, 1, 0, 0] #20
        self.assertEqual(sum_binary(bin1,bin2,8),expected)
