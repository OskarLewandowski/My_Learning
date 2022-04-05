#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 209

Napisz funkcję `monsters_automaton()`, która
tworzy i zwraca automat, który akceptuje
wyłącznie napisy "Godzilla", "Ghidora" oraz "Mothra"
i żadnych innych.

NAME: monsters_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task209 import monsters_automaton

class Task209Test(unittest.TestCase):
    """Testy do zadania 209"""

    def test_simple(self):
        """Prosty test."""

        automaton = monsters_automaton()

        self.assertTrue(automaton.accepts("Godzilla"))
        self.assertTrue(automaton.accepts("Ghidora"))
        self.assertTrue(automaton.accepts("Mothra"))

        self.assertFalse(automaton.accepts("Biollante"))
        self.assertFalse(automaton.accepts(""))
        self.assertFalse(automaton.accepts("Godzil"))
        self.assertFalse(automaton.accepts("Kojot"))
        self.assertFalse(automaton.accepts("Godzra"))

if __name__ == '__main__':
    unittest.main()
