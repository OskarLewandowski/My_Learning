#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 102

Napisz funkcję `add_three_numbers` zwracającą sumę trzech liczb całkowitych.

NAME: add_three_numbers
PARAMS: int, int, int
RETURN: int
POINTS: 1
"""

import unittest
from Task102 import add_three_numbers

class Task102Test(unittest.TestCase):
    """Testy do zadania 102"""

    def test_simple(self):
        """Prosty test."""
        self.assertEqual(add_three_numbers(2, 5, 7), 14)

    def test_negatives(self):
        """Test z liczbami ujemnymi."""
        self.assertEqual(add_three_numbers(-3, -1, 2), -2)

if __name__ == '__main__':
    unittest.main()
