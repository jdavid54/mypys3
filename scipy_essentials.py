import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.optimize import minimize

# x is a vector
f = lambda x:(x[0]-1)**2 + (x[1]-2.5)**2
cons = ({'type':'ineq', 'fun': lambda x: x[0]-2*x[1]+2},
        {'type':'ineq', 'fun': lambda x: -x[0]-2*x[1]+6},
        {'type':'ineq', 'fun': lambda x: -x[0]+2*x[1]+2})
bnds = ((0, None), (0, None))

res = minimize(f, (2,0), bounds=bnds, constraints=cons)
print(res)



# Interpolation
x = np.linspace(0, 10, 10)
y = x**2 * np.sin(x)
plt.scatter(x,y)
plt.show()



#Curve Fitting
x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2
plt.scatter(x_data, y_data)
plt.show()

from scipy.interpolate import interp1d
f = interp1d(x, y, kind='cubic')
x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)
plt.plot(x_dense, y_dense)
plt.scatter(x, y)
plt.show()


from scipy.optimize import curve_fit

def func(x, a, b):
    return a*x**2 + b
popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1))
print(popt)


t_data = np.array([ 0.   ,  0.34482759,  0.68965517,  1.03448276,  1.37931034,
        1.72413793,  2.06896552,  2.4137931 ,  2.75862069,  3.10344828,
        3.44827586,  3.79310345,  4.13793103,  4.48275862,  4.82758621,
        5.17241379,  5.51724138,  5.86206897,  6.20689655,  6.55172414,
        6.89655172,  7.24137931,  7.5862069 ,  7.93103448,  8.27586207,
        8.62068966,  8.96551724,  9.31034483,  9.65517241, 10.        ])
y_data = np.array([ 4.3303953 ,  1.61137995, -2.15418696, -3.90137249, -1.67259042,
        2.16884383,  3.86635998,  1.85194506, -1.8489224 , -3.96560495,
       -2.13385255,  1.59425817,  4.06145238,  1.89300594, -1.76870297,
       -4.26791226, -2.46874133,  1.37019912,  4.24945607,  2.27038039,
       -1.50299303, -3.46774049, -2.50845488,  1.20022052,  3.81633703,
        2.91511556, -1.24569189, -3.72716214, -2.54549857,  0.87262548])

plt.plot(t_data,y_data,'o--')
plt.show()


def func(x, A, w, phi):
    return A*np.cos(w*x+phi)

popt, pcov = curve_fit(func, t_data, y_data, p0=(4, np.pi, 0))
print(popt)

A, w, phi = popt
t = np.linspace(0, 10, 100)
y = func(t, A, w, phi)
plt.scatter(t_data,y_data)
plt.plot(t,y)
plt.show()

error = np.sqrt(np.diag(pcov))
print(error)


#Special Functions
from scipy.special import legendre
x = np.linspace(0, 1, 100)
plt.plot(x, legendre(6)(x))
plt.show()

from scipy.special import jv
x = np.linspace(0, 10, 100)
plt.plot(x, jv(3,x))
plt.show()


# Calculus
# Differentiation
from scipy.misc import derivative
def f(x):
    return x**2 * np.sin(2*x) *np.exp(-x)
x = np.linspace(0, 1, 100)
plt.plot(x, f(x))
plt.plot(x, derivative(f, x, dx=1e-6))
plt.plot(x, derivative(f, x, dx=1e-6, n=2))
plt.grid()
plt.show()

# Integration
from scipy.integrate import quad
integrand = lambda x: x**2 * np.sin(2*x) * np.exp(-x)
integral, integral_error = quad(integrand, 0, 1)
print(integral)

# Differetial Equations
# First Order ODEs
# 
# Air friction while falling   v'-av**2 +b =0;  v(0) = 0
from scipy.integrate import odeint
def dvdt(v, t):
    return 3*v**2 - 5
v0 = 0

#Solve differential equation
t = np.linspace(0, 1, 100)
sol = odeint(dvdt, v0, t)
v_sol = sol.T[0]
#Plot
plt.plot(t, v_sol)
plt.show()

# Coupled first order ODEs
def dSdx(S, x):
    y1, y2 = S
    return [y1 + y2**2  + 3*x,
           3*y1 + y2**3 - np.cos(x)]
