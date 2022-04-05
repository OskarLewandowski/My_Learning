#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 306

Napisać funkcję is_power_of_hundred(string), która sprawdza, czy
zadany napis jest potęgą liczby 100.
Uwaga: cała "logika" rozwiązania powinna być zaszyta
w wyrażeniu regularnym.

NAME: is_power_of_hundred
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task306 import is_power_of_hundred

class Task306Test(unittest.TestCase):
    """Testy do zadania 306"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_power_of_hundred("-100"))
        self.assertTrue(is_power_of_hundred("10000"))
        self.assertFalse(is_power_of_hundred("1001"))
        self.assertTrue(is_power_of_hundred("1"))
        self.assertTrue(is_power_of_hundred("1000000"))
        self.assertFalse(is_power_of_hundred("10"))
        self.assertFalse(is_power_of_hundred("2000"))
        self.assertFalse(is_power_of_hundred("500"))
        self.assertTrue(is_power_of_hundred("100"))

if __name__ == '__main__':
    unittest.main()
