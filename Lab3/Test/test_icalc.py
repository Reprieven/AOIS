import unittest
from ICalcMethod import (add_disjunction, replace_upper_case_with_inversion, 
                        separate_iterations_sdnf, separate_iterations_sknf)

class TestStringOperations(unittest.TestCase):
    def test_add_disjunction(self):
        self.assertEqual(add_disjunction("ab"), "avb")
        self.assertEqual(add_disjunction("a"), "a")
        self.assertEqual(add_disjunction("a(b)"), "av(b)")
        self.assertEqual(add_disjunction("abc"), "avbvc")

    def test_replace_upper_case(self):
        self.assertEqual(replace_upper_case_with_inversion("ABc"), "¬a¬bc")
        self.assertEqual(replace_upper_case_with_inversion("abc"), "abc")
        self.assertEqual(replace_upper_case_with_inversion("A"), "¬a")
        self.assertEqual(replace_upper_case_with_inversion(""), "")

class TestSeparateIterations(unittest.TestCase):
    def test_separate_sdnf(self):
        result = separate_iterations_sdnf("(a&b)|(a&!b)")
        self.assertIn("(ab)\n(ab)", result)
        self.assertIn("a", result.split('\n')[1])  # Проверяем упрощение

    def test_separate_sknf(self):
        result = separate_iterations_sknf("(a|b)&(a|!b)")
        self.assertIn("(ab)\n(ab)", result)
        self.assertIn("a", result.split('\n')[1])  # Проверяем упрощение

if __name__ == '__main__':  # pragma: no cover
    unittest.main()