y1_0 = 0
y2_0 = 0
S_0 = (y1_0, y2_0)
x = np.linspace(0, 1, 100)
sol = odeint(dSdx, S_0, x)
y1_sol = sol.T[0]
y2_sol = sol.T[1]
plt.plot(x, y1_sol)
plt.plot(x, y2_sol)
plt.show()


# Second Order ODEs
# 
# Equation for a pendulum
def dSdt(S, t):
    theta, omega = S
    return [omega,
           np.sin(theta)]
theta0 = np.pi/4
omega0 = 0
S0 = (theta0, omega0)
t = np.linspace(0, 20, 100)
sol = odeint(dSdt, S0, t)
theta, omega = sol.T
plt.plot(t, theta)
plt.show()


# Fourier Transforms

# show the signal
x = np.linspace(0, 10*np.pi, 100)
y = np.sin(2*np.pi*x) + np.sin(4*np.pi*x) + 0.1*np.random.randn(len(x))
plt.plot(x, y)
plt.show()

# show the harmonics
from scipy.fft import fft, fftfreq
N = len(y)
yf = fft(y)[:N//2]
xf = fftfreq(N, np.diff(x)[0])[:N//2]
plt.plot(xf, np.abs(yf))
plt.show()

# Examples
# Example 1. The energy required to get from point r1
#  to point r2
#  for a plane is given by :   E = a integral_curve(dr/dt)*dt - integral_curve(F*dr/dt)*dt
def f(A): 
    integrand = lambda t: 2 / (1 + np.abs(A*np.sin(np.pi*t/10)))**2 + 5*np.sqrt(1+(np.pi*A/10)**2 * np.cos(np.pi * t / 10)**2)
    return quad(integrand, 0, 10)[0]

res = minimize(f, 0.001, method="CG").x
print(res)

# Example 2: Newton's law of cooling is : dT/dt = -k(T-T_B(t))

t_m = np.array([ 0.,  1.04347826,  2.08695652,  3.13043478,  4.17391304,
        5.2173913 ,  6.26086957,  7.30434783,  8.34782609,  9.39130435,
       10.43478261, 11.47826087, 12.52173913, 13.56521739, 14.60869565,
       15.65217391, 16.69565217, 17.73913043, 18.7826087 , 19.82608696,
       20.86956522, 21.91304348, 22.95652174, 24.        ])

temp_m = np.array([283.2322975, 284.6945461, 286.2259041, 287.8603625, 289.6440635,
       291.6187583, 293.7939994, 296.1148895, 298.4395788, 300.5430675,
       302.1566609, 303.0363609, 303.0363609, 302.1566609, 300.5430675,
       298.4395788, 296.1148895, 293.7939994, 291.6187583, 289.6440635,
       287.8603625, 286.2259041, 284.6945461, 283.2322975])

plt.scatter(t_m, temp_m)
plt.xlabel('Time [hour]')
plt.ylabel('Temperature [K]')

# interpolation temperature of air in 24 hours
Ts = interp1d(t_m, temp_m, kind='cubic')


def dTdt(T, t):
    return -0.5*(T-Ts(t))

times = np.linspace(1, 23, 1000)
T0 = 284.6945461
sol = odeint(dTdt, T0, times).T[0]
plt.plot(times, sol, label='Shallow Water temp')
plt.scatter(t_m, temp_m, color='r', label='Outside Temp')
plt.legend()
plt.show()





# Linear Algebra
from scipy.linalg import solve_triangular
a = np.array([[3, 0, 0, 0],
              [2, 1, 0, 0],
              [1, 0, 1, 0],
              [1, 1, 1, 1]])
b = np.array([4, 2, 4, 2])
x = solve_triangular(a, b, lower=True)
print(x)

# Toeplitz Matrices (matrices with constant diagonals)
from scipy.linalg import solve_toeplitz, toeplitz

c = np.array([1, 3, 6, 10])    # First column of T
r = np.array([1, -1, -2, -3])  # First row of T
b = np.array([1, 2, 2, 5])

x = solve_toeplitz((c, r), b)
print(x)

# Eigenvalue Problems
# Eigenvalue problems can be solved using numpy, so here we focus on particular cases for optimization

from scipy.linalg import eigh_tridiagonal
d = 3*np.ones(4)
e = -1*np.ones(3)

w, v = eigh_tridiagonal(d, e)
A = np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)
print(A)
print(A@v.T[0])
print(w[0] * v.T[0])


# Special Matrices
# Fiedler matrix A_ij = |a_i - a_j|
#  where 
#  is some sequence of numbers
from scipy.linalg import fiedler
f = fiedler([1, 4, 12, 45])
print(f)

from scipy.linalg import toeplitz
f = toeplitz([1,2,3,6,0,0], [1,4,5,6,0,0])
print(f)

# Decompositions
# LU decomposition A = PLU
# where P is a permutation matrix, L is a lower triangular matrix and U is an upper triangular matrix.
from scipy.linalg import lu
A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
p, l, u = lu(A)
print(p)
print(l)
print(u)


from scipy.linalg import cholesky
A = np.array([[1,0.2],[0.2,1]])
C = cholesky(A, lower=True)
print(C)
print(C@C.T)
print(A)


# Sparse Matrices
# Matrices that contain lots of zeros (so lots of space can be reduced)
from scipy.linalg import kron # kronecker product, NOT sum
N= 5
d = -2*np.ones(N)
e = np.ones(N-1)
D = np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)
# convert to kronsum
D_kronsum = kron(D, np.identity(N)) + kron(np.identity(N),D)
print(D_kronsum)

