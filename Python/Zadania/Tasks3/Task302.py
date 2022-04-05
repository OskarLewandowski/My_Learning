# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 302."""

import re


def extract_minutes(text):
    """Z podanego napisu reprezentującego godzinę
    w formacie typu "9:13", "18:44" wyciąga minuty.
    Funkcja  zwraca napis "<NONE>", jeśli podany
    napis nie jest godziną."""

    check = re.search(r'^([0-9]|[1][0-9]|[2][0-3]):(?P<minutes>[0-5][0-9])$', text)
    if check:
        return check.group("minutes")
    else:
        return "<NONE>"

if __name__ == '__main__':
    print(extract_minutes("9:13"))
