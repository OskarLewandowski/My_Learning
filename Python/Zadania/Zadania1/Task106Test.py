#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 106

Napisz funkcję `penultimate(list, otherwise)` zwracającą przedostatni
element listy `list`. Jeśli lista jest pusta lub jednoelementowa,
należy zwrócić wartość `otherwise`.

NAME: penultimate
PARAMS: list, obj
RETURN: obj
POINTS: 1
"""

import unittest
from Task106 import penultimate

class Task106Test(unittest.TestCase):
    """Testy do zadania 106"""

    def test_sequence(self):
        """Prosty test."""
        self.assertEqual(
            penultimate([1, 2, 3, 4, 5, 6], 'blabla'),
            5)

    def test_empty(self):
        """Test na pustej liście."""
        self.assertEqual(
            penultimate([], 'DO NOT WANT'),
            'DO NOT WANT')

    def test_singleton(self):
        """Test na liście jednoelementowej."""
        self.assertEqual(
            penultimate([41], 42),
            42)

    def test_two_elements(self):
        """Test na liście dwuelementowej."""
        self.assertEqual(
            penultimate(['x', 'y'], 'z'),
            'x')

if __name__ == '__main__':
    unittest.main()
