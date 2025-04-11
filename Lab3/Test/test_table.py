import unittest
from TableMethod import *

class TestKarnaughMapFunctions(unittest.TestCase):
    def test_gray_code(self):
        self.assertEqual(gray_code(0), 0)
        self.assertEqual(gray_code(1), 1)
        self.assertEqual(gray_code(2), 3)
        self.assertEqual(gray_code(3), 2)

    def test_gray_code_to_list(self):
        self.assertEqual(gray_code_to_list(0, 2), [0, 0])
        self.assertEqual(gray_code_to_list(1, 2), [0, 1])
        self.assertEqual(gray_code_to_list(2, 2), [1, 1])

    def test_make_karno_table(self):
        table = make_karno_table("(a&b)|(!a&!b)")
        self.assertEqual(len(table), 2)
        self.assertEqual(len(table[0]), 2)

    def test_reverse_karno(self):
        original = [[0, 1], [1, 0]]
        reversed = reverse_karno(original)
        self.assertEqual(reversed, [[1, 0], [0, 1]])

class TestSplitFunctions(unittest.TestCase):
    def test_split_columns(self):
        karno = [[0, 1], [1, 0]]
        cols = split_columns_with_coordinates(karno)
        self.assertEqual(len(cols), 2)

    def test_split_rows(self):
        karno = [[0, 1], [1, 0]]
        rows = split_rows_with_coordinates(karno)
        self.assertEqual(len(rows), 2)

class TestCompoundFunctions(unittest.TestCase):
    def test_compound_cols_depth(self):
        cols = [([1], (0, 0)), ([1], (1, 0))]
        compounded = compound_cols_depth(cols)
        self.assertGreater(len(compounded), len(cols))

    def test_compound_rows_width(self):
        rows = [([1], (0, 0)), ([1], (0, 1))]
        compounded = compound_rows_width(rows)
        self.assertGreaterEqual(len(compounded), len(rows))

    def test_find_separate_cover(self):
        karno = [[1, 0], [0, 1]]
        cols = [([1], (0, 0))]
        rows = [([1], (1, 1))]
        cover = find_separate_cover(karno, cols, rows)
        self.assertEqual(len(cover[0]) + len(cover[1]), 2)

class TestMinimizationFunctions(unittest.TestCase):
    def test_analyze_kmap_group(self):
        group = [(0, 0), (1, 1)]
        result = analyze_kmap_group(group, 'a', 'b')
        self.assertFalse('a' in result or 'b' in result)

    def test_get_minimal_dnf(self):
        groups = [[(0, 0), (0, 1)]]
        result = get_minimal_dnf(groups, 'a', 'b')
        self.assertTrue('a' in result or 'b' in result)

class TestMainFunctions(unittest.TestCase):
    def test_make_sdnf(self):
        result = make_sdnf("(a&b)|(!a&!b)", ['a', 'b'])
        self.assertTrue('a' in result or 'b' in result)

    def test_make_sknf(self):
        result = make_sknf("(a|b)&(!a|!b)", ['a', 'b'])
        self.assertTrue('a' in result or 'b' in result)

class TestGrayCodeToList(unittest.TestCase):
    def test_zero_input(self):
        result = gray_code_to_list(0, 1)
        self.assertEqual(result, [0])
    
    def test_single_bit_values(self):
        result = gray_code_to_list(1, 2)
        self.assertEqual(result, [0, 1])

if __name__ == '__main__':  #pragma: no cover
    unittest.main()