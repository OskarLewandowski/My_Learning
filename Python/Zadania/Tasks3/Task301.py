# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 301."""

import re


def letter_and_two_digits(text):
    """Sprawdza czy podany napis 'text' zawiera ciąg składający się z wielkiej litery
    i dwóch cyfr """

    return re.search(r'[A-Z][0-9]{2}', text)


if __name__ == '__main__':
    print(letter_and_two_digits("haha39dsdsd"))
