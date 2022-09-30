import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, quad_vec
import time


# https://www.youtube.com/watch?v=VlIgQzV28nw

def f(x):
    return np.exp(-x**2) * np.sin(x)**2

x = np.linspace(-3,3,10000)
y= f(x)

plt.figure(figsize=(4,3))
plt.plot(x,y)
plt.show()

#  bounds
result = quad(f,-2,2)
print(result)

result = quad(f,-np.inf,np.inf)
print(result)

# function with arguments
def f(x,a,b):
    return np.exp(-a*x**2) * np.sin(b*x)**2

result = quad(f,-np.inf,np.inf,args=(2,3))   # a=2, b=3
print('with arguments a,b:',result)

test = False
if test:
    # default error tolerance
    t1 = time.perf_counter()
    l=[quad(f,-np.inf,np.inf,args=(2,3)) for i in range(10000)]
    t2 = time.perf_counter()
    print(t2-t1)  #23.945620799999233


    # fix error tolerance to speed computing time
    t1 = time.perf_counter()
    l=[quad(f,-np.inf,np.inf,args=(2,3), epsabs=1e-4) for i in range(10000)]
    t2 = time.perf_counter()
    print(t2-t1)  #15.375547200001165

# 7:28
# quad break points
def f(x):
     return np.exp(-(x-700)**2) + np.exp(-(x+700)**2)
    
x = np.linspace(-750,750,1000)
y = f(x)

plt.figure(figsize=(4,3))
plt.plot(x,y)
# plt.xlim(-720,-680)
# plt.xlim(680,720)
plt.show()

print(quad(f,-np.inf,np.inf))
# with points
#raise ValueError("Infinity inputs cannot be used with break points.")

print(quad(f,-800,800,points=[-700,700]))
# (3.544907701811011, 1.9972548851034084e-10)
print(2*np.sqrt(np.pi))


# more
# help(quad)

