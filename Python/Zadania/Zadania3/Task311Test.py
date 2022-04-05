#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 311

Napisać funkcję is_nip_number(string), która sprawdza, czy
napis jest numerem NIP zapisanym w formacie xxx-xxx-xx-xx bądź
xxx-xx-xx-xxx. Nie trzeba brać pod uwagę sumy kontrolnej.

NAME: is_nip_number
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task311 import is_nip_number

class Task311Test(unittest.TestCase):
    """Testy do zadania 311"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_nip_number("3454551234"))
        self.assertTrue(is_nip_number("000-00-00-000"))
        self.assertTrue(is_nip_number("345-45-12-334"))
        self.assertFalse(is_nip_number("345-455-12-349"))
        self.assertTrue(is_nip_number("345-455-12-34"))

if __name__ == '__main__':
    unittest.main()
