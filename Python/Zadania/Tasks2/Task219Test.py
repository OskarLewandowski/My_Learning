#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 219

Napisz funkcję `alt_automaton()`, która
tworzy i zwraca automat, akceptujący
napisy złożone z "abc" powielonego dowolną liczbę razy
(w tym zero) oraz napisy złożone z "ab" powielonego
dowolną liczbę razy.

NAME: alt_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task219 import alt_automaton

class Task219Test(unittest.TestCase):
    """Testy do zadania 219"""

    def test_simple(self):
        """Prosty test."""

        automaton = alt_automaton()

        self.assertTrue(automaton.accepts("abababab"))
        self.assertTrue(automaton.accepts("abcabc"))
        self.assertTrue(automaton.accepts("abc"))
        self.assertTrue(automaton.accepts("ab"))
        self.assertTrue(automaton.accepts(""))
        self.assertTrue(automaton.accepts("abab"))
        self.assertTrue(automaton.accepts("abcabcabcabcabcabcabcabc"))

        self.assertFalse(automaton.accepts("ba"))
        self.assertFalse(automaton.accepts("abca"))
        self.assertFalse(automaton.accepts("aba"))
        self.assertFalse(automaton.accepts("ababc"))
        self.assertFalse(automaton.accepts("abcab"))

if __name__ == '__main__':
    unittest.main()
