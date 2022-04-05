import random

""" Wyznaczyć liczbę Pi jako średnią 100 próbek przy losowaniu dla każdej próbki 
100,1000 lub 10000 punktów. Obliczyć rozrzut-odch, standardowe dla tych trzech przypadków"""

random.seed()
n = 0
k = 0
probka100 = []
probka1000 = []
probka10000 = []

for a in range(0, 3):
    k = 0
    if(a == 0):
        n = 100
    elif(a == 1):
        n = 1000
    else:
        n = 10000
    for b in range(0, 100):
        k = 0
        for c in range(0, n):
            x = random.random()
            y = random.random()
            if x * x + y * y <= 1:
                k += 1
        p = 4 * k / n
        if (a == 0):
            probka100.append(p)
        elif (a == 1):
            probka1000.append(p)
        else:
            probka10000.append(p)

#1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
suma100 = 0
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Próbka 100 - początkowe 10 próbek:\n{0}".format(probka100[0:10]))
print()

for i in probka100:
    suma100 = i + suma100

srednia100 = suma100 / len(probka100)
print("Średnia arytmetyczna = ", srednia100)

gora100 = 0
for i in probka100:
    wynik1 = (i - srednia100) * (i - srednia100)
    gora100 = wynik1 + gora100

odchylenie100 = gora100/srednia100
print("Odchylenie standardowe = √{0}".format(odchylenie100))


#2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
suma1000 = 0
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Próbka 1000 - początkowe 10 próbek:\n{0}".format(probka1000[0:10]))
print()

for i in probka1000:
    suma1000 = i + suma1000

srednia1000 = suma1000 / len(probka1000)
print("Średnia arytmetyczna = ", srednia1000)

gora1000 = 0
for i in probka1000:
    wynik2 = (i - srednia1000) * (i - srednia1000)
    gora1000 = wynik2 + gora1000

odchylenie1000 = gora1000/srednia1000
print("Odchylenie standardowe = √{0}".format(odchylenie1000))


#3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
suma10000 = 0
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Próbka 10000 - początkowe 10 próbek:\n{0}".format(probka10000[0:10]))
print()

for i in probka10000:
    suma10000 = i + suma10000

srednia10000 = suma10000 / len(probka10000)
print("Średnia arytmetyczna = ", srednia10000)

gora10000 = 0
for i in probka10000:
    wynik3 = (i - srednia10000) * (i - srednia10000)
    gora10000 = wynik3 + gora10000

odchylenie10000 = gora10000/srednia10000
print("Odchylenie standardowe = √{0}".format(odchylenie10000))
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")