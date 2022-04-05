import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Dane początkowe
k1 = 1
k2 = 2
m = 1
h = 0.05

x0 = 10
vx0 = 30
y0 = 10
vy0 = 0

w1 = math.sqrt(k1/m)
w2 = math.sqrt(k2/m)

A1 = math.sqrt((vx0*vx0)/(w1*w1) + (x0*x0))
A2 = math.sqrt((vy0*vy0)/(w2*w2) + (y0*y0))

iloscPunktow = 1000

#oś XY
setXl = -100
setXr = 100
setYl = -100
setYr = 100

if(vx0 <= 0):
   fi1 = math.acos(x0/A1) * 180/math.pi
else:
   fi1 = -math.acos(x0/A1) * 180/math.pi

if(vy0 <= 0):
   fi2 = math.acos(y0/A2) * 180/math.pi
else:
   fi2 = -math.acos(y0/A2) * 180/math.pi

#Wypisanie danych poczatkowych
print("X:\nk1 = {0}\nm = {1}\nh = {2}\nx0 = {3}\nvx0 = {4}\nw1 = {5}\nA1 = {6}\nfi1 = {7}"
      .format(k1, m, h, x0, vx0, w1, A1, fi1))
print("\nY:\nk2 = {0}\nm = {1}\nh = {2}\ny0 = {3}\nvy0 = {4}\nw2 = {5}\nA2 = {6}\nfi2 = {7}"
      .format(k2, m, h, y0, vy0, w2, A2, fi2))
print("\nIlosć punktów = {0}".format(iloscPunktow))

#Czas
time = []
for i in range(0, iloscPunktow+1):
    time.append(round((i*h), 2))
    #print(time[i])

#rozwiazanie dokladne listy oraz wartosci poczatkowe
dokladneX = []
dokladneY = []
dokladneVX = []
dokladneVY = []
dokladneX.append(x0)
dokladneY.append(y0)
dokladneVX.append(vx0)
dokladneVY.append(vy0)

#metoda eulera listy oraz wartosci poczatkowe
eulerX = []
eulerY = []
eulerVX = []
eulerVY = []
eulerX.append(x0)
eulerY.append(y0)
eulerVX.append(vx0)
eulerVY.append(vy0)

#metoda punktu posredniego listy oraz wartosci poczatkowe
posredniaX = []
posredniaY = []
posredniaVX = []
posredniaVY = []
posredniaX.append(x0)
posredniaY.append(y0)
posredniaVX.append(vx0)
posredniaVY.append(vy0)

#metoda verleta listy oraz wartosci poczatkowe
verletX = []
verletY = []
verletVX = []
verletVY = []
verletX.append(x0)
verletY.append(y0)
verletVX.append(vx0)
verletVY.append(vy0)

#metoda beemana listy oraz wartosci poczatkowe
beemanX = []
beemanY = []
beemanVX = []
beemanVY = []
beemanX.append(x0)
beemanY.append(y0)
beemanVX.append(vx0)
beemanVY.append(vy0)

