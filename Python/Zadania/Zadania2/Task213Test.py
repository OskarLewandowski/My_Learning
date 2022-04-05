#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 213

Napisz funkcję `tricky_automaton()`, która tworzy i zwraca automat
akceptujący wszystkie napisy złożone z napisu "abc" powtórzonego
dowolną liczbę razy (ale przynajmniej raz) oraz napis "a".

NAME: tricky_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task213 import tricky_automaton

class Task213Test(unittest.TestCase):
    """Testy do zadania 213"""

    def test_simple(self):
        """Prosty test."""

        automaton = tricky_automaton()

        self.assertTrue(automaton.accepts("a"))
        self.assertTrue(automaton.accepts("abc"))
        self.assertTrue(automaton.accepts("abcabc"))
        self.assertTrue(automaton.accepts("abcabcabcabcabc"))

        self.assertFalse(automaton.accepts("ab"))
        self.assertFalse(automaton.accepts(""))
        self.assertFalse(automaton.accepts("abca"))
        self.assertFalse(automaton.accepts("abcabca"))


if __name__ == '__main__':
    unittest.main()
