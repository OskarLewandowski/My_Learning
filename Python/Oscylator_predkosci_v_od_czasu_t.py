import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Dane poczatkowe
k = 1
m = 1
h = 0.05
x0 = 10
v0 = 0
w = round(math.sqrt(k/m), 2)
A = round(math.sqrt(math.pow(v0, 2)/math.pow(w, 2) + math.pow(x0, 2)), 2)
ile = 1000  #Ilosc iteracji
tolX = 65 #oś X na wykresie
tolY = 35 #oś Y na wykresie

if(v0 < 0):
   fi = round((math.acos(x0/A) * 180/math.pi), 2)
else:
   fi = round((-math.acos(x0/A) * 180/math.pi), 2)

time = []
for i in range(0, ile+1):
    time.append(i*h)


# Sprawdzenie
print("k = {0}\nm = {1}\nh = {2}\nx0 = {3}\nv0 = {4}\nw = {5}\nA = {6}\nfi = {7}  ".format(k, m, h, x0, v0, w, A, fi))
print("Ilośc iteracji = ", ile)


#Dokladna
dokladneX = []
dokladneX.append(x0)
dokladneV = []
dokladneV.append(v0)
#Euler
eulerX = []
eulerX.append(x0)
eulerV = []
eulerV.append(v0)
#posrednia
posredniaX = []
posredniaX.append(x0)
posredniaV = []
posredniaV.append(v0)
#verlet
verletX = []
verletX.append(x0)
verletV = []
verletV.append(v0)
#beeman
beemanX = []
beemanX.append(x0)
beemanV = []
beemanV.append(v0)


for i in range(1, ile+1):
    #dokladna
    dokX = round(A * math.cos(w * time[i] + fi * math.pi/180), 2)
    dokladneX.append(dokX)
    dokV = round(-A * w * math.sin(w * time[i] + fi * math.pi/180), 2)
    dokladneV.append(dokV)
    #euler
    eulX = round((eulerX[i-1]+eulerV[i-1]*h), 2)
    eulerX.append(eulX)
    eulV = round((eulerV[i-1]-math.pow(w, 2)*eulerX[i-1]*h), 2)
    eulerV.append(eulV)
    #posrednia
    posX = round((posredniaX[i-1] + posredniaV[i-1] * h - 0.5 * math.pow(w, 2) * posredniaX[i-1] * math.pow(h, 2)), 2)
    posredniaX.append(posX)
    posV = round((posredniaV[i-1] - math.pow(w, 2) * posredniaX[i-1] * h), 2)
    posredniaV.append(posV)
    #verlet
    verX = round((verletX[i-1] + verletV[i-1] * h - 0.5 * math.pow(w, 2) * verletX[i-1] * math.pow(h, 2)), 2)
    verletX.append(verX)
    verV = round((verletV[i-1] - 0.5 * math.pow(w, 2) * (verletX[i-1] + verletX[i]) * h), 2)
    verletV.append(verV)
    #bemman
    bemX = round((beemanX[i-1] + beemanV[i-1] * h - 0.5 * math.pow(w, 2) * beemanX[i-1]*math.pow(h, 2)), 2)
    beemanX.append(bemX)
    bemV = round((beemanV[i-1] - 0.5 * math.pow(w, 2) * (beemanX[i-1] + beemanX[i]) * h), 2)
    beemanV.append(bemV)

print(beemanX)
print(beemanV)


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
ax.set_xlim(0, tolX)
ax.set_ylim(-tolY, tolY)
plt.title("Zależność prędkości v od czasu t\n- oscylator harmoniczny, porónanie rozwiązań numerycznych", fontdict=font1)
plt.xlabel("t", fontdict = font2)
plt.ylabel("v(t)", fontdict = font2)
line, = ax.plot(0, 0, '.')
line2, = ax.plot(0, 0, 'r.')
line3, = ax.plot(0, 0, 'g.')
line4, = ax.plot(0, 0, 'k.')
line5, = ax.plot(0, 0, 'm.')

line.set_label('v(t) - rozwiązanie dokładne')
line2.set_label('v(t) - metoda Eulera')
line3.set_label('v(t) - metoda Pośrednia')
line4.set_label('v(t) - metoda Verleta')
line5.set_label('v(t) - metoda Beemana')
ax.legend()

def animation_frame(i):
    xdata.append(time[i])
    ydata.append(dokladneV[i])

    xdata2.append(time[i])
    ydata2.append(eulerV[i])

    xdata3.append(time[i])
    ydata3.append(posredniaV[i])

    xdata4.append(time[i])
    ydata4.append(verletV[i])

    xdata5.append(time[i])
    ydata5.append(beemanV[i])

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

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(0, ile + 1, 1), interval = 5)
plt.show()

