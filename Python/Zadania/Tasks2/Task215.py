# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 215."""

from deterministic_automaton import DeterministicAutomaton


def four_automaton():
    """Zwraca True jeśli napis jest podzielny przez 4 bez 0 na poczatku np. '004' = False """

    automat = DeterministicAutomaton()

    q0 = automat.add_state()
    q1 = automat.add_state()
    q2 = automat.add_state()
    q3 = automat.add_state()
    q4 = automat.add_state()

    """ q0 """
    # 0 q0 q4 = 4*n
    automat.add_transition(q0, '0', q4)

    # 4 8 q0 q0 = 4*n
    automat.add_transition(q0, '4', q0)
    automat.add_transition(q0, '8', q0)

    # 1 5 9 q0 q1 = 4*n+1
    automat.add_transition(q0, '1', q1)
    automat.add_transition(q0, '5', q1)
    automat.add_transition(q0, '9', q1)

    # 2 6 q0 q2 = 4*n+2
    automat.add_transition(q0, '2', q2)
    automat.add_transition(q0, '6', q2)

    # 3 7 q0 q3 = 4*n+3
    automat.add_transition(q0, '3', q3)
    automat.add_transition(q0, '7', q3)

    """ q1 """
    # 0 4 8 q1 q2
    automat.add_transition(q1, '0', q2)
    automat.add_transition(q1, '4', q2)
    automat.add_transition(q1, '8', q2)

    # 1 5 9 q1 q3
    automat.add_transition(q1, '1', q3)
    automat.add_transition(q1, '5', q3)
    automat.add_transition(q1, '9', q3)

    # 2 6 q1 q0
    automat.add_transition(q1, '2', q0)
    automat.add_transition(q1, '6', q0)

    # 3 7 q1 q1
    automat.add_transition(q1, '3', q1)
    automat.add_transition(q1, '7', q1)

    """ q2 """
    # 0 4 8 q2 q0
    automat.add_transition(q2, '0', q0)
    automat.add_transition(q2, '4', q0)
    automat.add_transition(q2, '8', q0)

    # 1 5 9 q2 q1
    automat.add_transition(q2, '1', q1)
    automat.add_transition(q2, '5', q1)
    automat.add_transition(q2, '9', q1)

    # 2 6 q2 q2
    automat.add_transition(q2, '2', q2)
    automat.add_transition(q2, '6', q2)

    # 3 7 q2 q3
    automat.add_transition(q2, '3', q3)
    automat.add_transition(q2, '7', q3)

    """ q3 """
    # 0 4 8 q3 q2
    automat.add_transition(q3, '0', q2)
    automat.add_transition(q3, '4', q2)
    automat.add_transition(q3, '8', q2)

    # 1 5 9 q3 q3
    automat.add_transition(q3, '1', q3)
    automat.add_transition(q3, '5', q3)
    automat.add_transition(q3, '9', q3)

    # 2 6 q3 q0
    automat.add_transition(q3, '2', q0)
    automat.add_transition(q3, '6', q0)

    # 3 7 q3 q1
    automat.add_transition(q3, '3', q1)
    automat.add_transition(q3, '7', q1)

    automat.mark_as_initial(q0)
    automat.mark_as_final(q0)
    automat.mark_as_final(q4)

    return automat


if __name__ == '__main__':
    automat = four_automaton()
    print(automat.accepts("12200"))
