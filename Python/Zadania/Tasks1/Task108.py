# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 108."""


def pokemon_speak(words):
    """Zamienia w podanym napisie co drugą literę na wielką i zwraca zamieniony tekst"""

    oneUpper = 1
    newWords = ""

    for x in words:
        if(x != ""):
            if(oneUpper == 1 and x!= ""):
                newWords = newWords + x.upper()
                oneUpper = 0
            else:
                newWords = newWords + x
                oneUpper = 1
    return newWords



if __name__ == '__main__':
    print(pokemon_speak('do not want'))
