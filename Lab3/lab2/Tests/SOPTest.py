import unittest
from SOP import *
from ValueFinder import solve_expression

class TestBinToDecimal(unittest.TestCase):
    def test_make_sdnf(self):
        expression = "(a|b)&!c"
        truth_table = solve_expression(expression)
        sdnf = make_sdnf(truth_table)
        expected_sdnf = "(¬a ∧ b ∧ ¬c) ∨ (a ∧ ¬b ∧ ¬c) ∨ (a ∧ b ∧ ¬c)"
        self.assertEqual(sdnf,expected_sdnf)

    def test_make_numerical_sknf(self):
        expression = "(a|b)&!c"
        truth_table = solve_expression(expression)
        sdnf = make_numerical_sdnf(truth_table)
        expected_sdnf = "(2, 4, 6)∨"
        self.assertEqual(sdnf,expected_sdnf)