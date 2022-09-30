#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://apmonitor.com/pdc/index.php/Main/PythonDifferentialEquations


import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO()    # create GEKKO model
k = 0.3        # constant
y = m.Var(5.0) # create GEKKO variable
m.Equation(y.dt()==-k*y) # create GEKKO equation
m.time = np.linspace(0,20) # time points

# solve ODE
m.options.IMODE = 4
m.solve(disp=False)

# plot results
plt.plot(m.time,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()



m = GEKKO()    # create GEKKO model
k = m.Param()  # constant
y = m.Var(5.0) # create GEKKO variable
m.Equation(y.dt()==-k*y) # create GEKKO equation
m.time = np.linspace(0,20) # time points

# solve ODEs and plot
m.options.IMODE = 4
m.options.TIME_SHIFT=0

k.value = 0.1
m.solve(disp=False)
plt.plot(m.time,y,'r-',linewidth=2,label='k=0.1')

k.value = 0.2
m.solve(disp=False)
plt.plot(m.time,y,'b--',linewidth=2,label='k=0.2')

k.value = 0.5
m.solve(disp=False)
plt.plot(m.time,y,'g:',linewidth=2,label='k=0.3')

plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()