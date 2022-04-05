#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 307

Stworzyć funkcję `extract_phone_number(string_to_be_checked), która wydobywa z zadanego napisu numer telefonu. Zakładamy, że numer telefonu składa się z dwóch cyfr opcjonalnie poprzedzonych zerem, po których następuje spacja i 7 cyfr w formacie N-NNN-NNN. Jeśli zadany napis nie zawiera numeru telefonu, należy zwrócić "<NONE>".

NAME: is_phone_number
PARAMS: string
RETURN: bool
POINTS: 9
"""

import unittest

from Task307 import extract_phone_number

class Task307Test(unittest.TestCase):
    """Testy do zadania 307"""

    def test_simple(self):
        """Podstawowy test."""

        self.assertEqual(extract_phone_number("bla 61 5-555-555xyz"), "61 5-555-555");
        self.assertEqual(extract_phone_number("bla 061 5-555-555xyz"), "061 5-555-555");
        self.assertEqual(extract_phone_number("bla 61 5-555-45xyz"), "<NONE>");
        self.assertEqual(extract_phone_number("bla 5-555-4555xyz"), "<NONE>");

if __name__ == '__main__':
    unittest.main()
