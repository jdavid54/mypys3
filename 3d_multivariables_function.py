import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_nu():
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.plot_surface(B, D, nu)
    plt.xlabel('b')
    plt.ylabel('d')
    plt.show()

    plt.contourf(B, D, nu)
    plt.colorbar()
    plt.xlabel('b')
    plt.ylabel('d')
    plt.show()
    
#     plt.contour(B,D,nu,[0.5])
#     plt.axis('equal')
#     plt.show()
    fig, ax = plt.subplots()
    ax.imshow(nu, origin='lower', interpolation='none')
    plt.show()


b = np.arange(0.2, 3.2, 0.2)
d = np.arange(0.1, 1.0, 0.1)

B, D = np.meshgrid(b, d)
# sqrt(1+(2*y*x)**2) / sqrt ((1-x**2)**2 + (2*y*x)**2)
nu = np.sqrt( 1 + (2*D*B)**2 ) / np.sqrt( (1-B**2)**2 + (2*D*B)**2)
plot_nu()

nu = D**2 + B**2
plot_nu()