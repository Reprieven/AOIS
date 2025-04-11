import unittest
from POS import *
from ValueFinder import solve_expression

class TestBinToDecimal(unittest.TestCase):
    def test_make_sknf(self):
        expression = "(a|b)&!c"
        truth_table = solve_expression(expression)
        sknf = make_sknf(truth_table)
        expected_sknf = "(a ∨ b ∨ c) ∧ (a ∨ b ∨ ¬c) ∧ (a ∨ ¬b ∨ ¬c) ∧ (¬a ∨ b ∨ ¬c) ∧ (¬a ∨ ¬b ∨ ¬c)"
        self.assertEqual(sknf,expected_sknf)

    def test_make_numerical_sknf(self):
        expression = "(a|b)&!c"
        truth_table = solve_expression(expression)
        sknf = make_numerical_sknf(truth_table)
        expected_sknf = "(0, 1, 3, 5, 7)∧"
        self.assertEqual(sknf,expected_sknf)
