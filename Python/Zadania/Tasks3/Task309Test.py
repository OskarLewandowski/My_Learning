#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 309

Napisać funkcję is_movie_number(string), która sprawdza, czy
napis jest 9-cyfrowym numerem telefonu zapisanym w formacie
"NNN-NNN-NNN" badź "NNN NNN NNN" zaczynającym sie od kombinacji
"555".

NAME: is_movie_number
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task309 import is_movie_number

class Task309Test(unittest.TestCase):
    """Testy do zadania 309"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertFalse(is_movie_number("555 000-000"))
        self.assertFalse(is_movie_number("556 345-667"))
        self.assertFalse(is_movie_number("556 345 6675"))
        self.assertFalse(is_movie_number("055-555-555"))
        self.assertTrue(is_movie_number("555 123 456"))
        self.assertFalse(is_movie_number("505-324-555"))
        self.assertTrue(is_movie_number("555-123-456"))
        self.assertFalse(is_movie_number("555-000 000"))
        self.assertTrue(is_movie_number("555 000 000"))
        self.assertTrue(is_movie_number("555-000-000"))
        self.assertFalse(is_movie_number("556 345 667"))
        self.assertFalse(is_movie_number("551-233-455"))

if __name__ == '__main__':
    unittest.main()
