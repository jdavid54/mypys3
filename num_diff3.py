import numpy as np
import numdifftools as nd  # See https://pypi.python.org/pypi/Numdifftools

# https://numdifftools.readthedocs.io/en/latest/tutorials/getting_started.html#the-derivative
def rosen(x):
    return (1-x[0])**2 + 105.*(x[1]-x[0]**2)**2

grad = nd.Gradient(rosen)([1, 1])
print(grad)

H = nd.Hessian(rosen)([1, 1])
li, U = np.linalg.eig(H)

f = lambda x: np.sum(x**2)
grad = nd.Gradient(f)(np.r_[1, 2, 3, 4, 5])
evl = np.allclose(grad, [  2.,   4.,   6.,   8.,  10.])
print(evl)
#True

H = nd.Hessian(lambda xy: np.cos(xy[0] - xy[1]))([0, 0])
print(np.abs(np.linalg.eig(H)[0]) < 1e-12)

# Jacobian matrix of a scalar function is just the gradient
jac = nd.Jacobian(rosen)([2, 3])
grad = nd.Gradient(rosen)([2, 3])
print(np.allclose(jac, grad))
#True