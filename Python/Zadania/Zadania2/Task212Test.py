#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 212

Napisz funkcję `negation_automaton()`, która tworzy i zwraca automat
akceptujący wszystkie napisy nad alfabetem "abcd"
z wyjątkiem napisu "abba".

NAME: negation_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task212 import negation_automaton

class Task212Test(unittest.TestCase):
    """Testy do zadania 212"""

    def test_simple(self):
        """Prosty test."""

        automaton = negation_automaton()

        self.assertTrue(automaton.accepts("abbb"))
        self.assertTrue(automaton.accepts("baca"))
        self.assertTrue(automaton.accepts("dddddd"))
        self.assertTrue(automaton.accepts("abbaa"))
        self.assertTrue(automaton.accepts("abb"))
        self.assertTrue(automaton.accepts("ab"))
        self.assertTrue(automaton.accepts(""))

        self.assertFalse(automaton.accepts("abba"))
        self.assertFalse(automaton.accepts("xa"))


if __name__ == '__main__':
    unittest.main()
