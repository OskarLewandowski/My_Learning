#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 314

Napisać funkcję is_male(string), która sprawdza, czy
napis reprezentuje imię i nazwisko mężczyzny. Imię i nazwisko to
przynajmniej dwuliterowy napis zaczynający się wielką literą, po
której następują małe litery. Dodatkowo imię nie może kończyć
się na "a".

NAME: is_male
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task314 import is_male

class Task314Test(unittest.TestCase):
    """Testy do zadania 314"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_male("Joanna Kowalska"))
        self.assertTrue(is_male("Oo Oo"))
        self.assertTrue(is_male("Atanazy Bazakbal"))
        self.assertTrue(is_male("Ai Oi"))
        self.assertTrue(is_male("Ax Aa"))
        self.assertFalse(is_male("Aa Ax"))
        self.assertTrue(is_male("Kim Bo"))
        self.assertTrue(is_male("Jan Maska"))

if __name__ == '__main__':
    unittest.main()
