# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 203."""


def get_number_of_transitions(automat, symbol):
    """Zwraca liczbę przejść automatu etykietowanych zadanym symbolem."""

    x = automat.get_number_of_states()
    y = 0

    for i in range(0, x):
        if automat.get_target_state(i, symbol) != None:
           y = y + 1
    return y


if __name__ == '__main__':
    print("hello")
