

def rozklad(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki


def rsa(sID):
    c = sID
    n = 2791273
    e = 13

    czynniki = rozklad(n)

    p = czynniki[0]
    q = czynniki[1]
    Phi = (p - 1) * (q - 1)
    d = pow(e, -1, Phi)
    m = pow(c, d, n)

    print("c={}\nn={}\ne={}\np={}\nq={}\nPhi={}\nd={}\nm={}".format(c, n, e, p, q, Phi, d, m))
    print("\nSprawdzenie:")
    print("{} == {}^{} (mod {})".format(c, m, e, n))
    spr = pow(m, e, n)
    print("Wynik: {}".format(c == spr))
    return m


if __name__ == '__main__':
    print(rsa(448700))