from operations import conjunction, disjunction, implication, inversion, equivalence
import unittest
class TestOperations(unittest.TestCase):
    def test_conjuction(self):
        self.assertEqual(conjunction(0,1), 0)
        self.assertEqual(conjunction(1,1),1)

    def test_disjunction(self):
        self.assertEqual(disjunction(1,0),1)
        self.assertEqual(disjunction(0,0),0)

    def test_implication(self):
        self.assertEqual(implication(1,1),1)
        self.assertEqual(implication(1,0),0)

    def test_inversion(self):
        self.assertEqual(inversion(1),0)

    def test_equivalence(self):
        self.assertEqual(equivalence(0,0),1)
        self.assertEqual(equivalence(1,0),0)
    