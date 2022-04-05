#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 203

Napisz funkcję `get_number_of_transitions(automaton, symbol)`, która
oblicza liczbę przejść automatu etykietowanych zadanym symbolem.
Należy używać metod klasy (nie odwoływać się bezpośrednio do pól!).


NAME: get_number_of_transitions
PARAMS: automaton, char
RETURN: int
POINTS: 3
"""

import unittest
from Task203 import get_number_of_transitions
from deterministic_automaton import DeterministicAutomaton

class Task203Test(unittest.TestCase):
    """Testy do zadania 203"""

    def test_simple(self):
        """Prosty test."""

        automaton = DeterministicAutomaton()

        state_a = automaton.add_state()
        state_b = automaton.add_state()
        state_c = automaton.add_state()

        automaton.mark_as_initial(state_b)
        automaton.mark_as_final(state_a)

        self.assertEqual(get_number_of_transitions(automaton, 'b'), 0)

        automaton.add_transition(state_b, 'a', state_a)

        self.assertEqual(get_number_of_transitions(automaton, 'a'), 1)
        self.assertEqual(get_number_of_transitions(automaton, 'b'), 0)

        automaton.add_transition(state_b, 'b', state_a)
        automaton.add_transition(state_a, 'b', state_b)
        automaton.add_transition(state_c, 'b', state_a)

        self.assertEqual(get_number_of_transitions(automaton, 'b'), 3)

if __name__ == '__main__':
    unittest.main()
