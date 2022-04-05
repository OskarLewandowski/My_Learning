#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 208

Napisz funkcję `twenty_five_automaton()`, która
tworzy i zwraca automat, który akceptuje
napisy reprezentujące liczby podzielne przez 25. Automat
może akceptować napisy zaczynające
nieznaczącymi zerami (np. "075"). Nie powinien akceptować natomiast
samego zera ("0").

NAME: twenty_five_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task208 import twenty_five_automaton

class Task208Test(unittest.TestCase):
    """Testy do zadania 208"""

    def test_simple(self):
        """Prosty test."""

        automaton = twenty_five_automaton()

        self.assertTrue(automaton.accepts("25"))
        self.assertTrue(automaton.accepts("50"))
        self.assertTrue(automaton.accepts("75"))
        self.assertTrue(automaton.accepts("100"))
        self.assertTrue(automaton.accepts("1098375"))
        self.assertTrue(automaton.accepts("333325"))
        self.assertTrue(automaton.accepts("17150"))

        self.assertTrue(automaton.accepts("025"))
        self.assertTrue(automaton.accepts("0000175"))
        self.assertFalse(automaton.accepts("1"))
        self.assertFalse(automaton.accepts("2"))
        self.assertFalse(automaton.accepts("5"))
        self.assertFalse(automaton.accepts("10"))
        self.assertFalse(automaton.accepts("45"))
        self.assertFalse(automaton.accepts("124"))

if __name__ == '__main__':
    unittest.main()
