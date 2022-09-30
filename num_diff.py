# http://www.eg.bucknell.edu/~phys310/jupyter/numdiff.html
# https://numdifftools.readthedocs.io/en/latest/

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

def plot_f():
    plt.figure(1)
    x = np.linspace(-2, 2, 100)
    for i in range(10):  # n derivatives of tanh
        df = nd.Derivative(np.tanh, n=i)
        y = df(x)
        h = plt.plot(x, y/np.absolute(y).max())
    plt.grid()
    plt.title('10 derivatives of tanh(x), -2=<x<2')
    plt.show()
    
plot_f()


# jacobian matrix
def jacobian(f,x):
    #       | df1/dx  df2/dx  df3/dx |
    #  J =  | df1/dy  df2/dy  df3/dy |
    #       | df1/dz  df2/dz  df3/dz |
    return nd.Jacobian(f)(x)

# Divergence of vector-valued function f evaluated at x
def div(f,x):
    #jac = nd.Jacobian(f)(x)
    jac = jacobian(f,x)
    # return sum of diagonal (trace of matrix)
    return jac[0,0] + jac[1,1] + jac[2,2]
# Gradient of scalar-valued function f evaluated at x
def grad(f,x): 
    return nd.Gradient(f)(x)
# Curl of vector field f evaluated at x
def curl(f,x):    # rot(f,x)
    #jac = nd.Jacobian(f)(x)
    jac = jacobian(f,x)
    # curl = [df2/dz-df3/dy, df3/dx-df1/dz, df1/dy-df2/dx]
    return np.array([jac[2,1]-jac[1,2],jac[0,2]-jac[2,0],jac[1,0]-jac[0,1]])

def hessdiag(f,x):
    return nd.Hessdiag(f)(x)

# Laplacian of scalar field f evaluated at x
def laplacian(f,x):
    #hes = nd.Hessdiag(f)(x)
    hes = hessdiag(f,x)
    print(hes)
    return sum(hes)

def laplacian2(f,x):
    grd = grad(f,x)
    print(x, grd)
    return sum(grd)


# Scalar function single variable
def f(x):
    return 4*x**3

x0 = 3
d1 = nd.Derivative(f,n=1)  # OR nd.Derivative(f)
# d1 = 12*x**2
d2 = nd.Derivative(f,n=2)
# d2 = 24*x
print(d1(x0),d2(x0))

# scalar field (3D)
def g(x_):
    x, y, z = x_
    return x**2 + y**3 + 1

r0 = np.array([1,2,3])
gr = grad(g,r0)
print(gr)


# Vector field (3D)
def v1(x_):
    # v1(x,y,z) = [f1(x,y,z), f2(x,y,z), f3(x,y,z)] = [y**3, x**2, x]
    x, y, z = x_
    return np.array([y**3, x**2, x])

def v2(x_):
    # v2(x,y,z) = [x**3 * z, y, z*x]
    x, y, z = x_
    return np.array([x**3*z, y, z*y])

r0 = np.array([1,2,3])
print('ro = ',r0)

# v1(r0) = [y**3, x**52, x]
print('v1(ro)=',v1(r0))

# v1 = [y**3, x**2, x]
# jac1 col0 = [d(y**3)/dx, d(x**2)/dx, d(x)/dx]
#           = [0, 2*x, 1] = [0,2,1]

# jac1 col1 = [d(y**3)/dy, d(x**2)/dy, d(x)/dy]
#           = [3*y**2, 0, 0] = [12,0,0]

# jac1 col3 = [d(y**3)/dz, d(x**2)/dz, d(x)/dz]
#           = [0, 0, 0]
jac1 = nd.Jacobian(v1)(r0)
print('jacobian v1 =',jac1)


# v2 = [x**3*z, y, z*y]
# jac2 col0 = [d(x**3*z)/dx, d(y)/dx, d(z*y)/dx]
#           = [z*3*x**2, 0, 0] = [9,0,0]

# jac2 col1 = [d(x**3*z)/dy, d(y)/dy, d(z*y)/dy]
#           = [0, 1, z] = [0,1,3]

# jac2 col3 = [d(x**3*z)/dz, d(y)/dz, d(z*y)/dz]
#           = [x**3, 0, y] = [1,0,2]

# jac2 =[[9., 0., 1.],
#        [0., 1., 0.],
#        [0., 3., 2.]]

jac2 = nd.Jacobian(v2)(r0)
print('jacobian v2 =',jac2)

crl = curl(v1,r0)
print(crl)
# array([  0.,  -1., -10.])
div1, div2 = div(v1,r0), div(v2,r0)
print(div1, div2)


lapl = laplacian(g,r0)
print(lapl)

# https://numdifftools.readthedocs.io/en/latest/tutorials/getting_started.html#the-derivative
def rosen(x):
    return (1-x[0])**2 + 105.*(x[1]-x[0]**2)**2

grd = nd.Gradient(rosen)([1, 1])
print(grd)
# see num_diff3.py for nd.Hessian()


f = lambda x: np.sum(x**2)
grd = nd.Gradient(f)(np.r_[1, 2, 3, 4, 5])
evl = np.allclose(grd, [  2.,   4.,   6.,   8.,  10.])
print(evl)
#True


jac = nd.Jacobian(rosen)([2, 3])
grd = nd.Gradient(rosen)([2, 3])
print(np.allclose(jac, grd))
#True

