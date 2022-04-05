#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 200

Napisz funkcję `abc_automaton()`, która
tworzy i zwraca automat, który akceptuje
napisy zaczynające się od a, kończące się na c i zawierające w środku
dowolną liczbę znaków b

NAME: abc_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 1
"""

import unittest
from Task200 import abc_automaton

class Task200Test(unittest.TestCase):
    """Testy do zadania 200"""

    def test_simple(self):
        """Prosty test."""

        automaton = abc_automaton()

        self.assertTrue(automaton.accepts("ac"))
        self.assertTrue(automaton.accepts("abc"))
        self.assertTrue(automaton.accepts("abbbbbbbbbbc"))

        self.assertFalse(automaton.accepts("a"))
        self.assertFalse(automaton.accepts("c"))
        self.assertFalse(automaton.accepts("bbbc"))
        self.assertFalse(automaton.accepts("abcabc"))
        self.assertFalse(automaton.accepts(""))


if __name__ == '__main__':
    unittest.main()
