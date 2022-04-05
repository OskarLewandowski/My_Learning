#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 324

Napisać funkcję is_one_vowel(string), która sprawdza, czy
napis jest wyrazem zawierającym dokładnie jedną samogłoskę.
Należy uwzględnić małe litery alfabetu łacińskiego.

NAME: is_one_vowel
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task324 import is_one_vowel

class Task324Test(unittest.TestCase):
    """Testy do zadania 324"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_one_vowel("dom"))
        self.assertFalse(is_one_vowel("puko"))
        self.assertTrue(is_one_vowel("u"))
        self.assertFalse(is_one_vowel("ostrach"))
        self.assertFalse(is_one_vowel("html"))
        self.assertTrue(is_one_vowel("strach"))
        self.assertFalse(is_one_vowel("strachy"))
        self.assertFalse(is_one_vowel("aa"))
        self.assertFalse(is_one_vowel("223"))

if __name__ == '__main__':
    unittest.main()
