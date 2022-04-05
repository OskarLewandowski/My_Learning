#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 319

Napisać funkcję less_than(string), która sprawdza, czy
napis reprezentuje liczbę całkowitą nieujemną mniejszą niż 143.
Liczba nie powinna zawierać zer nieznaczących.

NAME: less_than
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task319 import less_than

class Task319Test(unittest.TestCase):
    """Testy do zadania 319"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(less_than("098"))
        self.assertFalse(less_than("05"))
        self.assertTrue(less_than("142"))
        self.assertTrue(less_than("139"))
        self.assertTrue(less_than("78"))
        self.assertFalse(less_than("143"))
        self.assertTrue(less_than("103"))
        self.assertTrue(less_than("99"))
        self.assertTrue(less_than("0"))
        self.assertFalse(less_than("1000"))
        self.assertFalse(less_than("-1"))
        self.assertTrue(less_than("5"))

if __name__ == '__main__':
    unittest.main()
