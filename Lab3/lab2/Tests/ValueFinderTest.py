import unittest
from ValueFinder import *

class TestOperations(unittest.TestCase):
    def test_max_precedence(self):
        expression = "!a&b|c"
        self.assertEqual(max_precedence(expression), 3)
    
    def test_apply_operator(self):
        first = 1
        second = 0 
        operator = "|"
        self.assertEqual(apply_operator(operator,first,second), 1)
    
    def test_find_value(self):
        expression = ["!",0,"|",1,"&",0,">",1]
        self.assertEqual(find_value(expression),1)
    
    def test_change_to_int(self):
        expression = "(a|b)&!c"
        truth_table = all_vars(expression)
        expression_parsed = parser(expression)
        expression_parsed_int = change_to_int(expression_parsed,truth_table,0)
        self.assertEqual(expression_parsed_int, ["(",0,"|",0,")","&","!",0])
    
    def test_process_brackets(self):
        expression = "(a|b)&!c"
        truth_table = all_vars(expression)
        expression_parsed = parser(expression)
        expression_parsed_int = change_to_int(expression_parsed,truth_table,0)
        expression_parsed_int = process_brackets(expression_parsed_int)
        self.assertEqual(expression_parsed_int,[0,"&","!",0])
    
    def test_solve_for_row(self):
        expression = "(a|b)&!c"
        truth_table = all_vars(expression)
        expression_parsed = parser(expression)
        solution = solve_for_row(expression_parsed,truth_table,0)
        self.assertEqual(solution,0)
    
    def test_solve_expression(self):
        expression = "(a|b)&!c"
        solution = solve_expression(expression)
        expected = {
            "a": [0, 0, 0, 0, 1, 1, 1, 1],
            "b": [0, 0, 1, 1, 0, 0, 1, 1],
            "c":[0, 1, 0, 1, 0, 1, 0, 1],
            "res": [0, 0, 1, 0, 1, 0, 1, 0]
        }
        self.assertDictEqual(solution,expected)