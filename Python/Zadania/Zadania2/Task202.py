# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 202."""


def get_number_of_final_states(automat):
    """Zwraca liczbę stanów końcowych automatu."""


    ilosc_stanow = automat.get_number_of_states()
    ilosc_koncowych = 0

    for i in range(0, ilosc_stanow):
        if automat.is_final_state(i):
            ilosc_koncowych = ilosc_koncowych + 1
    return ilosc_koncowych


if __name__ == '__main__':
    print("hello")
