# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 103."""


def probability(a):
    """Zwraca 0 jeśli liczba nie reprezentuje prawdopodobieństwa w przeciwnym wypadku zwraca wartość podaną"""
    if a >= 0.0 and a <= 1.0:
        return a
    else:
        return 0



if __name__ == '__main__':
    print(probability(0.69))
