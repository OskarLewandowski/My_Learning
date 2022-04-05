#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 326

Napisać funkcję is_dna(string), która sprawdza, czy
napis jest niepustym ciągiem liter A, G, C, T, U, przy czym w jednym
ciągu może wystąpić albo T, albo U nie obie litery
równocześnie.

NAME: is_dna
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task326 import is_dna

class Task326Test(unittest.TestCase):
    """Testy do zadania 326"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_dna("UAT"))
        self.assertTrue(is_dna("AGCUUGGAAACU"))
        self.assertTrue(is_dna("AGCTTGGAAACT"))
        self.assertFalse(is_dna("89"))
        self.assertTrue(is_dna("AAAAA"))
        self.assertFalse(is_dna("aaa"))
        self.assertFalse(is_dna("TAU"))
        self.assertTrue(is_dna("G"))
        self.assertTrue(is_dna("UAU"))
        self.assertTrue(is_dna("TAT"))

if __name__ == '__main__':
    unittest.main()
