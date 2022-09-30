import numpy as np


x = np.full((5,5),0)
y = np.full((5,5),0)

x[0][0] = 0;    y[0][0] = 0
x[0][1] = 1 ;   y[0][1] = 0
x[0][2] = 2;    y[0][2] = 0
x[0][3] = 3;    y[0][3] = 0
x[0][4] = 4 ;   y[0][4] = 0

x[1][0] = 0 ;   y[1][0] = 1
x[1][1] = 1 ;   y[1][1] = 1
x[1][2] = 2;    y[1][2] = 1
x[1][3] = 3 ;   y[1][3] = 1
x[1][4] = 4;    y[1][4] = 1

x[2][0] = 0;    y[2][0] = 2
x[2][1] = 1 ;   y[2][1] = 2
x[2][2] = 2 ;   y[2][2] = 2
x[2][3] = 3 ;   y[2][3] = 2
x[2][4] = 4;    y[2][4] = 2

x[3][0] = 0 ;   y[3][0] = 3
x[3][1] = 1 ;   y[3][1] = 3
x[3][2] = 2;    y[3][2] = 3
x[3][3] = 3;    y[3][3] = 3
x[3][4] = 4 ;   y[3][4] = 3

x[4][0] = 0 ;   y[4][0] = 4
x[4][1] = 1 ;   y[4][1] = 4
x[4][2] = 2;    y[4][2] = 4
x[4][3] = 3;    y[4][3] = 4
x[4][4] = 4 ;   y[4][4] = 4

import matplotlib.pyplot as plt
plt.plot(x,y, marker='.', color='k', linestyle='none')
plt.show()

# meshgrid
xvalues = np.array([0, 1, 2, 3, 4]);
yvalues = np.array([0, 1, 2, 3, 4]);
xx, yy = np.meshgrid(xvalues, yvalues)

plt.plot(xx, yy, marker='.', color='k', linestyle='none')
plt.show()

x = np.arange(-5,5,.1)
y = np.arange(-5,5,.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)
plt.show()

def sinus2d(x, y):
    return np.sin(x) + np.sin(y)

#et vous voulez, par exemple, voir à quoi il ressemble dans la gamme de 0 à 2*pi.
#Comment le feriez-vous? Il y a np.meshgrid entre:

xx, yy = np.meshgrid(np.linspace(0,2*np.pi,100), np.linspace(0,2*np.pi,100))
z = sinus2d(xx, yy) # Create the image on this grid
#et un tel complot ressemblerait à:

plt.imshow(z, origin='lower', interpolation='none')
plt.show()
