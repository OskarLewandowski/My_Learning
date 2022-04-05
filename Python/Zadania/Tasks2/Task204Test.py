#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 204

Napisz funkcję `get_number_of_loops(automaton, symbol)`, która
oblicza liczbę pętli (tj. przejść od stanu z powrotem do danego
stanu) w zadanym automacie etykietowanych zadanym symbolem.

NAME: get_number_of_loops
PARAMS: automaton, char
RETURN: int
POINTS: 2
"""

import unittest
from Task204 import get_number_of_loops
from deterministic_automaton import DeterministicAutomaton

class Task204Test(unittest.TestCase):
    """Testy do zadania 204"""

    def test_simple(self):
        """Prosty test."""

        automaton = DeterministicAutomaton()

        state_a = automaton.add_state()
        state_b = automaton.add_state()
        state_c = automaton.add_state()

        automaton.mark_as_initial(state_b)
        automaton.mark_as_final(state_a)

        self.assertEqual(get_number_of_loops(automaton, 'b'), 0)

        automaton.add_transition(state_b, 'a', state_a)

        self.assertEqual(get_number_of_loops(automaton, 'a'), 0)
        self.assertEqual(get_number_of_loops(automaton, 'b'), 0)

        automaton.add_transition(state_b, 'b', state_b)
        automaton.add_transition(state_c, 'b', state_c)
        automaton.add_transition(state_a, 'a', state_a)
        automaton.add_transition(state_a, 'b', state_b)

        self.assertEqual(get_number_of_loops(automaton, 'a'), 1)
        self.assertEqual(get_number_of_loops(automaton, 'b'), 2)

if __name__ == '__main__':
    unittest.main()
