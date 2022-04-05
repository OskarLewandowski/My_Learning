#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 201

Napisz funkcję `is_initial_state_a_final_one(automaton)`, która
sprawdza, czy stan początkowy automatu jest równocześnie
stanem końcowym. Należy używać metod klasy (nie odwoływać
się bezpośrednio do pól!).

NAME: is_initial_state_a_final_one
PARAMS: automaton
RETURN: bool
POINTS: 2
"""

import unittest
from Task201 import is_initial_state_a_final_one
from deterministic_automaton import DeterministicAutomaton

class Task201Test(unittest.TestCase):
    """Testy do zadania 201"""

    def test_simple(self):
        """Prosty test."""

        automaton = DeterministicAutomaton()

        state_a = automaton.add_state()
        state_b = automaton.add_state()

        automaton.mark_as_initial(state_b)

        self.assertFalse(is_initial_state_a_final_one(automaton))

        automaton.mark_as_final(state_a)

        self.assertFalse(is_initial_state_a_final_one(automaton))

        automaton.mark_as_final(state_b)

        self.assertTrue(is_initial_state_a_final_one(automaton))


if __name__ == '__main__':
    unittest.main()
