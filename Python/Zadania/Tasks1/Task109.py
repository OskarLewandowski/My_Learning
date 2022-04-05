# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 109"""


def count_yes_lines(filename):
    """Zwraca liczbę wystapien frazy "YES\n" """
    count = 0
    file = open(filename, "r")
    if(file.readable()):
        text = file.readlines()
        file.close()
        for x in text:
            if(x == "YES\n"):
                count = count + 1
    return count



if __name__ == '__main__':
    print(count_yes_lines("Task109Test.dat.txt"))
