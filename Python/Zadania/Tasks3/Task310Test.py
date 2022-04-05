#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 310

Napisać funkcję is_football_result(string), która sprawdza, czy
napis reprezentuje wynik meczu piłkarskiego (dwie liczby oddzielone
dwukropkiem). Maksymalna liczba bramek wynosi 10.

NAME: is_football_result
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task310 import is_football_result

class Task310Test(unittest.TestCase):
    """Testy do zadania 310"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_football_result("3"))
        self.assertTrue(is_football_result("10:10"))
        self.assertTrue(is_football_result("5:2"))
        self.assertFalse(is_football_result("11:2"))
        self.assertFalse(is_football_result("5-5"))
        self.assertTrue(is_football_result("2:1"))
        self.assertTrue(is_football_result("5:5"))
        self.assertFalse(is_football_result(":3"))
        self.assertFalse(is_football_result("3:101"))
        self.assertFalse(is_football_result("xxxx"))
        self.assertTrue(is_football_result("0:7"))

if __name__ == '__main__':
    unittest.main()
