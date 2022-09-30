from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# plot 1
fig = plt.figure()
ax = plt.axes(projection='3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.3, label='Three planes')
ax.legend()
plt.title('Plot 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


# plot 2
limit = 1.2
delta = 0.1
fig = plt.figure()
ax = plt.axes(projection='3d')
x, y = np.meshgrid(np.arange(-limit, limit, delta),
                      np.arange(-limit, limit, delta))
# vector field
F = (x*y+x, x+y)

ax.quiver(x,y,F[0], x,y,F[1], length=0.1,label='Vector field')

def f(x, y):
    return x*y+x

z = f(x, y)
# ax.contour3D(x, y, z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

theta = np.linspace(-2 * pi, 2 * pi, 100)
# circle
r = 1
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.plot(x, y, label='parametric curve C',color='red')
ax.legend()
plt.title('Plot 2')
plt.show()


# Plot 3
# Data for a three-dimensional line
fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')
plt.title('Plot 3')
# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()