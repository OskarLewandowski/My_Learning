#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 313

Napisać funkcję is_human_age(string), która sprawdza, czy
napis reprezentuje wiek człowieka, tzn. jest postaci typu "45 lat".
Maksymalny wiek - 99 lat.

NAME: is_human_age
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task313 import is_human_age

class Task313Test(unittest.TestCase):
    """Testy do zadania 313"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_human_age("12 lata"))
        self.assertTrue(is_human_age("99 lat"))
        self.assertTrue(is_human_age("5 lat"))
        self.assertTrue(is_human_age("1 rok"))
        self.assertTrue(is_human_age("44 lata"))
        self.assertTrue(is_human_age("11 lat"))
        self.assertTrue(is_human_age("22 lata"))
        self.assertTrue(is_human_age("4 lata"))
        self.assertFalse(is_human_age("100 lat"))
        self.assertFalse(is_human_age("112 lat"))
        self.assertFalse(is_human_age("22 lat"))
        self.assertTrue(is_human_age("2 lata"))
        self.assertTrue(is_human_age("3 lata"))
        self.assertTrue(is_human_age("12 lat"))

if __name__ == '__main__':
    unittest.main()
