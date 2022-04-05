#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 210

Napisz funkcję `abc_automaton()`, która
tworzy i zwraca automat, który akceptuje
napisy składające z dowolnej liczby
znaków 'a', po których następuje dowolna liczba
znaków 'b', po których następuje dowolna liczba
znaków 'c'. "Dowolna" oznacza także zero.

NAME: abc_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task210 import abc_automaton

class Task210Test(unittest.TestCase):
    """Testy do zadania 210"""

    def test_simple(self):
        """Prosty test."""

        automaton = abc_automaton()

        self.assertTrue(automaton.accepts(""))
        self.assertTrue(automaton.accepts("abc"))
        self.assertTrue(automaton.accepts("aaaaaaaabccc"))
        self.assertTrue(automaton.accepts("bbbccc"))
        self.assertTrue(automaton.accepts("ac"))
        self.assertTrue(automaton.accepts("abbbbbbbbbbbbbb"))

        self.assertFalse(automaton.accepts("ba"))
        self.assertFalse(automaton.accepts("cccbbbaaa"))
        self.assertFalse(automaton.accepts("baba"))
        self.assertFalse(automaton.accepts("abcca"))


if __name__ == '__main__':
    unittest.main()
