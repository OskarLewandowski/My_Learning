#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 304

Napisz funkcję `split_list(string)`, która która zwraca listę powstałą
w wyniku podziału napisu. Separatorami mogą być przecinki otoczone
opcjonalnymi spacjami bądź pojedyncze dwukropki.


NAME: split_list
PARAMS: string
RETURN: list
POINTS: 2
"""

import unittest
from Task304 import split_list

class Task304Test(unittest.TestCase):
    """Testy do zadania 304"""

    def test_simple(self):
        """Prosty test."""
        self.assertEqual(
            split_list("foo, bar   , sss:s"),
            ['foo', 'bar', 'sss', 's'])


        self.assertEqual(
            split_list("foo"),
            ['foo'])

        self.assertEqual(
            split_list("bla  : bla"),
            ['bla  ', ' bla'])


if __name__ == '__main__':
    unittest.main()
