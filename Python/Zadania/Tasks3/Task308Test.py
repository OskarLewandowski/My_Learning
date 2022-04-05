#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 308

Napisać funkcję is_horse_head(string), która sprawdza, czy
napis jest napisem złożonym z ciągu 5 wielkich liter i 4 wielkich
liter oddzielonych spacją, które wstukane na standardowym telefonie
dadzą taki sam numer jak przy wstukaniu napisu "HORSE HEAD".
Zakładamy standardowe mapowanie liter na cyfry w telefonie ("ABC" -
2, "DEF" - 3 itd.)

NAME: is_horse_head
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task308 import is_horse_head

class Task308Test(unittest.TestCase):
    """Testy do zadania 308"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_horse_head("ZOSRE IDAD"))
        self.assertFalse(is_horse_head("morse head"))
        self.assertFalse(is_horse_head("MORSEHEAD"))
        self.assertFalse(is_horse_head("AAAAAA BBBB"))
        self.assertFalse(is_horse_head("MORSE HEAD"))
        self.assertTrue(is_horse_head("HORSE HEAD"))
        self.assertFalse(is_horse_head("AAAAA BBBB"))
        self.assertTrue(is_horse_head("GOSRE IDAD"))
        self.assertFalse(is_horse_head("0MORSE HEAD"))

if __name__ == '__main__':
    unittest.main()
