#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 109

Napisz funkcję `count_yes_lines(filename)`, która po podaniu nazwy pliku
tekstowego `filename` zwraca liczbę wierszy w pliku zawierających
(wyłącznie) napis "YES" (i znak końca wiersza).

NAME: count_yes_lines
PARAMS: string
RETURN: int
POINTS: 1
"""
import unittest
from Task109 import count_yes_lines

class Task109Test(unittest.TestCase):
    """Testy do zadania 109."""

    def test_on_self(self):
        """Testy na samym sobie."""
        self.failUnlessEqual(count_yes_lines("Task109Test.py"), 0)

    def test_simple(self):
        """Testy na prostym pliku."""
        self.failUnlessEqual(count_yes_lines("Task109Test.dat.txt"), 4)

if __name__ == '__main__':
    unittest.main()
