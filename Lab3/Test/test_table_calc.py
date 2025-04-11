import unittest
from TableCalcMethod import *

class TestHelperFunctions(unittest.TestCase):
    def test_contains_substring(self):
        self.assertTrue(contains_substring("abc", "ab"))
        self.assertTrue(contains_substring("aBc", "aB"))
        self.assertFalse(contains_substring("abc", "ad"))
        self.assertTrue(contains_substring("abc", ""))
        self.assertFalse(contains_substring("", "a"))

    def test_x_count(self):
        self.assertEqual(x_count(["X", "", "X"], ["", "X", "X"]), (2, 2))
        self.assertEqual(x_count(["X", "X", "X"], ["", "", ""]), (3, 0))
        self.assertEqual(x_count([], []), (0, 0))
        self.assertEqual(x_count(["X"], ["X"]), (1, 1))

    def test_arrays_contain(self):
        self.assertEqual(arrays_contain(["X", "X"], ["X", ""]), ["X", ""])
        self.assertIsNone(arrays_contain(["", "X"], ["X", ""]))
        self.assertEqual(arrays_contain(["X"], ["X"]), ["X"])
        self.assertEqual(arrays_contain([""], ["X"]), [""])

    def test_remove_unnecessary(self):
        input_dict = {"a": [1], "b": [2], "c": [3]}
        self.assertEqual(remove_unnecessary(input_dict, ["a", "b"]), {"a": [1], "b": [2]})
        self.assertEqual(remove_unnecessary(input_dict, []), {})
        self.assertEqual(remove_unnecessary({}, ["a"]), {})
        self.assertEqual(remove_unnecessary(input_dict, ["a", "b", "c"]), input_dict)

class TestTableCalculations(unittest.TestCase):

    def test_minimal_set_cover(self):
        test_cases = [
            ({"a": ["X", "X"]}, ["a"]),
            ({"a": ["X", ""], "b": ["", "X"]}, ["a", "b"]),
            ({"a": ["X", "X"], "b": ["", "X"]}, ["a"])
        ]
        
        for table, expected in test_cases:
            with self.subTest(table=table):
                result = minimal_set_cover(table)
                self.assertEqual(len(result), len(expected))
                for item in expected:
                    self.assertIn(item, result)

    def test_table_calc_sdnf(self):
        result = table_calc_sdnf("(a&b)|(a&!b)")
        self.assertEqual(len(result), 1)

    def test_table_calc_sknf(self):
        result = table_calc_sknf("(a|b)&(a|!b)")
        self.assertEqual(len(result), 1)


    def test_edge_cases(self):
        empty_sdnf = form_table_sdnf("")
        empty_sknf = form_table_sknf("")
        self.assertEqual(empty_sdnf, {})
        self.assertEqual(empty_sknf, {})
        no_simplify = table_calc_sdnf("(a&b)|(!a&!b)")
        self.assertEqual(len(no_simplify), 1)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()