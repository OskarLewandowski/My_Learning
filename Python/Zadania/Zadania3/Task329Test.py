#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 329

Napisać funkcję is_singing(string), która sprawdza, czy
napis jest śpiewem, tj. jest ciągiem sylab "li", "la", "lo" (co
najmniej dwóch), po którym następuje opcjonalny ciąg
wykrzykników.

NAME: is_singing
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task329 import is_singing

class Task329Test(unittest.TestCase):
    """Testy do zadania 329"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_singing("!!lala!!"))
        self.assertFalse(is_singing("lol"))
        self.assertFalse(is_singing("ola!"))
        self.assertFalse(is_singing("luli"))
        self.assertTrue(is_singing("lilala!!!"))
        self.assertTrue(is_singing("lololali!"))
        self.assertTrue(is_singing("lilili!!!!"))
        self.assertTrue(is_singing("lala"))

if __name__ == '__main__':
    unittest.main()
