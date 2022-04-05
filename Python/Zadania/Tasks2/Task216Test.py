#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 216

Napisz funkcję `code_automaton()`, która
tworzy i zwraca automat, który akceptuje
kody pocztowe (ciągi cyfra-cyfra-minus-cyfra-cyfr-cyfra).

NAME: code_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task216 import code_automaton

class Task216Test(unittest.TestCase):
    """Testy do zadania 216"""

    def test_simple(self):
        """Prosty test."""

        automaton = code_automaton()

        self.assertTrue(automaton.accepts("61-909"))
        self.assertTrue(automaton.accepts("22-340"))
        self.assertTrue(automaton.accepts("00-000"))
        self.assertTrue(automaton.accepts("99-999"))

        self.assertFalse(automaton.accepts("61909"))
        self.assertFalse(automaton.accepts("61-90"))
        self.assertFalse(automaton.accepts("000-000"))
        self.assertFalse(automaton.accepts(""))


if __name__ == '__main__':
    unittest.main()
