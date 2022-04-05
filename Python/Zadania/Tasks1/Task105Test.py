#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 105

Napisz funkcję `is_almost_prime(number, limit)` sprawdzającą, czy
podana liczba nie dzieli się przez żadną liczbę z zakresu od 2 do
`limit`. Dla liczb ujemnych powinna zostać zwrócona wartość `False`.

NAME: is_almost_prime
PARAMS: int, int
RETURN: bool
POINTS: 1
"""

import unittest
from Task105 import is_almost_prime

class Task105Test(unittest.TestCase):
    """Testy do zadania 105"""

    def test_simple(self):
        """Proste testy"""
        self.assertTrue(is_almost_prime(35, 4))
        self.assertFalse(is_almost_prime(35, 5))
        self.assertFalse(is_almost_prime(35, 100))
        self.assertTrue(is_almost_prime(17, 4))
        self.assertTrue(is_almost_prime(17, 16))
        self.assertFalse(is_almost_prime(17, 17))
        self.assertFalse(is_almost_prime(17, 100))
        self.assertFalse(is_almost_prime(16, 2))
        self.assertFalse(is_almost_prime(16, 5))
        self.assertFalse(is_almost_prime(16, 13))
        self.assertFalse(is_almost_prime(16, 101))

    def test_special_cases(self):
        """Testy przypadków szczególnych."""
        self.assertFalse(is_almost_prime(-1, 10))
        self.assertFalse(is_almost_prime(0, 8))
        self.assertTrue(is_almost_prime(1, 6))
        self.assertFalse(is_almost_prime(2, 2))

    def test_negatives(self):
        """Testy dla liczb ujemnych."""
        self.assertFalse(is_almost_prime(-5, 100))
        self.assertFalse(is_almost_prime(-13, 5))

if __name__ == '__main__':
    unittest.main()
