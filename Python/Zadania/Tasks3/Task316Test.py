#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 316

Napisać funkcję is_acronym(string), która sprawdza, czy
napis jest akronimem (ciągiem co najmniej dwóch i co najwyżej
pięciu wielkich liter. Dodatkowo należy uwzględnić akronim
"PCMCIA".

NAME: is_acronym
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task316 import is_acronym

class Task316Test(unittest.TestCase):
    """Testy do zadania 316"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_acronym("ATX"))
        self.assertFalse(is_acronym("AAAAAA"))
        self.assertFalse(is_acronym("P"))
        self.assertTrue(is_acronym("ABCDE"))
        self.assertFalse(is_acronym("Pc"))
        self.assertTrue(is_acronym("PC"))
        self.assertTrue(is_acronym("PCMCIA"))
        self.assertTrue(is_acronym("ZZZZ"))
        self.assertFalse(is_acronym("PCMCIB"))

if __name__ == '__main__':
    unittest.main()
