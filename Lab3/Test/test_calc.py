import unittest
from Calc import *

class TestCountMatches(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(count_matches("abc", "abc"), 3)
    
    def test_different_strings(self):
        self.assertEqual(count_matches("abc", "def"), 3)
    
    def test_two_match(self):
        self.assertEqual(count_matches("abc", "Abc"), 2)
    
    def test_length(self):
        self.assertEqual(count_matches("abcd", "Abc"), -1)

class TestAdhesion(unittest.TestCase):
    def test_full_match(self):
        self.assertEqual(adhesion("abc", "abc"), "abc")
    
    def test_partial_match(self):
        self.assertEqual(adhesion("abc", "aBc"), "ac")
    
    def test_no_match(self):
        self.assertEqual(adhesion("abc", "def"), "")

class TestDeleteAdhesioned(unittest.TestCase):
    def test_filtering(self):
        input_dict = {"a": 0, "b": 1, "c": 0}
        expected = {"a": 0, "c": 0}
        self.assertEqual(delete_adhesioned(input_dict), expected)
    
    def test_empty_result(self):
        self.assertEqual(delete_adhesioned({"a": 1, "b": 2}), {})

class TestCalcIteration(unittest.TestCase):
    def test_simple_case(self):
        parsed = {"ab": 0, "aB": 0}
        result, ads = calc_iteration(parsed)
        self.assertEqual(ads, 1)
        self.assertIn("a", result)
    
    def test_no_adhesion(self):
        parsed = {"ab": 0, "cd": 0}
        result, ads = calc_iteration(parsed)
        self.assertEqual(ads, 0)

class TestCalcSDNF(unittest.TestCase):
    def test_simple_disjunction(self):
        """Проверка простой дизъюнкции"""
        expression = "(a&b)|(a&!b)"
        result = calc_SDNF(expression)
        self.assertGreaterEqual(len(result), 2)

    def test_no_adhesion_case(self):
        """Случай без возможности склеивания"""
        expression = "(a&b)|(!a&!b)"
        result = calc_SDNF(expression)
        self.assertEqual(len(result), 2)

class TestCalcSKNF(unittest.TestCase):
    def test_simple_conjunction(self):
        """Проверка простой конъюнкции"""
        expression = "(a|b)&(a|!b)"
        result = calc_SKNF(expression)
        self.assertGreaterEqual(len(result), 2)

    def test_no_adhesion_case(self):
        """Случай без возможности склеивания"""
        expression = "(a|b)&(!a|!b)"
        result = calc_SKNF(expression)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()