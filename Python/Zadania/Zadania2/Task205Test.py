#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 205

Napisz funkcję `haha_automaton()`, która
tworzy i zwraca automat, który akceptuje śmiechy
tj. napisy typu "hahaha!!!", gdzie ha powtarza
się przynajmniej dwa razy, wykrzyknik występuje dowolną liczbę
razy (przynajmniej raz).

NAME: haha_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task205 import haha_automaton

class Task205Test(unittest.TestCase):
    """Testy do zadania 205"""

    def test_simple(self):
        """Prosty test."""

        automaton = haha_automaton()

        self.assertTrue(automaton.accepts("hahaha!!!!!!!!!"))
        self.assertTrue(automaton.accepts("haha!"))
        self.assertTrue(automaton.accepts("hahahaha!!"))
        self.assertFalse(automaton.accepts("ha!!!!!"))
        self.assertFalse(automaton.accepts("hahaha"))
        self.assertFalse(automaton.accepts("hahoha"))
        self.assertFalse(automaton.accepts("!!haha"))


if __name__ == '__main__':
    unittest.main()
