import sympy as sp
from math import *

display=print

x=sp.symbols('x')
ysymbolique=sp.sin(x)
x = 45
ynumerique=sin(x)
print(ysymbolique, ynumerique)

# active le module de calcul symbolique, et la ligne suivante:
x,y=sp.symbols('x,y')
# définit x et y comme variables algébriques symboliques.
# on définit ensuite les deux équations à résoudre
eq1= 2*x+  y+1
eq2=-4*x-5*y+4
# et on solutionne
solution=sp.solve((eq1,eq2),x,y)
# comme dans la fenetre de commande de matlab, on peut faire écho de la solution:
print(solution)

[z1,z2]=sp.solve(x**2-3*x+4)
display(z1)
solution=sp.solve(x**2-3*x+4)
display(solution)
display(type(solution))


sp.init_printing(use_latex=True)
racines=sp.solve(x**3+x**2-x+10)
#
# ici j'utilise la fonction display qui affichera en LaTeX
# J'ai fait la commande
#   from IPython.display import * 
# et sp.init_printing(use_latex=True)
# plus haut, j'ai donc accès à cet outil de formattage supérieur. Comparez avec la cellule 
# plus bas
#
display(racines)
display(racines[0])

display(racines[0].evalf())


# plot
from sympy import plot,tan
x=sp.symbols('x')
plot(tan(x),(x,-1.4,1.4))

eq=x**3+x**2-x+10
racines=sp.solve(eq)
sp.plot(eq,(x,-2,2))
for i in range(len(racines)):
    display(racines[i].evalf())
    
    
def planck(T,lam):
    h=6.62608e-34
    k=1.38066e-23
    c=2.99792e8
    P1=2*sp.pi*c**2*h
    P2=lam**5
    P3=sp.exp(c*h/lam/k/T)-1
    return P1/P2/P3
lam=sp.symbols('lam')
sp.plot(planck(5800,lam),(lam,100e-9,1000e-9),ylabel='q corps noir (W/m3)',
        xlabel=' lambda (m)',xscale='log')


x = sp.symbols('x')
 
# Range non fixé dans la direction y. options par default
sp.plot(1/(x - 2), (x, 0, 4))

# Range non fixé dans la direction y, mais l'algorithme de calcul
# n'adapte pas les intervalles pour mieux couvrir la fonction. 
# adaptive = False donne des intervalles fixes.

sp.plot(1/(x - 2), (x, 0, 4),adaptive=False)
 
# On peut améliorer en changeant les limites de l'affichage en y.
sp.plot(1/(x - 2), (x, 0, 4), ylim=(-10, 10), adaptive=False)


from sympy.plotting import plot3d
x,y=sp.symbols('x y')
plot3d((sp.exp(-(x**1.5+y**2))),(x,-2,2),(y,-2,2))


# source:
# http://matplotlib.org/1.3.1/examples/mplot3d/contourf3d_demo2.html

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(figsize=(14,12))
#ax = fig.gca(projection='3d')
ax = plt.axes(projection='3d')
X, Y, Z = axes3d.get_test_data(0.04)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.show()

# https://pierreproulx.espaceweb.usherbrooke.ca/notebooks/python_2.html