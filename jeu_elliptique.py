# https://www.youtube.com/watch?v=Et_qi3MuuuI

import matplotlib.pyplot as plt
import numpy as np

def m_a(a,b):
    return (a+b)/2

def m_g(a,b):
    return (a*b)**.5

def elliptik():
    pass

lemniscate = 2.6220575542921198104648395 # perimetre
a = np.sqrt(2)
b = 1

# print(m_a(a,b))
# print(m_g(a,b))
an = [a]
bn = [b]
p = 10

for k in range(p):
    ma = m_a(a,b)
    mg = m_g(a,b)
#     print(ma, mg)
    an.append(ma)
    bn.append(mg)
    a = ma
    b = mg
    
print('Calcul de la suite:\n',a,a*lemniscate,np.pi,1/a) # constante de Gauss : G
n = np.arange(p+1)
plt.plot(n,an)
plt.plot(n,bn)
plt.show()

print(an[-1],bn[-1])

# functions
def f(x):
    try:
        return 1/np.sqrt((1 - x**2)*(1 - k**2 * x**2))
    except:
        return x

def K(k):
        return integrate.quad(lambda x: f(x), 0, 1)[0]

# import warnings
# warnings.filterwarnings("error")

y = []
print('Plot fonction f')
k = 0.5
X = np.linspace(-(1+1/k),(1+1/k),100)
for x in X:
        y.append(f(x))
        if np.isnan(f(x)) or np.isinf(f(x)):
            pass
            #print(x)
#print(y)           
plt.plot(X,y)
plt.show()

import scipy.integrate as integrate
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html
import scipy.special as special

print('calcul du perimetre du lemniscate')
lem = integrate.quad(lambda x: 1/(np.sqrt(1-x**4)), -1, 1)[0]
print('Perimetre lemniscate',lem)

# integration K(k)
Kk = integrate.quad(lambda x: f(x), 0, 1)[0]
#print(k,Kk)

a = np.sqrt(2)
b = 1

# fonction video 1:35:15
k2 = 1 - b**2/a**2
k = np.sqrt(k2)

Kk = K(k)
print('result with my functions:',Kk,np.pi*a/(2*Kk))  # pas bonne valeur ???

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ellipk.html
print('result by special.ellipk:',special.ellipk(k2),np.pi * a/(2*special.ellipk(k2)))

# plot courbe multivaleur
L = np.linspace(0,5,100)
r = []
for l in L:
    r.append(integrate.quad(lambda x: f(x), 0, l)[0])
    
print(r[-1],np.pi * a/(2*r[-1]))
plt.plot(L,r)
plt.plot(r,L)
plt.show()

# quad_vec()
def f_l(x,l):
    return (x<=l)*f(x)

x = np.linspace(0,1,100)
plt.plot(x,f_l(x,1))
plt.show()

y = integrate.quad_vec(f_l, -np.inf, np.inf, args=(L,),points=[0])[0]
print('y',y)


plt.plot(x,y)
plt.show()