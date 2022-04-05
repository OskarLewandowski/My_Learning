# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 325."""
"""^((\$[1-9])|(\$[1-9]+[0-9]*))$"""

import re


def is_dollar_sum(text):
    """Sprawdza, czy napis wyraża sumę w dolarach, tj. zaczyna się znakiem dolara,
    poktórym następuje liczba dodatnia (bez zer nieznaczących)."""

    return re.search(r'^(\$[1-9]([0-9]+)?)$', text)


if __name__ == '__main__':
    print(is_dollar_sum("$100"))
