# -*- coding: utf-8 -*-
def xor(dane, klucz, numer):

    tablicaLosowyByte = bytearray(open(dane, 'rb').read())
    tablicaTajnyByte = bytearray(open(klucz, 'rb').read())

    print("\nLosowy ciąg = {0} długość = {1}" .format(tablicaLosowyByte, len(tablicaLosowyByte)))
    print("Klucz tajny = {0} długość = {1}\n" .format(tablicaTajnyByte, len(tablicaTajnyByte)))

    wynik = bytearray()

    for i in range(len(tablicaTajnyByte)):
        box = tablicaLosowyByte[i] ^ tablicaTajnyByte[i]
        wynik.append(box)
        print("Nr:{0} Byte: {1} ^ {2} Wynik: {3}\n"
        .format(i+1, tablicaLosowyByte[i], tablicaTajnyByte[i], wynik[i]))

    nazwaPliku = "wynik" + str(numer) + ".txt"
    open(nazwaPliku, 'wb').write(wynik)
    return wynik

if __name__ == '__main__':
    print(xor("dane.txt", "klucz.bin", "448700"))
