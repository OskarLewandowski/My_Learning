#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 315

Napisać funkcję is_female(string), która sprawdza, czy
napis reprezentuje imię i nazwisko kobiety. Imię i nazwisko to
przynajmniej dwuliterowy napis zaczynający się wielką literą, po
której następują małe litery. Dodatkowo imię musi kończyć się
na "a".

NAME: is_female
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task315 import is_female

class Task315Test(unittest.TestCase):
    """Testy do zadania 315"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertTrue(is_female("Joanna Kowalska"))
        self.assertFalse(is_female("Ai Oi"))
        self.assertTrue(is_female("Aa Ax"))
        self.assertFalse(is_female("Kim Bo"))
        self.assertFalse(is_female("Jan Maska"))
        self.assertFalse(is_female("Oo Oo"))
        self.assertTrue(is_female("Za Mysz"))
        self.assertFalse(is_female("Atanazy Bazakbal"))
        self.assertFalse(is_female("Ax Aa"))

if __name__ == '__main__':
    unittest.main()
