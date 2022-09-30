import numpy as np
pi = np.pi
sqrt = np.sqrt
exp = np.exp
inf = np.inf


def bell_curve(x,m,s):
    return 1/(s*sqrt(2*pi))*exp(-1/2*((x-m)/s)**2)


import matplotlib.pyplot as plt
from scipy import integrate

fig,ax = plt.subplots()
x = np.linspace(-5,5,100)


mu = 0
sigma = 1.5
Y = lambda x : 1/(sigma*sqrt(2*pi))*exp(-1/2*((x-mu)/sigma)**2)
y = bell_curve(x,mu,sigma)
plt.plot(x,y,label=f'mu={mu},sigma={sigma}')
print(bell_curve(0,mu,sigma))
i1 = integrate.quad(Y, -inf, inf)[0]

mu = 0
sigma = 1
Y = lambda x : 1/(sigma*sqrt(2*pi))*exp(-1/2*((x-mu)/sigma)**2)
y = bell_curve(x,mu,sigma)
plt.plot(x,y,label=f'mu={mu},sigma={sigma}')
print(bell_curve(0,mu,sigma))
i2 = integrate.quad(Y, -inf, inf)[0]

mu = 0
sigma = 0.5
Y = lambda x : 1/(sigma*sqrt(2*pi))*exp(-1/2*((x-mu)/sigma)**2)
y = bell_curve(x,mu,sigma)
plt.plot(x,y,label=f'mu={mu},sigma={sigma}')
print(bell_curve(0,mu,sigma))
i3 = integrate.quad(Y, -inf, inf)[0]

print(i1, i2,i3)
plt.legend()
plt.show()