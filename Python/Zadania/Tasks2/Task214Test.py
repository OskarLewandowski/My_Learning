#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 214

Napisz funkcję `hex_automaton()`, która tworzy i zwraca automat
akceptujący napisy reprezentujące liczby szesnastkowo.
Cyfry szesnastkowe mogą być reprezentowane za pomocą małych
bądź wielkich liter, ale konsekwentnie ("a0f9" i "A0F9" ma być akceptowane,
"a0F9" i "A0f9" - nie). Liczba może zawierać zera nieznaczące na początku.

NAME: hex_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task214 import hex_automaton

class Task214Test(unittest.TestCase):
    """Testy do zadania 214"""

    def test_simple(self):
        """Prosty test."""

        automaton = hex_automaton()

        self.assertTrue(automaton.accepts("a0f9"))
        self.assertTrue(automaton.accepts("A0F9"))
        self.assertTrue(automaton.accepts("0"))
        self.assertTrue(automaton.accepts("0B000"))
        self.assertTrue(automaton.accepts("DDDD"))
        self.assertTrue(automaton.accepts("baca"))

        self.assertFalse(automaton.accepts("gg"))
        self.assertFalse(automaton.accepts("a0F9"))
        self.assertFalse(automaton.accepts("A0f9"))
        self.assertFalse(automaton.accepts("Baca"))


if __name__ == '__main__':
    unittest.main()
