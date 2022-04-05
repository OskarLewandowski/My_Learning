#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 104

Napisz funkcję `fahrenheit`, która przelicza stopnie Celsjusza na
stopnie Fahrenheita. Dla wartości mniejszych niż -273.15 funkcja
powinna zwracać zawsze -459.67.

NAME: fahrenheit
PARAMS: float
RETURN: float
POINTS: 1
"""

import unittest
from Task104 import fahrenheit

class Task104Test(unittest.TestCase):
    """Testy do zadania 104"""

    def test_simple_cases(self):
        """Testy dla standardowych przypadków."""
        self.assertAlmostEqual(fahrenheit(10), 50)
        self.assertAlmostEqual(fahrenheit(33), 91.4)
        self.assertAlmostEqual(fahrenheit(0), 32)
        self.assertAlmostEqual(fahrenheit(-8), 17.6)
        self.assertAlmostEqual(fahrenheit(-273), -459.4)
        self.assertAlmostEqual(fahrenheit(-273.15), -459.67)

    def test_below_zero(self):
        """Testy dla temperatur poniżej zera absolutnego."""
        self.assertAlmostEqual(fahrenheit(-274), -459.67)
        self.assertAlmostEqual(fahrenheit(-10000), -459.67)

if __name__ == '__main__':
    unittest.main()
