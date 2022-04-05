#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 108

Napisz funkcję `pokemon_speak`, która zamienia w podanym napisie co
drugą literę na wielką. Np. `pokemon_speak('pokemon')` powinno zwrócić
'PoKeMoN'.

NAME: pokemon_speak
PARAMS: string
RETURN: string
POINTS: 1
"""

import unittest
from Task108 import pokemon_speak

class Task108Test(unittest.TestCase):
    """Testy do zadania 108."""

    def test_special_cases(self):
        """Przypadki szczególne."""
        self.assertEqual(pokemon_speak(''), '')
        self.assertEqual(pokemon_speak('x'), 'X')
        self.assertEqual(pokemon_speak('X'), 'X')
        self.assertEqual(pokemon_speak('1337'), '1337')

    def test_standard_cases(self):
        """Standardowe przypadki."""
        self.assertEqual(pokemon_speak('pokemon'), 'PoKeMoN')
        self.assertEqual(pokemon_speak('do not want'), 'Do nOt wAnT')
        self.assertEqual(pokemon_speak('POKEMON'), 'POKEMON')

if __name__ == '__main__':
    unittest.main()
