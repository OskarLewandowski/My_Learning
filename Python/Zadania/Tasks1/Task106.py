# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 106"""


def penultimate(list, otherwise):
    """Zwraca 'otherwise' jeśli lista posiada 0 lub 1 element w przeciwnym
    razie zwraca przedostatnią wartość z 'list'"""

    listLength = len(list)

    if(listLength == 0 or listLength == 1):
        return otherwise
    else:
        return list[listLength-2]



if __name__ == '__main__':
    print(penultimate([1, 2, 3, 4, 5, 6], 'blabla'))
