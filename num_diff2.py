import numpy as np
import numdifftools as nd  # See https://pypi.python.org/pypi/Numdifftools

# https://pypi.org/project/numdifftools/
fd = nd.Derivative(np.exp)        # 1'st derivative
fdd = nd.Derivative(np.exp, n=2)  # 2'nd derivative
print(np.allclose(fd(1), 2.7182818284590424))
#True
print(np.allclose(fdd(1), 2.7182818284590424))
#True

xdata = np.reshape(np.arange(0,1,0.1),(-1,1))
ydata = 1+2*np.exp(0.75*xdata)
fun = lambda c: (c[0]+c[1]*np.exp(c[2]*xdata) - ydata)**2
Jfun = nd.Jacobian(fun)
print(np.allclose(np.abs(Jfun([1,2,0.75])), 0)) # should be numerically zero
#True

fun = lambda x: np.sum(x**2)
dfun = nd.Gradient(fun)
print(np.allclose(dfun([1,2,3]), [ 2.,  4.,  6.]))
#True

import numdifftools.nd_algopy as nda

fd = nda.Derivative(np.exp)        # 1'st derivative
fdd = nda.Derivative(np.exp, n=2)  # 2'nd derivative
print(np.allclose(fd(1), 2.7182818284590424))
#True
print(np.allclose(fdd(1), 2.7182818284590424))
#True
