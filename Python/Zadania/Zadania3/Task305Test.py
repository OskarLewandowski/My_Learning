#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 305

Napisać funkcję divisable_by_two(string), która sprawdza, czy
zadany napis reprezentuje nieujemną liczbę podzielną przez 2.
Napis nie powinien zawierać zer nieznaczących.
Uwaga: cała "logika" rozwiązania powinna być zaszyta
w wyrażeniu regularnym, w szczególności proszę nie używać operatora
wyznaczania reszty.

NAME: divisable_by_two
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task305 import divisable_by_two

class Task305Test(unittest.TestCase):
    """Testy do zadania 305"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(divisable_by_two("222221"))
        self.assertFalse(divisable_by_two("3"))
        self.assertFalse(divisable_by_two("4 4"))
        self.assertFalse(divisable_by_two("04"))
        self.assertTrue(divisable_by_two("2"))
        self.assertTrue(divisable_by_two("222222"))
        self.assertFalse(divisable_by_two("1"))
        self.assertTrue(divisable_by_two("4"))
        self.assertFalse(divisable_by_two("0018"))
        self.assertFalse(divisable_by_two("-20"))
        self.assertTrue(divisable_by_two("88"))
        self.assertTrue(divisable_by_two("0"))
        self.assertTrue(divisable_by_two("16"))

if __name__ == '__main__':
    unittest.main()
