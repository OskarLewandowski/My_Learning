# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 304."""

import re


def split_list(text):
    """Zwraca listę powstałą w wyniku podziału napisu. Separatorami mogą być
    przecinki otoczone opcjonalnymi spacjami bądź pojedyncze dwukropki."""

    check = re.split(r'\s*,\s*|:', text)
    return check


if __name__ == '__main__':
    print(split_list("foo, bar   , sss:s"))
