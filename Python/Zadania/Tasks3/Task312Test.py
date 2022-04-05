#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 312

Napisać funkcję is_pin_code(string), która sprawdza, czy
napis jest 4-cyfrowym kodem PIN, przy czym zakładamy, że kod PIN
nie może składać się z samych zer.

NAME: is_pin_code
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task312 import is_pin_code

class Task312Test(unittest.TestCase):
    """Testy do zadania 312"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_pin_code("7787"))
        self.assertTrue(is_pin_code("8888"))
        self.assertTrue(is_pin_code("5034"))
        self.assertFalse(is_pin_code("WTF"))
        self.assertTrue(is_pin_code("1112"))
        self.assertTrue(is_pin_code("0123"))
        self.assertTrue(is_pin_code("1111"))
        self.assertTrue(is_pin_code("0300"))
        self.assertFalse(is_pin_code("0000"))
        self.assertFalse(is_pin_code("12345"))
        self.assertTrue(is_pin_code("4655"))

if __name__ == '__main__':
    unittest.main()
