# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 104."""


def fahrenheit(a):
    """Zwraca -459.67 jeśli liczba jest mniejsza od -273.15 w przeciwnym wypadku przelicza stopnie Celsjusza na
    stopnie Fahrenheita. """

    testValue = float(-273.15)
    returnValue = float(-459.67)
    if(a <= testValue):
        return returnValue
    else:
        convertCelsius = float(((9 / 5) * a + 32))
        return convertCelsius



if __name__ == '__main__':
    print(fahrenheit(-455))
