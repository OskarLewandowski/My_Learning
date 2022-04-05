#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 318

Napisać funkcję is_five_six_digit(string), która sprawdza, czy
napis reprezentuje liczbę pięcio- bądź sześciocyfrową. Liczba
nie powinna zawierać zer nieznaczących.

NAME: is_five_six_digit
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task318 import is_five_six_digit

class Task318Test(unittest.TestCase):
    """Testy do zadania 318"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_five_six_digit("0123456"))
        self.assertTrue(is_five_six_digit("123456"))
        self.assertTrue(is_five_six_digit("100001"))
        self.assertTrue(is_five_six_digit("10000"))
        self.assertTrue(is_five_six_digit("99999"))
        self.assertFalse(is_five_six_digit("333333333333"))
        self.assertFalse(is_five_six_digit("012345"))
        self.assertTrue(is_five_six_digit("999999"))
        self.assertTrue(is_five_six_digit("12345"))
        self.assertFalse(is_five_six_digit("9999"))

if __name__ == '__main__':
    unittest.main()
