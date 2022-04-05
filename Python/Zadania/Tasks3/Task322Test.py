#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 322

Napisać funkcję is_temperature(string), która sprawdza, czy
napis jest liczbą całkowitą z zakresu od -49 do 49. Liczba nie
powinna zawierać zer nieznaczących.

NAME: is_temperature
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task322 import is_temperature

class Task322Test(unittest.TestCase):
    """Testy do zadania 322"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_temperature("-9"))
        self.assertFalse(is_temperature("7"))
        self.assertFalse(is_temperature("-200"))
        self.assertTrue(is_temperature("-21"))
        self.assertTrue(is_temperature("18"))
        self.assertTrue(is_temperature("0"))
        self.assertTrue(is_temperature("49"))
        self.assertFalse(is_temperature("100"))
        self.assertTrue(is_temperature("-49"))

if __name__ == '__main__':
    unittest.main()
