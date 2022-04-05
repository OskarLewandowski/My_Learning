#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 217

Napisz funkcję `dna_automaton()`, która
tworzy i zwraca automat, który akceptuje
niepuste ciągi złozone z liter "A", "C", "G" i "T"
których długość jest wielokrotnością liczby 3.

NAME: dna_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task217 import dna_automaton

class Task217Test(unittest.TestCase):
    """Testy do zadania 217"""

    def test_simple(self):
        """Prosty test."""

        automaton = dna_automaton()

        self.assertTrue(automaton.accepts("AAACGT"))
        self.assertTrue(automaton.accepts("ACA"))
        self.assertTrue(automaton.accepts("ACAAAAGCAACAAAAGCA"))
        self.assertTrue(automaton.accepts("TTT"))

        self.assertFalse(automaton.accepts("TT"))
        self.assertFalse(automaton.accepts("A"))
        self.assertFalse(automaton.accepts("AAACG"))
        self.assertFalse(automaton.accepts(""))

if __name__ == '__main__':
    unittest.main()
