# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 107."""


def list_cubed(list):
    """Zwraca sumę sześcianów, jeżeli 'list' jest pusta zwraca 0"""
    cubesSum = 0
    listLength = len(list)
    if(listLength == 0):
        return 0
    else:
        for x in list:
            cubesSum = cubesSum + pow(x, 3)
        return cubesSum



if __name__ == '__main__':
    print(list_cubed([3, 0, -1, 2]))
