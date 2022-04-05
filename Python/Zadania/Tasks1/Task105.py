# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 105."""


def is_almost_prime(a, b):
    """Zwraca False gdy 'a' jest ujemna lub dzieli się przez liczby z przedziału od 2 do 'b'
    w przciwnym razie zwraca True"""

    if(a <= 0):
        return False
    else:
        for x in range(2, b+1):
            if(a % x == 0):
                return False
        return True



if __name__ == '__main__':
    print(is_almost_prime(35, 5))
