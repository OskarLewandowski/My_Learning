#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 320

Napisać funkcję is_domain_name(string), która sprawdza, czy
napis reprezentuje nazwę domenową. Zakładamy, że nazwa domenowa
składa się z 2 lub 3 członów oddzielonych kropkami. Każdy człon
to ciąg małych liter.

NAME: is_domain_name
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task320 import is_domain_name

class Task320Test(unittest.TestCase):
    """Testy do zadania 320"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_domain_name("www.haha.bla.pl"))
        self.assertTrue(is_domain_name("foo.tv"))
        self.assertTrue(is_domain_name("bla.pl"))
        self.assertFalse(is_domain_name("bla1.pl"))
        self.assertTrue(is_domain_name("www.bla.pl"))
        self.assertFalse(is_domain_name("foo..tv"))
        self.assertTrue(is_domain_name("z.z"))
        self.assertTrue(is_domain_name("x.y.z"))
        self.assertFalse(is_domain_name("foo.pl."))

if __name__ == '__main__':
    unittest.main()
