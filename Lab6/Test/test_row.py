import unittest
from src.row import Row

class TestRow(unittest.TestCase):
    def test_row_init(self):
        row = Row("Алгебра", "Часть математики")
        self.assertEqual(row.key, "Алгебра")
        self.assertEqual(row.value, "Часть математики")
        