#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 215

Napisz funkcję `four_automaton()`, która
tworzy i zwraca automat, który akceptuje
napisy reprezentujące liczby podzielne przez 4. Automat
nie powinien akceptować napisów zaczynających
nieznaczącymi zerami (np. "044").

NAME: four_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task215 import four_automaton

class Task215Test(unittest.TestCase):
    """Testy do zadania 215"""

    def test_simple(self):
        """Prosty test."""

        automaton = four_automaton()

        self.assertTrue(automaton.accepts("4"))
        self.assertTrue(automaton.accepts("0"))
        self.assertTrue(automaton.accepts("12"))
        self.assertTrue(automaton.accepts("324"))
        self.assertTrue(automaton.accepts("1052"))
        self.assertTrue(automaton.accepts("444444"))

        self.assertFalse(automaton.accepts("012"))
        self.assertFalse(automaton.accepts("0000324"))
        self.assertFalse(automaton.accepts("5"))
        self.assertFalse(automaton.accepts("1"))
        self.assertFalse(automaton.accepts("3"))
        self.assertFalse(automaton.accepts("34"))
        self.assertFalse(automaton.accepts("1057"))
        self.assertFalse(automaton.accepts("4454"))


if __name__ == '__main__':
    unittest.main()
