#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 321

Napisać funkcję is_identifier(string), która sprawdza, czy
napis jest identyfikatorem (ciągiem liter, cyfr i podkreślników
nie zaczynających się cyfrą).

NAME: is_identifier
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task321 import is_identifier

class Task321Test(unittest.TestCase):
    """Testy do zadania 321"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_identifier("Gitorah"))
        self.assertTrue(is_identifier("z0000000"))
        self.assertTrue(is_identifier("_____"))
        self.assertTrue(is_identifier("godzilla"))
        self.assertTrue(is_identifier("x"))
        self.assertFalse(is_identifier("2"))
        self.assertFalse(is_identifier("bla-bla"))
        self.assertFalse(is_identifier("2_"))
        self.assertFalse(is_identifier(";zmienna"))
        self.assertFalse(is_identifier("zmienna$"))
        self.assertFalse(is_identifier("90876z"))
        self.assertTrue(is_identifier("_2"))
        self.assertTrue(is_identifier("_a_"))
        self.assertTrue(is_identifier("blo_34a"))

if __name__ == '__main__':
    unittest.main()
