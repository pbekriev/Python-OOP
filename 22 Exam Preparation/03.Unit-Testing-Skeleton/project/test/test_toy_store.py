import unittest

from project.toy_store import ToyStore



class TestToyStore(unittest.TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_add_toy(self):
        # Test adding a toy to an empty shelf
        result = self.toy_store.add_toy('A', 'Barbie')
        self.assertEqual(result, 'Toy:Barbie placed successfully!')

        # Test adding a toy to a shelf that already has a toy
        with self.assertRaises(Exception):
            self.toy_store.add_toy('A', 'GI Joe')

        # Test adding a toy to a shelf that doesn't exist
        with self.assertRaises(Exception):
            self.toy_store.add_toy('H', 'Lego')

    def test_remove_toy(self):
        # Test removing a toy from a shelf
        self.toy_store.add_toy('B', 'Hot Wheels')
        result = self.toy_store.remove_toy('B', 'Hot Wheels')
        self.assertEqual(result, 'Remove toy:Hot Wheels successfully!')

        # Test removing a toy that doesn't exist in a shelf
        with self.assertRaises(Exception):
            self.toy_store.remove_toy('B', 'Lego')

        # Test removing a toy from a shelf that doesn't exist
        with self.assertRaises(Exception):
            self.toy_store.remove_toy('H', 'Hot Wheels')