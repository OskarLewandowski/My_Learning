#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 327

Napisać funkcję is_giggle(string), która sprawdza, czy
napis jest chichotem tzn. "hi" powtórzonym przynajmniej 2 razy, po
czym następuje opcjonalny ciąg wykrzykników.

NAME: is_giggle
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task327 import is_giggle

class Task327Test(unittest.TestCase):
    """Testy do zadania 327"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_giggle("hi"))
        self.assertFalse(is_giggle("ih!"))
        self.assertTrue(is_giggle("hihi!!!!!!!!!"))
        self.assertTrue(is_giggle("hihihihihihihihi"))
        self.assertTrue(is_giggle("hihi"))
        self.assertFalse(is_giggle("!!!!!"))
        self.assertTrue(is_giggle("hihihi"))
        self.assertFalse(is_giggle("hi!!!"))
        self.assertFalse(is_giggle("!hi"))
        self.assertTrue(is_giggle("hihihi!"))

if __name__ == '__main__':
    unittest.main()
