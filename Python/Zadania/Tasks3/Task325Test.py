#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 325

Napisać funkcję is_dollar_sum(string), która sprawdza, czy
napis wyraża sumę w dolarach, tj. zaczyna się znakiem dolara, po
którym następuje liczba dodatnia (bez zer nieznaczących).

NAME: is_dollar_sum
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task325 import is_dollar_sum

class Task325Test(unittest.TestCase):
    """Testy do zadania 325"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_dollar_sum("$"))
        self.assertTrue(is_dollar_sum("$1"))
        self.assertTrue(is_dollar_sum("$100"))
        self.assertFalse(is_dollar_sum("10$100"))
        self.assertFalse(is_dollar_sum("89"))
        self.assertFalse(is_dollar_sum("$0098"))
        self.assertTrue(is_dollar_sum("$67592234"))
        self.assertTrue(is_dollar_sum("$89"))

if __name__ == '__main__':
    unittest.main()
