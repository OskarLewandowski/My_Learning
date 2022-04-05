# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 201."""


def is_initial_state_a_final_one(automat):
    """Zwraca True jeśli stan początkowy automatu jest równocześnie stanem końcowym."""

    stan_poczatkowy = automat.get_initial_state()
    if automat.is_final_state(stan_poczatkowy):
        return True
    else:
        return False


if __name__ == '__main__':
    print("hello")
