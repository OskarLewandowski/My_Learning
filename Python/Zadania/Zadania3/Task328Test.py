#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 328

Napisać funkcję is_hmmmm(string), która sprawdza, czy
napis to "hmmm....." - 'm' występuje 2 lub więcej razy, kropki są
opcjonalne, ale jeśli występują muszą wystąpić przynajmniej 3
razy.

NAME: is_hmmmm
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task328 import is_hmmmm

class Task328Test(unittest.TestCase):
    """Testy do zadania 328"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_hmmmm("hmm..."))
        self.assertFalse(is_hmmmm("hmmmm.....?!"))
        self.assertFalse(is_hmmmm("ahmmmm....."))
        self.assertFalse(is_hmmmm("hhmmm....."))
        self.assertFalse(is_hmmmm("hm....."))
        self.assertFalse(is_hmmmm("mmm...."))
        self.assertFalse(is_hmmmm("hmmm.."))
        self.assertTrue(is_hmmmm("hmmmm......"))
        self.assertFalse(is_hmmmm("hmmm."))
        self.assertTrue(is_hmmmm("hmm"))
        self.assertTrue(is_hmmmm("hmmm...."))

if __name__ == '__main__':
    unittest.main()
