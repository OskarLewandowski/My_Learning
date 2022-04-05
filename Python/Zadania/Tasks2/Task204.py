# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 204."""


def get_number_of_loops(automat, symbol):
    """Zwraca liczbę pętli w zadanym automacie etykietowanych zadanym symbolem"""

    ilosc_stanow = automat.get_number_of_states()
    ilosc_petli= 0

    for i in range(0, ilosc_stanow):
        if (automat.get_target_state(i, symbol) == i ):
           ilosc_petli = ilosc_petli + 1
    return ilosc_petli


if __name__ == '__main__':
    print("hello")
