import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Dane początkowe
g = 9.80665
m = 1
h = 0.02
c = 1

x0 = 0
vx0 = 40
y0 = 0
vy0 = 10
v = math.sqrt((vx0*vx0)+(vy0*vy0))
alfa = math.asin(vy0/v)*180/math.pi

iloscPunktow = 1000

#oś XY
setXl = 0
setXr = 90
setYl = 0
setYr = 6

#Wypisanie danych poczatkowych
print("\ng = {0}\nm = {1}\nh = {2}\nc = {3}\nx0 = {4}\nvx0 = {5}\ny0 = {6}\nvy0 = {7}\nv = {8}\nalfa = {9}"
      .format(g, m, h, c, x0, vx0, y0, vy0, v, alfa))
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
eulerAX = []
eulerAX.append(-c*vx0)
eulerAY = []
eulerAY.append(-g-c*vy0)

#metoda beemana listy oraz wartosci poczatkowe
beemanX = []
beemanY = []
beemanVX = []
beemanVY = []
beemanX.append(x0)
beemanY.append(y0)
beemanVX.append(vx0)
beemanVY.append(vy0)
beemanAX = []
beemanAX.append(-c*vx0)
beemanAY = []
beemanAY.append(-g-c*vy0)

for i in range(1, iloscPunktow+1):
    #dokladna
    dokX = x0+vx0*time[i]
    dokladneX.append(dokX)
    dokY = y0 + vy0 * time[i] - 0.5 * g * (time[i] * time[i])
    dokladneY.append(dokY)
    dokVX = vx0
    dokladneVX.append(dokVX)
    dokVY = vy0-g*time[i]
    dokladneVY.append(dokVY)
    #euler
    eulX = eulerX[i - 1] + eulerVX[i - 1] * h
    eulerX.append(eulX)
    eulY = eulerY[i - 1] + eulerVY[i - 1] * h
    eulerY.append(eulY)
    eulVX = eulerVX[i - 1] + eulerAX[i - 1] * h
    eulerVX.append(eulVX)
    eulVY = eulerVY[i - 1] + eulerAY[i - 1] * h
    eulerVY.append(eulVY)
    eulAX = - c * eulerVX[i]
    eulerAX.append(eulAX)
    eulAY = - g - c * eulerVY[i]
    eulerAY.append(eulAY)
    #beeman
    # z eulera liczone
    if(i == 1):
        beemanX.append(eulerX[1])
        beemanY.append(eulerY[1])
        beemanVX.append(eulerVX[1])
        beemanVY.append(eulerVY[1])
        beemanAX.append(-c*beemanVX[1])
        beemanAY.append(-g - c * beemanVY[1])
    else:
        bemX = beemanX[i - 1] + beemanVX[i - 1] * h + (1/6) * (4 * beemanAX[i - 1] - beemanAX[i - 2]) * (h * h)
        beemanX.append(bemX)
        bemY = beemanY[i - 1] + beemanVY[i - 1] * h + (1/6) * (4 * beemanAY[i - 1] - beemanAY[i - 2]) * (h * h)
        beemanY.append(bemY)
        bemVX = beemanVX[i - 1] + beemanAX[i - 1] * h
        beemanVX.append(bemVX)
        bemVY = beemanVY[i - 1] + beemanAY[i - 1] * h
        beemanVY.append(bemVY)
        bemAX = -c * beemanVX[i]
        beemanAX.append(bemAX)
        bemAY = -g - c * beemanVY[i]
        beemanAY.append(bemAY)

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
plt.title("Rzut ukośny", fontdict=font1)
plt.xlabel("t", fontdict = font2)
plt.ylabel("h", fontdict = font2)

line, = ax.plot(0, 0, '.') #niebieski
line2, = ax.plot(0, 0, 'r.') #czerwony
line3, = ax.plot(0, 0, 'g.') #zielony

line.set_label('rozwiązanie Dokładne')
line2.set_label('metoda Eulera')
line3.set_label('metoda Beemana')
ax.legend()

def animation_frame(i):
    xdata.append(dokladneX[i])
    ydata.append(dokladneY[i])

    xdata2.append(eulerX[i])
    ydata2.append(eulerY[i])

    xdata3.append(beemanX[i])
    ydata3.append(beemanY[i])

    line.set_xdata(xdata)
    line.set_ydata(ydata)

    line2.set_xdata(xdata2)
    line2.set_ydata(ydata2)

    line3.set_xdata(xdata3)
    line3.set_ydata(ydata3)

    return line, line2, line3,

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(0, iloscPunktow + 1, 1), interval = 5)
plt.show()