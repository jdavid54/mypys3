# https://www.youtube.com/watch?v=iVOsU4tnouk

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**5 -5*x + 3

def df(x):
    return 5*x**4 - 5

def xn(x):
    return x - f(x)/df(x)

# f(guess) number must not be a maximal or minimal ie df(guess) must be different to zero
guess_list = (-1.5,0.8,2)
sol = []

for k in range(3):
    guess = guess_list[k]
    for n in range(10):
        #print(guess)
        guess = xn(guess)
    sol.append(guess)    
    print(f(guess))

x = np.linspace(-2,2,100)
y = f(x)
plt.plot(x,y)
for g in sol:
    plt.plot(g,f(g),'ro')
plt.grid()
plt.show()