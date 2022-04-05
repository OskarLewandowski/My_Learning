#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 301

Napisz funkcję `letter_and_two_digits(string)`, która sprawdza
czy podany napis zawiera ciąg składający się z wielkiej litery
i dwóch cyfr.

NAME: letter_and_two_digits
PARAMS: string
RETURN: bool
POINTS: 3
"""

import unittest
from Task301 import letter_and_two_digits

class Task301Test(unittest.TestCase):
    """Testy do zadania 301"""

    def test_sequence(self):
        """Prosty test."""
        self.assertTrue(letter_and_two_digits("hahaA39dsdsd"))
        self.assertTrue(letter_and_two_digits("G3923d"))
        self.assertTrue(letter_and_two_digits("Z00"))
        self.assertTrue(letter_and_two_digits("sssssssssssU23"))
        self.assertFalse(letter_and_two_digits("Z0x0"))
        self.assertFalse(letter_and_two_digits("dsdg34"))
        self.assertFalse(letter_and_two_digits("G9"))
        self.assertFalse(letter_and_two_digits("az33a"));
        self.assertFalse(letter_and_two_digits("Ha3a5"));


if __name__ == '__main__':
    unittest.main()
