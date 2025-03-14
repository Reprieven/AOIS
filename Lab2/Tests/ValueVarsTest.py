import unittest
from ValueVars import all_vars
class TestGetVars(unittest.TestCase):
    def test_vars(self):
        expression = "(a|b)&!c"
        truth_table = all_vars(expression)
        truth_table_expected = {
            "a":[0, 0, 0, 0, 1, 1, 1, 1],
            "b":[0, 0, 1, 1, 0, 0, 1, 1],
            "c":[0, 1, 0, 1, 0, 1, 0, 1]
        }
        self.assertDictEqual(truth_table,truth_table_expected)

    