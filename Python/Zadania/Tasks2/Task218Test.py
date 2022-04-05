#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 218

Napisz funkcję `binary_list_automaton()`, która
tworzy i zwraca automat, który akceptuje
napisy złożone z liczb zapisanych binarnie
(bez zbędnych zer na początku) oddzielonych dwukropkami.
Akceptowana powinna być także pojedyncza liczba.

NAME: binary_list_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task218 import binary_list_automaton

class Task218Test(unittest.TestCase):
    """Testy do zadania 218"""

    def test_simple(self):
        """Prosty test."""

        automaton = binary_list_automaton()

        self.assertTrue(automaton.accepts("100:11:11101"))
        self.assertTrue(automaton.accepts("1"))
        self.assertTrue(automaton.accepts("0:110"))

        self.assertFalse(automaton.accepts(""))
        self.assertFalse(automaton.accepts("010:110"))
        self.assertFalse(automaton.accepts("2"))
        self.assertFalse(automaton.accepts("100::11:11101"))
        self.assertFalse(automaton.accepts("100:11:11101:"))
        self.assertFalse(automaton.accepts(":100:11:11101"))

if __name__ == '__main__':
    unittest.main()
