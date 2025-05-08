import unittest
from src.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_find_v(self):
        table = HashTable(4)
        term = "Алгебра"
        v_value = table.find_v(term)
        self.assertEqual(v_value, 12)

    def test_hash(self):
        table = HashTable(4)
        term = "Алгебра"
        hash = table.hash(term)
        self.assertEqual(hash, 0)
    
    def test_insert(self):
        table = HashTable(4)
        term = "Алгебра"
        definition = " Часть математики"
        table.insert(term, definition)
        row = table.table[0]
        self.assertEqual(term, row.key)
        self.assertEqual(definition, row.value)
    
    def test_search(self):
        table = HashTable(4)
        term = "Алгебра"
        definition = "Часть математики"
        table.insert(term, definition)
        definition_find = table.search(term)
        self.assertEqual(definition, definition_find)
    
    def test_search_collision(self):
        table = HashTable(4)
        term1 = "Теорема Виета"
        definition1 = "Teорема Виета..."

        term2 = "Теорема чисел"
        definition2 = "Теорема чисел..."

        table.insert(term1, definition1)
        table.insert(term2, definition2)

        find1 = table.search(term1)
        self.assertEqual(find1, definition1)

        find2 = table.search(term2)
        self.assertEqual(find2, definition2)


    def test_delete(self):
        table = HashTable(4)
        term = "Алгебра"
        definition = " Часть математики"
        table.insert(term, definition)
        table.delete(term)
        self.assertEqual(table.table[0], None)
    
    

