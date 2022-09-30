import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, quad_vec
import time

# https://www.youtube.com/watch?v=9wXBaqQwr8g

def f(x,a):
    return np.exp(-a*x**2)

a = np.linspace(1,2,10000)
result = quad_vec(f,-1,3,args=(a,))
print(result)

# timing with quad_vec
t1 = time.perf_counter()
l = quad_vec(f,-1,3,args=(a,))
t2 = time.perf_counter()
print(t2-t1) #0.024946799998360802

# looping over quad
t1 = time.perf_counter()
l = [quad(f,-1,3,args=(ai,)) for ai in a]
t2 = time.perf_counter()
print(t2-t1) #3.5244456000000355

# 4:44
def f(x,a,b):
    return np.exp(-a*(x-b)**2)

a = np.arange(1,20,1)  #20 values
b = np.linspace(0,5,100)  # 100 values

av, bv = np.meshgrid(a,b) 

integral = quad_vec(f,-1,3,args=(av,bv))[0]
#print(integral)

plt.figure(figsize=(6,3))
plt.pcolormesh(av,bv,integral)
plt.xlabel('$a$')
plt.ylabel('$b$')
plt.colorbar(label='$f(x;a,b)$')
#plt.plot(x,y)
plt.show()

# 7:01

a = 1
# integrate with bounds [-a, a]
# => put bounds in function definition as a boolean statement
# integrate from -inf to inf
def f(x,a):
    return (x>=-a)*(x<=a)*np.exp(-a*x**2)

x = np.linspace(-5,5,1000)
y = f(x,1);y2 = f(x,20)
plt.figure(figsize=(6,3))
plt.plot(x,y);plt.plot(x,y2)
plt.show()

a = np.arange(1,20,1)
integral = quad_vec(f,-1,3,args=(a,))
print(integral[0])

# break points
integral = quad_vec(f,-np.inf,np.inf,args=(a,))
print(integral[0])