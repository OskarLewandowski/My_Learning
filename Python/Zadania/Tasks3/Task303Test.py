#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 303

Napisz funkcję `divisable_by_four(string)`, która
sprawdza, czy podany napis reprezentuje liczbę nieujemną podzielną
przez 4. Uwaga: cała "logika" rozwiązania powinna być zaszyta
w wyrażeniu regularnym, w szczególności proszę nie używać operatora
wyznaczania reszty.

NAME: divisable_by_four
PARAMS: string
RETURN: bool
POINTS: 3
"""

import unittest
from Task303 import divisable_by_four

class Task303Test(unittest.TestCase):
    """Testy do zadania 303"""

    def test_simple(self):
        """Prosty test."""
        self.assertTrue(divisable_by_four("32"))
        self.assertFalse(divisable_by_four("33"))
        self.assertFalse(divisable_by_four("-32"))
        self.assertTrue(divisable_by_four("0"))

        for num in range(45000, 47000):
            if num % 4 == 0:
                self.assertTrue(divisable_by_four(str(num)), str(num))
            else:
                self.assertFalse(divisable_by_four(str(num)), str(num))

if __name__ == '__main__':
    unittest.main()
