import unittest
from CalcCheck import *

class TestMakeStrings(unittest.TestCase):
    def test_make_str_sdnf(self):
        cases = [
            ({'ab': 0}, "(a&b)"),
            ({'aB': 0}, "(a&!b)"),
            ({'ab': 0, 'aB': 0}, "(a&b)|(a&!b)"),
            ({'abc': 0}, "(a&b&c)"),
            ({}, "")
        ]
        for input_dict, expected in cases:
            with self.subTest(input=input_dict):
                self.assertEqual(make_str_sdnf(input_dict), expected)

    def test_make_str_sknf(self):
        cases = [
            ({'ab': 0}, "(a|b)"),
            ({'aB': 0}, "(a|!b)"),
            ({'ab': 0, 'aB': 0}, "(a|b)&(a|!b)"),
            ({'abc': 0}, "(a|b|c)"),
            ({}, "")
        ]
        for input_dict, expected in cases:
            with self.subTest(input=input_dict):
                self.assertEqual(make_str_sknf(input_dict), expected)

class TestDeleteUnnecessary(unittest.TestCase):
    def test_delete_unnecessary_sdnf(self):
        cases = [
            ({'ab': 0}, {'ab': 0}),
            ({'ab': 0, 'aB': 0}, {'ab': 0, 'aB': 0}),
            ({'a': 0}, {'a': 0})
        ]
        for input_dict, expected in cases:
            with self.subTest(input=input_dict):
                self.assertEqual(delete_unnecessary_sdnf(input_dict), expected)

    def test_delete_unnecessary_sknf(self):
        cases = [
            ({'ab': 0}, {'ab': 0}),
            ({'ab': 0, 'aB': 0}, {'ab': 0, 'aB': 0}),
            ({'a': 0}, {'a': 0})
        ]
        for input_dict, expected in cases:
            with self.subTest(input=input_dict):
                self.assertEqual(delete_unnecessary_sknf(input_dict), expected)

    def test_delete_redundant_terms(self):
        input_dict = {
            'ab': 0,
            'aB': 0,    
            'cd': 0     
        }
        result = delete_unnecessary_sdnf(input_dict)
        self.assertIn('ab', result)
        self.assertIn('aB', result)
        self.assertIn('cd', result)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()