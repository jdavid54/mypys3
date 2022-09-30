#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://apmonitor.com/che263/index.php/Main/PythonSolveEquations

import numpy as np
from scipy.optimize import fsolve

def myFunction(z):
   x = z[0]
   y = z[1]
   w = z[2]

   F = np.empty((3))
   F[0] = x**2+y**2-20
   F[1] = y - x**2
   F[2] = w + 5 - x*y
   return F

print('Scipy.optimize')
print('fsolve')
zGuess = np.array([1,1,1])
z = fsolve(myFunction,zGuess)
print(z)


print('Gekko')
from gekko import GEKKO
m = GEKKO()
x,y,w = [m.Var(1) for i in range(3)]
m.Equations([x**2+y**2==20,\
             y-x**2==0,\
             w+5-x*y==0])
m.solve(disp=False)
print(x.value,y.value,w.value)
zGuess = np.array([1,1,1])
z = fsolve(myFunction,zGuess)
print(z)

print('Sympy')
import sympy as sym
sym.init_printing()
x,y,z = sym.symbols('x,y,z')
c1 = sym.Symbol('c1')
f = sym.Eq(2*x**2+y+z,1)
g = sym.Eq(x+2*y+z,c1)
h = sym.Eq(-2*x+y,-z)

sym.solve([f,g,h],(x,y,z))