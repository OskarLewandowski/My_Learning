import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Dane początkowe
k1 = 1
m = 1
h = 0.05

x0 = 10
vx0 = 0

w1 = math.sqrt(k1/m)
A1 = math.sqrt((vx0*vx0)/(w1*w1) + (x0*x0))

iloscPunktow = 1000

#oś XY
setXl = 0
setXr = 55
setYl = 49.95
setYr = 50.04

if(vx0 <= 0):
   fi1 = math.acos(x0/A1) * 180/math.pi
else:
   fi1 = -math.acos(x0/A1) * 180/math.pi

#Wypisanie danych poczatkowych
print("\nk1 = {0}\nm = {1}\nh = {2}\nx0 = {3}\nvx0 = {4}\nw1 = {5}\nA1 = {6}\nfi1 = {7}"
      .format(k1, m, h, x0, vx0, w1, A1, fi1))
print("\nIlosć punktów = {0}".format(iloscPunktow))

#Czas
time = []
for i in range(0, iloscPunktow+1):
    time.append(round((i*h), 2))
    #print(time[i])

#rozwiazanie dokladne listy oraz wartosci poczatkowe
dokladneX = []
dokladneVX = []
dokladneX.append(x0)
dokladneVX.append(vx0)
dokladneE = []

#metoda eulera listy oraz wartosci poczatkowe
eulerX = []
eulerVX = []
eulerX.append(x0)
eulerVX.append(vx0)
eulerE = []

#metoda punktu posredniego listy oraz wartosci poczatkowe
posredniaX = []
posredniaVX = []
posredniaX.append(x0)
posredniaVX.append(vx0)
posredniaE = []

#metoda verleta listy oraz wartosci poczatkowe
verletX = []
verletVX = []
verletX.append(x0)
verletVX.append(vx0)
verletE = []

#metoda beemana listy oraz wartosci poczatkowe
beemanX = []
beemanVX = []
beemanX.append(x0)
beemanVX.append(vx0)
beemanE = []

#uzupelnianie list
for i in range(1, iloscPunktow+1):
    #dokladna
    dokX = A1 * math.cos(w1 * time[i] + fi1 * math.pi / 180)
    dokVX = -A1 * w1 * math.sin(w1 * time[i] + fi1 * math.pi/180)
    dokladneX.append(dokX)
    dokladneVX.append(dokVX)
    #euler
    eulX = eulerX[i - 1] + eulerVX[i - 1] * h
    eulVX = eulerVX[i - 1] - (w1 * w1) * eulerX[i - 1] * h
    eulerX.append(eulX)
    eulerVX.append(eulVX)
    #posrednia
    posX = posredniaX[i-1] + posredniaVX[i-1] * h - 0.5 * (w1 * w1) * posredniaX[i-1] * (h * h)
    posVX = posredniaVX[i-1] - (w1 * w1) * posredniaX[i-1] * h
    posredniaX.append(posX)
    posredniaVX.append(posVX)
    #verlet
    verX = verletX[i - 1] + verletVX[i - 1] * h - 0.5 * (w1 * w1) * verletX[i - 1] * (h * h)
    verletX.append(verX)
    verVX = verletVX[i - 1] - 0.5 * (w1 * w1) * (verletX[i - 1] + verletX[i]) * h
    verletVX.append(verVX)
    #beeman
    # z verleta liczone
    if(i == 1):
        beemanX.append(verletX[1])
        beemanVX.append(verletVX[1])
    else:
        bemX = beemanX[i - 1] + beemanVX[i - 1] * h + (w1 * w1) * (beemanX[i - 2] - 4 * beemanX[i - 1]) * (h * h)/6
        beemanX.append(bemX)
        bemVX = beemanVX[i - 1] + (w1 * w1) * (beemanX[i - 2] - 5 * beemanX[i - 1] - 2 * beemanX[i]) * h/6
        beemanVX.append(bemVX)

#energia

for i in range(0, iloscPunktow+1):
    dokE = 0.5 * k1 * (A1*A1)
    dokladneE.append(dokE)
    eulE = m * (eulerVX[i] * eulerVX[i])/2 + k1 * (eulerX[i] * eulerX[i]/2)
    eulerE.append(eulE)
    posE = m * (posredniaVX[i] * posredniaVX[i])/2 + k1 * (posredniaX[i] * posredniaX[i]/2)
    posredniaE.append(posE)
    verE = m * (verletVX[i] * verletVX[i])/2 + k1 * (verletX[i] * verletX[i]/2)
    verletE.append(verE)
    bemE = m * (beemanVX[i] * beemanVX[i])/2 + k1 * (beemanX[i] * beemanX[i]/2)
    beemanE.append(bemE)

#Animacja
xdata = []
ydata = []

xdata2 = []
ydata2 = []

xdata3 = []
ydata3 = []


font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
fig, ax = plt.subplots()
ax.set_xlim(setXl, setXr)
ax.set_ylim(setYl, setYr)
plt.title("Energia całkowita oscylatora", fontdict=font1)
plt.xlabel("t", fontdict = font2)
plt.ylabel("E", fontdict = font2)

line, = ax.plot(0, 0, '.') #niebieski
line2, = ax.plot(0, 0, 'r.') #czerwony
line3, = ax.plot(0, 0, 'g.') #zielony

line.set_label('rozwiązanie Dokładne')
line2.set_label('metoda Verleta')
line3.set_label('metoda Beemana')
ax.legend()

def animation_frame(i):
    xdata.append(time[i])
    ydata.append(dokladneE[i])

    xdata2.append(time[i])
    ydata2.append(verletE[i])

    xdata3.append(time[i])
    ydata3.append(beemanE[i])

    line.set_xdata(xdata)
    line.set_ydata(ydata)

    line2.set_xdata(xdata2)
    line2.set_ydata(ydata2)

    line3.set_xdata(xdata3)
    line3.set_ydata(ydata3)

    return line, line2, line3,

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(0, iloscPunktow + 1, 1), interval = 5)
plt.show()