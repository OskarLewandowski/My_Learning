#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 103

Napisz funkcję `probability` sprawdzającej, czy zadana liczba
reprezentuje prawdopodobieństwo (liczbę z zakresu od 0.0 do 1.0).
Jeśli tak, powinna zostać zwrócona ta liczba, w przeciwnym razie -
liczba 0.

NAME: probability
PARAMS: double
RETURN: double
POINTS: 1

"""

import unittest
from Task103 import probability

class Task103Test(unittest.TestCase):
    """Testy do zadania 103"""

    def test_simple(self):
        """Prosty test."""
        self.assertAlmostEqual(probability(0.62), 0.62)

    def test_negatives(self):
        """Test z liczbami ujemnymi."""
        self.assertAlmostEqual(probability(-0.6), 0.0)
        self.assertAlmostEqual(probability(-1337), 0.0)

    def test_special_cases(self):
        """Test z wartościami specjalnymi."""
        self.assertEqual(probability(0.0), 0.0)
        self.assertEqual(probability(1.0), 1.0)

    def test_out_of_range(self):
        """Za duże wartości."""
        self.assertEqual(probability(1.001), 0.0)
        self.assertEqual(probability(972.12), 0.0)


if __name__ == '__main__':
    unittest.main()
