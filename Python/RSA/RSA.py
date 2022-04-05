# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

def rsa(dane):

    Dane = open(dane, 'r').read()
    print("Wiadomość: {}\n".format(Dane))
    key = RSA.generate(1024)
    klucz_pub = key.publickey().exportKey()
    klucz_priv = key.exportKey()
    open("klucz_publiczny.txt", 'wb').write(klucz_pub)
    open("klucz_prywatny.txt", 'wb').write(klucz_priv)

    p = key.p
    q = key.q
    n = key.n
    d = key.d
    e = key.e

    #PHI = (p-1)*(q-1)
    m = bytes_to_long(Dane.encode('utf-8'))
    encrypted = pow(m, e, n)
    decrypted = pow(encrypted, d, n)

    print("p={}\nq={}\nn={}\ne={}\nd={}\n".format(p, q, n, d, e))
    print("Wiadomość:\n{} <=> {}\n".format(Dane, m))
    print("Wiadmość zaszyfrowana:\n{}".format(encrypted))
    print("Wiadomość odszyfrowana:\n{}".format(decrypted))
    wynik = long_to_bytes(decrypted)
    open("encrypted.txt", 'w').write(str(encrypted))

    print("\nSprawdzenie:")
    verify = open("encrypted.txt", 'rb').read()
    test = pow(int(verify), d, n)
    if(decrypted == test):
        print("Zgodność prawidłowa")
    else:
        print("Zgodność nieprawidłowa")
    wynik2 = long_to_bytes(test)
    print("Odkodowane wiadomości:\n{} <=> {} {}".format(wynik, wynik2, wynik == wynik2))
    open("decrypted.txt", 'wb').write(wynik2)
    return test

if __name__ == '__main__':
    print(rsa("plain.txt"))