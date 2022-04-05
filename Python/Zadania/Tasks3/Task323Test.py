#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 323

Napisać funkcję are_stars(string), która sprawdza, czy
napis składa się z samych gwiazdek (co najmniej jednej).

NAME: are_stars
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task323 import are_stars

class Task323Test(unittest.TestCase):
    """Testy do zadania 323"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(are_stars("*a"))
        self.assertTrue(are_stars("***********"))
        self.assertTrue(are_stars("**"))
        self.assertFalse(are_stars("a*"))
        self.assertTrue(are_stars("*"))
        self.assertFalse(are_stars("+"))
        self.assertTrue(are_stars("***"))

if __name__ == '__main__':
    unittest.main()
