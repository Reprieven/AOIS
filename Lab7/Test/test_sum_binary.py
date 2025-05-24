from sum_binary import sum_binary
import unittest
class TestSumBinary(unittest.TestCase):
    def test_sum_binary(self):
        first_num = [0,1,1,1]
        second_num = [1,0,0,1]
        expected = [1,0,0,0,0]