# sparse matrix : lots of zeroes and a small number of data is sparsed inside
from scipy import sparse
N=100
diag = np.ones([N])
diags = np.array([diag, -2*diag, diag])
D = sparse.spdiags(diags, np.array([-1,0,1]), N, N)
T = -1/2 * sparse.kronsum(D,D)
print(T)


# Statistics
# beta distribution
from scipy.stats import beta
a, b = 2.5, 3.1
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
x = np.linspace(beta.ppf(0, a, b), beta.ppf(1, a, b), 100)
plt.plot(x, beta.pdf(x, a, b))
plt.show()

r = beta.rvs(a, b, size=10)
print(r)

#  Gaussian Distribution
from scipy.stats import norm
mu = 1
sigma = 2
mean, var = norm.stats(loc=mu, scale=sigma, moments='mv')
x = np.linspace(norm.ppf(0.01, mu, sigma), norm.ppf(0.99, mu, sigma), 100)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.show()

# Multinomial Distribution
from scipy.stats import multinomial
# rolling dice 6 times at a row
p = np.ones(6)/6
res = multinomial.pmf([6,0,0,0,0,0], n=6, p=p)
print(res)
# a hundred trial
res = multinomial.rvs(n=100, p=p, size=5)
print(res)

# Generating Random Numbers from your own distribution
import scipy.stats as st

class mr_p_solver_dist(st.rv_continuous):
    def _pdf(self,x, a1, a2, b1, b2):
        return 1/(2*(a1*b1+a2*b2))*(b1*np.exp(-np.sqrt(x/a1)) + b2*np.exp(-np.sqrt(x/a2)))
my_rv = mr_p_solver_dist(a=0, b=np.inf)
a1, a2, b1, b2 = 2, 3, 1, 2
x = np.linspace(my_rv.ppf(0.01, a1, a2, b1, b2), my_rv.ppf(0.99, a1, a2, b1, b2), 100)
y = my_rv.pdf(x, a1, a2, b1, b2)
plt.plot(x, y)
plt.semilogy()
plt.show()

res = my_rv.rvs(a1, a2, b1, b2, size=10)
print(res)

class mr_p_solver_dist(st.rv_continuous):
    def _pdf(self,x, a1, a2, b1, b2):
        return 1/(2*(a1*b1+a2*b2))*(b1*np.exp(-np.sqrt(x/a1)) + b2*np.exp(-np.sqrt(x/a2)))
    def _cdf(self, x, a1, a2, b1, b2):
        return 1/(2*(a1*b1+a2*b2))* ( -2*a1*b1*(np.sqrt(x/a1)+1)*np.exp(-np.sqrt(x/a1)) \
           -2*a2*b2*(np.sqrt(x/b2)+1)*np.exp(-np.sqrt(x/b2)) \
           + 2*a1*b1 + 2*a2*b2 )
    def _rvs(self, a1, a2, b1, b2, delta=0.001, size=None, random_state=None):
        a_min = min([a1, a2])
        x = np.linspace(0, a_min*np.log(1/delta)**2, 10000)
        r = np.random.rand(size)
        return x[np.searchsorted(self._cdf(x[:-1], a1, a2, b1, b2), r)]

my_rv = mr_p_solver_dist(a=0, b=np.inf)
print(my_rv._rvs(a1, a2, b1, b2, size=10000))

# END