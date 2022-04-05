#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Zadanie 110

Napisz funkcję `words_to_length(infile, outfile)`, która wczytując
wiersze z pliku `infile` i wypisując je do pliku `outfile`, zamienia
wyrazy na liczbę odpowiadającą długości wyrazu. Np. wiersz `this is a
string` zostanie zamieniony na `4 2 1 6`. Zakładamy, że wyrazy
oddzielone są spacjami (np. dla `pies, czyli kot` powinno wyjść `5 5
3`).

NAME: word_to_length
PARAMS: file, file
RETURN: string
POINTS: 1
"""

import unittest
from Task110 import word_to_length

class Task110Test(unittest.TestCase):
    """Testy do zadania 110"""

    def test(self):
        """Prosty test przez porównanie z oczekiwanym wyjściem."""
        infile = open("Task110Test.dat.in.txt", 'r')

        out1  = open("Task110Test.out.txt", 'w')
        word_to_length(infile, out1)
        infile.close()
        out1.close()

        out1  = open("Task110Test.out.txt", 'r')
        out2  = open("Task110Test.dat.out.txt", 'r')

        for line1 in out1:
            line2 = out2.readline()
            self.assertEqual( line1, line2 )

        out1.close()
        out2.close()

if __name__ == '__main__':
    unittest.main()
