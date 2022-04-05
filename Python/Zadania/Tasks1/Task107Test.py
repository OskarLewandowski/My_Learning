#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 107

Napisz funkcję `list_cubed(list)` zwracającą sumę sześcianów
zadanych liczb. Dla listy pustej powinna zostać zwrócona wartość zero.

NAME: list_cubed
PARAMS: list
RETURN: obj
POINTS: 1
"""

import unittest
from Task107 import list_cubed

class Task107Test(unittest.TestCase):
    """Testy do zadania 107"""

    def test_simple(self):
        """Prosty test."""
        self.assertEqual(list_cubed([3, 0, -1, 2]), 34),

    def test_empty(self):
        """Test na pustej liście."""
        self.assertEqual(list_cubed([]), 0),

    def test_singleton(self):
        """Test na liście jednoelementowej."""
        self.assertEqual(list_cubed([-4]), -64)

    def test_two_elements(self):
        """Test na liście dwuelementowej."""
        self.assertEqual(list_cubed([100, -100]), 0)
        self.assertEqual(list_cubed([2, 10]), 1008)

if __name__ == '__main__':
    unittest.main()
