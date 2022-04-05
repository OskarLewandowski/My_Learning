import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Dane początkowe
g = 9.80665
m = 1
h = 0.000629
c = 0

x0 = 1
vx0 = 0
y0 = 0
vy0 = 1
v = math.sqrt((vx0*vx0)+(vy0*vy0))
alfa = math.asin(vy0/v)*180/math.pi
G = 1
M = 1

iloscPunktow = 50000

#kotrola wykresu oś XY
setXl = -1.1
setXr = 1.1
setYl = -1.1
setYr = 1.1

#Wypisanie danych poczatkowych
print("\ng = {0}\nm = {1}\nh = {2}\nc = {3}\nx0 = {4}\nvx0 = {5}\ny0 = {6}\nvy0 = {7}\nv = {8}\nalfa = {9}"
      .format(g, m, h, c, x0, vx0, y0, vy0, v, alfa))
print("G = {0}\nM = {1}"
      .format(G, M))
print("\nIlosć punktów = {0}".format(iloscPunktow))

#Czas
time = []
for i in range(0, iloscPunktow+1):
    time.append(round((i*h), 2))
    #print(time[i])

#metoda eulera listy oraz wartosci poczatkowe
eulerX = []
eulerY = []
eulerVX = []
eulerVY = []
eulerX.append(x0)
eulerY.append(y0)
eulerVX.append(vx0)
eulerVY.append(vy0)
eulerR = []
eulerR.append(math.sqrt((x0*x0)+(y0*y0)))
eulerAX = []
eulerAX.append(-(G*M*x0)/(eulerR[0]*eulerR[0]*eulerR[0]))
eulerAY = []
eulerAY.append(-(G*M*y0)/(eulerR[0]*eulerR[0]*eulerR[0]))

#metoda beemana listy oraz wartosci poczatkowe
beemanX = []
beemanY = []
beemanVX = []
beemanVY = []
beemanX.append(x0)
beemanY.append(y0)
beemanVX.append(vx0)
beemanVY.append(vy0)
beemanR = []
beemanR.append(math.sqrt((x0*x0)+(y0*y0)))
beemanAX = []
beemanAX.append(-(G*M*x0)/(beemanR[0]*beemanR[0]*beemanR[0]))
beemanAY = []
beemanAY.append(-(G*M*y0)/(beemanR[0]*beemanR[0]*beemanR[0]))

for i in range(1, iloscPunktow+1):
    #euler
    eulX = eulerX[i - 1] + eulerVX[i - 1] * h
    eulerX.append(eulX)
    eulY = eulerY[i - 1] + eulerVY[i - 1] * h
    eulerY.append(eulY)
    eulVX = eulerVX[i - 1] + eulerAX[i - 1] * h
    eulerVX.append(eulVX)
    eulVY = eulerVY[i - 1] + eulerAY[i - 1] * h
    eulerVY.append(eulVY)
    eulR = math.sqrt((eulerX[i]*eulerX[i])+(eulerY[i]*eulerY[i]))
    eulerR.append(eulR)
    eulAX = -(G*M*eulerX[i])/(eulerR[i]*eulerR[i]*eulerR[i])
    eulerAX.append(eulAX)
    eulAY = -(G*M*eulerY[i])/(eulerR[i]*eulerR[i]*eulerR[i])
    eulerAY.append(eulAY)
    #beeman
    # z eulera liczone
    if(i == 1):
        beemanX.append(eulerX[1])
        beemanY.append(eulerY[1])
        beemanVX.append(eulerVX[1])
        beemanVY.append(eulerVY[1])
        beemanR.append(math.sqrt((beemanX[i] * beemanX[i]) + (beemanY[i] * beemanY[i])))
        beemanAX.append(-(G*M*beemanX[i])/(beemanR[i]*beemanR[i]*beemanR[i]))
        beemanAY.append(-(G*M*beemanY[i])/(beemanR[i]*beemanR[i]*beemanR[i]))
    else:
        bemX = beemanX[i - 1] + beemanVX[i - 1] * h + (1/6) * (4 * beemanAX[i - 1] - beemanAX[i - 2]) * (h * h)
        beemanX.append(bemX)
        bemY = beemanY[i - 1] + beemanVY[i - 1] * h + (1/6) * (4 * beemanAY[i - 1] - beemanAY[i - 2]) * (h * h)
        beemanY.append(bemY)
        bemVX = beemanVX[i - 1] + beemanAX[i - 1] * h
        beemanVX.append(bemVX)
        bemVY = beemanVY[i - 1] + beemanAY[i - 1] * h
        beemanVY.append(bemVY)
        bemR = math.sqrt((beemanX[i] * beemanX[i]) + (beemanY[i] * beemanY[i]))
        beemanR.append(bemR)
        bemAX = -(G*M*beemanX[i])/(beemanR[i]*beemanR[i]*beemanR[i])
        beemanAX.append(bemAX)
        bemAY = -(G*M*beemanY[i])/(beemanR[i]*beemanR[i]*beemanR[i])
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
plt.title("Grawitacja dla 1 obiektu", fontdict=font1)
plt.xlabel("X", fontdict = font2)
plt.ylabel("Y", fontdict = font2)

line, = ax.plot(0, 0, 'k.') #czarny
line2, = ax.plot(0, 0, 'r.') #czerwony
line3, = ax.plot(0, 0, 'b.') #niebieski

line.set_label('Planeta')
line2.set_label('metoda Eulera')
line3.set_label('metoda Beemana')
ax.legend()

def animation_frame(i):
    xdata.append(0)
    ydata.append(0)

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

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(0, iloscPunktow + 1, 1), interval = 1)
plt.show()