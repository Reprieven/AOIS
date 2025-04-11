import unittest
from Parse import *

class TestSimplifyInversion(unittest.TestCase):
    def test_simpify(self):
        expression = "!!!!!a&!!b"
        self.assertEqual(simplify_inversion(expression), "!a&b")

class TestParser(unittest.TestCase):
    def test_parser(self):
        expression = "!a -> b ~ c & d | e"
        self.assertEqual(parser(expression), ['!', 'a', '>', 'b', '~', 'c', '&', 'd', '|', 'e'])
        