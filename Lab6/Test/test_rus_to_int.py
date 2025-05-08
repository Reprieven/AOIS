import unittest
from src.rus_to_int import rus_to_int

class TestRusToInt(unittest.TestCase):
    def test_rus_to_int_first(self):
        char = 'а'
        int_char = rus_to_int(char)
        self.assertEqual(0, int_char)

    def test_rus_to_int_mid(self):
        char = 'п'
        int_char = rus_to_int(char)
        self.assertEqual(16, int_char)

    
    

        