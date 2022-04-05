# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 303."""

import re


def divisable_by_four(text):
    """Sprawdza, czy podany napis reprezentuje liczbę nieujemną podzielną
    przez 4 Zwraca True jeśli liczba jest nieujemna i poddzielne przez 4."""

    return re.search(r'^([048]|\d*[02468][048]|\d*[13579][26])$', text)


if __name__ == '__main__':
    print(divisable_by_four("32"))
