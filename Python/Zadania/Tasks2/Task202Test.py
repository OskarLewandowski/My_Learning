#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 202

Napisz funkcję `get_number_of_final_states(automaton)`, która oblicza
liczbę stanów końcowych automatu. Należy używać metod klasy (nie
odwoływać się bezpośrednio do pól!).


NAME: get_number_of_final_states
PARAMS: automaton
RETURN: int
POINTS: 2
"""

import unittest
from Task202 import get_number_of_final_states
from deterministic_automaton import DeterministicAutomaton

class Task202Test(unittest.TestCase):
    """Testy do zadania 202"""

    def test_simple(self):
        """Prosty test."""

        automaton = DeterministicAutomaton()

        state_a = automaton.add_state()
        state_b = automaton.add_state()
        state_c = automaton.add_state()

        automaton.mark_as_initial(state_b)

        self.assertEqual(get_number_of_final_states(automaton), 0)

        automaton.mark_as_final(state_a)

        self.assertEqual(get_number_of_final_states(automaton), 1)

        automaton.mark_as_final(state_c)
        automaton.mark_as_final(state_b)

        self.assertEqual(get_number_of_final_states(automaton), 3)


if __name__ == '__main__':
    unittest.main()
