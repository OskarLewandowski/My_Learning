#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 317

Napisać funkcję is_integer(string), która sprawdza, czy
napis reprezentuje liczbę całkowitą. Liczba nie powinna zawierać
zer nieznaczących. Liczby dodatnie mogą opcjonalnie zaczynać się
plusem.

NAME: is_integer
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task317 import is_integer

class Task317Test(unittest.TestCase):
    """Testy do zadania 317"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_integer("+5"))
        self.assertTrue(is_integer("-5"))
        self.assertTrue(is_integer("3434343435"))
        self.assertFalse(is_integer("-0"))
        self.assertTrue(is_integer("0"))
        self.assertFalse(is_integer("03434343435"))
        self.assertFalse(is_integer("+0"))
        self.assertFalse(is_integer("06"))
        self.assertTrue(is_integer("100"))
        self.assertTrue(is_integer("5"))
        self.assertTrue(is_integer("-11110"))

if __name__ == '__main__':
    unittest.main()
