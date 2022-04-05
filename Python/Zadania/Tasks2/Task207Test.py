#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 207

Napisz funkcję `three_automaton()`, która
tworzy i zwraca automat, który akceptuje
napisy reprezentujące liczby podzielne przez 3. Automat
nie powinien akceptować napisów zaczynających
nieznaczącymi zerami (np. "033").

NAME: three_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task207 import three_automaton

class Task207Test(unittest.TestCase):
    """Testy do zadania 207"""

    def test_simple(self):
        """Prosty test."""

        automaton = three_automaton()

        self.assertTrue(automaton.accepts("3"))
        self.assertTrue(automaton.accepts("0"))
        self.assertTrue(automaton.accepts("12"))
        self.assertTrue(automaton.accepts("324"))
        self.assertTrue(automaton.accepts("333333"))
        self.assertTrue(automaton.accepts("30003"))
        self.assertTrue(automaton.accepts("513"))

        self.assertFalse(automaton.accepts("00"))
        self.assertFalse(automaton.accepts("012"))
        self.assertFalse(automaton.accepts("0000324"))
        self.assertFalse(automaton.accepts("1"))
        self.assertFalse(automaton.accepts("2"))
        self.assertFalse(automaton.accepts("5"))
        self.assertFalse(automaton.accepts("1111"))

if __name__ == '__main__':
    unittest.main()
