#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 211

Napisz funkcję `kot_automaton()`, która tworzy i zwraca automat, który
akceptuje napisy "kos", "kot", "kat", "lot", "lat" i nie akceptuje
żadnych innych napisów.

NAME: kot_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task211 import kot_automaton

class Task211Test(unittest.TestCase):
    """Testy do zadania 211"""

    def test_simple(self):
        """Prosty test."""

        automaton = kot_automaton()

        self.assertTrue(automaton.accepts("kos"))
        self.assertTrue(automaton.accepts("kot"))
        self.assertTrue(automaton.accepts("kat"))
        self.assertTrue(automaton.accepts("lot"))
        self.assertTrue(automaton.accepts("lat"))

        self.assertFalse(automaton.accepts("ko"))
        self.assertFalse(automaton.accepts(""))
        self.assertFalse(automaton.accepts("los"))
        self.assertFalse(automaton.accepts("kota"))


if __name__ == '__main__':
    unittest.main()
