#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 302

Napisz funkcję `extract_minutes(string)`, która
z podanego napisu reprezentującego godzinę
w formacie typu "9:13", "18:44" wyciąga minuty.
Funkcja powinna zwracać napis "<NONE>", jeśli podany
napis nie jest godziną.

NAME: extract_minutes
PARAMS: string
RETURN: string
POINTS: 4
"""

import unittest
from Task302 import extract_minutes

class Task302Test(unittest.TestCase):
    """Testy do zadania 302"""

    def test_simple(self):
        """Prosty test."""
        self.assertEqual(extract_minutes("9:13"), "13")
        self.assertEqual(extract_minutes("18:44"), "44")
        self.assertEqual(extract_minutes("23:59"), "59")
        self.assertEqual(extract_minutes("0:00"), "00")
        self.assertEqual(extract_minutes("25:14"), "<NONE>")
        self.assertEqual(extract_minutes("9:61"), "<NONE>")
        self.assertEqual(extract_minutes("x9:13y"), "<NONE>")

if __name__ == '__main__':
    unittest.main()
