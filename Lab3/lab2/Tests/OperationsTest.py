import unittest
from Operations import *
class TestConjunction(unittest.TestCase):
    def test_conjunction_true(self):
        first = 1
        second = 1
        self.assertEqual(conjunction(first,second), 1)

    def test_conjunction_false(self):
        first = 1
        second = 0
        self.assertEqual(conjunction(first,second), 0)


class TestDisjunction(unittest.TestCase):
    def test_disjunction_true(self):
        first = 1
        second = 0
        self.assertEqual(disjunction(first,second), 1)

    def test_disjunction_false(self):
        first = 0
        second = 0
        self.assertEqual(disjunction(first,second), 0)
    
class TestImplication(unittest.TestCase):
    def test_implication_true(self):
        first = 1
        second = 1
        self.assertEqual(implication(first,second), 1)

    def test_implication_false(self):
        first = 1
        second = 0
        self.assertEqual(implication(first,second), 0)

class TestEquivalence(unittest.TestCase):
    def test_equivalence_true(self):
        first = 1
        second = 1
        self.assertEqual(equivalence(first,second), 1)

    def test_equivalence_false(self):
        first = 1
        second = 0
        self.assertEqual(equivalence(first,second), 0)

class TestInversion(unittest.TestCase):
    def test_inversion_true(self):
        first = 0
        self.assertEqual(inversion(first), 1)

    def test_inversion_false(self):
        first = 1
        self.assertEqual(inversion(first), 0)

class TestPrecedence(unittest.TestCase):
    def test_precedence_success(self):
        self.assertEqual(precedence('!'),3)
    
    def test_precedence_error(self):
        self.assertEqual(precedence('a'),-1)

    






    