#uzupelnianie list
for i in range(1, iloscPunktow+1):
    #dokladna
    dokX = A1 * math.cos(w1 * time[i] + fi1 * math.pi / 180)
    dokY = A2 * math.cos(w2 * time[i] + fi2 * math.pi / 180)
    dokVX = -A1 * w1 * math.sin(w1 * time[i] + fi1 * math.pi/180)
    dokVY = -A2 * w2 * math.sin(w2 * time[i] + fi2 * math.pi/180)
    dokladneX.append(dokX)
    dokladneY.append(dokY)
    dokladneVX.append(dokVX)
    dokladneVY.append(dokVY)
    #euler
    eulX = eulerX[i - 1] + eulerVX[i - 1] * h
    eulY = eulerY[i - 1] + eulerVY[i - 1] * h
    eulVX = eulerVX[i - 1] - (w1 * w1) * eulerX[i - 1] * h
    eulVY = eulerVY[i - 1] - (w2 * w2) * eulerY[i - 1] * h
    eulerX.append(eulX)
    eulerY.append(eulY)
    eulerVX.append(eulVX)
    eulerVY.append(eulVY)
    #posrednia
    posX = posredniaX[i-1] + posredniaVX[i-1] * h - 0.5 * (w1 * w1) * posredniaX[i-1] * (h * h)
    posY = posredniaY[i-1] + posredniaVY[i-1] * h - 0.5 * (w2 * w2) * posredniaY[i-1] * (h * h)
    posVX = posredniaVX[i-1] - (w1 * w1) * posredniaX[i-1] * h
    posVY = posredniaVY[i-1] - (w2 * w2) * posredniaY[i-1] * h
    posredniaX.append(posX)
    posredniaY.append(posY)
    posredniaVX.append(posVX)
    posredniaVY.append(posVY)
    #verlet
    verX = verletX[i - 1] + verletVX[i - 1] * h - 0.5 * (w1 * w1) * verletX[i - 1] * (h * h)
    verletX.append(verX)
    verY = verletY[i - 1] + verletVY[i - 1] * h - 0.5 * (w2 * w2) * verletY[i - 1] * (h * h)
    verletY.append(verY)
    verVX = verletVX[i - 1] - 0.5 * (w1 * w1) * (verletX[i - 1] + verletX[i]) * h
    verletVX.append(verVX)
    verVY = verletVY[i - 1] - 0.5 * (w2 * w2) * (verletY[i - 1] + verletY[i]) * h
    verletVY.append(verVY)
    #beeman
    # z verleta liczone
    if(i == 1):
        beemanX.append(verletX[1])
        beemanY.append(verletY[1])
        beemanVX.append(verletVX[1])
        beemanVY.append(verletVY[1])
    else:
        bemX = beemanX[i - 1] + beemanVX[i - 1] * h + (w1 * w1) * (beemanX[i - 2] - 4 * beemanX[i - 1]) * (h * h)/6
        beemanX.append(bemX)
        bemVX = beemanVX[i - 1] + (w1 * w1) * (beemanX[i - 2] - 5 * beemanX[i - 1] - 2 * beemanX[i]) * h/6
        beemanVX.append(bemVX)
        bemY = beemanY[i - 1] + beemanVY[i - 1] * h + (w2 * w2) * (beemanY[i - 2] - 4 * beemanY[i - 1]) * (h * h)/6
        beemanY.append(bemY)
        bemVY = beemanVY[i - 1] + (w2 * w2) * (beemanY[i - 2] - 5 * beemanY[i - 1] - 2 * beemanY[i]) * h/6
        beemanVY.append(bemVY)

#Animacja
xdata = []
ydata = []

xdata2 = []
ydata2 = []

xdata3 = []
ydata3 = []

xdata4 = []
ydata4 = []

xdata5 = []
ydata5 = []

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
fig, ax = plt.subplots()
ax.set_xlim(setXl, setXr)
ax.set_ylim(setYl, setYr)
plt.title("Oscylator harmoniczny 2D-XY, porównanie rozwiązań numerycznych", fontdict=font1)
plt.xlabel("X", fontdict = font2)
plt.ylabel("Y", fontdict = font2)

line, = ax.plot(0, 0, '.') #niebieski
line2, = ax.plot(0, 0, 'r.') #czerwony
line3, = ax.plot(0, 0, 'g.') #zielony
line4, = ax.plot(0, 0, 'y.') #żółty
line5, = ax.plot(0, 0, 'm.') #fioletowy

line.set_label('rozwiązanie Dokładne')
line2.set_label('metoda Eulera')
line3.set_label('metoda pkt. Pośredniego')
line4.set_label('metoda Verleta')
line5.set_label('metoda Beemana')
ax.legend()

def animation_frame(i):
    xdata.append(dokladneX[i])
    ydata.append(dokladneY[i])

    xdata2.append(eulerX[i])
    ydata2.append(eulerY[i])

    xdata3.append(posredniaX[i])
    ydata3.append(posredniaY[i])

    xdata4.append(verletX[i])
    ydata4.append(verletY[i])

    xdata5.append(beemanX[i])
    ydata5.append(beemanY[i])

    line.set_xdata(xdata)
    line.set_ydata(ydata)

    line2.set_xdata(xdata2)
    line2.set_ydata(ydata2)

    line3.set_xdata(xdata3)
    line3.set_ydata(ydata3)

    line4.set_xdata(xdata4)
    line4.set_ydata(ydata4)

    line5.set_xdata(xdata5)
    line5.set_ydata(ydata5)
    return line, line2, line3, line4, line5,

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(0, iloscPunktow + 1, 1), interval = 5)
plt.show()