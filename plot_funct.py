import numpy as np
import numdifftools as nd  # See https://pypi.python.org/pypi/Numdifftools

import matplotlib as mpl
import matplotlib.pyplot as plt

# Following is an Ipython magic command that puts figures in the  notebook.
# %matplotlib notebook

# plt.style.use('classic')
# M.L. modification of matplotlib defaults
# Changes can also be put in matplotlibrc file, 
# or effected using mpl.rcParams[]
plt.rc('figure', figsize = (6, 4.5))    # Reduces overall size of figures
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('figure', autolayout = True)  # Adjusts supblot parameters for new size

def plot_f(n=10,f=np.tanh):
    plt.figure(1)
    print(f)
    x = np.linspace(-2, 2, 100)
    for i in range(n):  # n derivatives of tanh
        df = nd.Derivative(f, n=i)
        y = df(x)
        h = plt.plot(x, y/np.absolute(y).max())
    plt.grid()
    plt.title('10 derivatives of tanh(x), -2=<x<2')
    plt.show()
    
plot_f()

plot_f(2,lambda x:x**5+3*x)