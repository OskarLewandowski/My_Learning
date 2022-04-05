# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 200."""

from deterministic_automaton import DeterministicAutomaton


def abc_automaton():
    """Zwraca automat akceptujący aXc gdzie X zawiera dowolną liczbę znaków b """

    automat = DeterministicAutomaton()

    q0 = automat.add_state()
    q1 = automat.add_state()
    q2 = automat.add_state()

    automat.add_transition(q0, 'a', q1)
    automat.add_transition(q1, 'b', q1)
    automat.add_transition(q1, 'c', q2)

    automat.mark_as_initial(q0)
    automat.mark_as_final(q2)

    return automat


if __name__ == '__main__':
    automat = abc_automaton()
    print(automat.accepts("abbbbbbbbbbbc"))
