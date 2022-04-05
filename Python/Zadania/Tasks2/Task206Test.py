#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 206

Napisz funkcję `big_no_automaton()`, która tworzy i zwraca automat,
który akceptuje "Big NO!" tj. napisy typu "NOO...OO!", gdzie "O"
powtarza się przynajmniej 5 razy (zob.
http://tvtropes.org/pmwiki/pmwiki.php/Main/BigNo).

NAME: big_no_automaton
PARAMS: -
RETURN: DeterministicAutomaton
POINTS: 8
"""

import unittest
from Task206 import big_no_automaton

class Task206Test(unittest.TestCase):
    """Testy do zadania 206"""

    def test_simple(self):
        """Prosty test."""

        automaton = big_no_automaton()

        self.assertTrue(automaton.accepts("NOOOOO!"))
        self.assertTrue(automaton.accepts("NOOOOOOOOOOOOOOOO!"))
        self.assertFalse(automaton.accepts("NOOOO!"))
        self.assertFalse(automaton.accepts("NOOOOOO!!!!!!"))
        self.assertFalse(automaton.accepts("NOOOOOO"))
        self.assertFalse(automaton.accepts("ONOOOOO!"))
        self.assertFalse(automaton.accepts(""))

if __name__ == '__main__':
    unittest.main()
