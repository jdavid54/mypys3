import numpy as np
import matplotlib.pyplot as plt

sqrt = np.sqrt

c = 1
# 0 <= v <= 1

def gamma(v,c=1):
    return 1/sqrt(1-v**2/c**2)

max_v = 0.999

def plot_gamma():
    v = np.linspace(0,max_v,100)
    fig, ax = plt.subplots()
    plt.plot(v,gamma(v), label='gamma')
    for vi in (0.5,0.6,0.7,.8,0.9,.99,.999): 
        plt.plot(vi,gamma(vi),'.')
    ax.set_xlabel("speed v")
    ax.set_ylabel("gamma")
    plt.legend()
    plt.show()

def trans_lorentz(x,y,z,t,v,c=1):
    x2 = gamma(v)*(x-v*t)
    y2 = y
    z2 = z
    t2 = gamma(v)*(t-v*x/c**2)
    return x2, y2, z2, t2

def lorentz_inverse(x,y,z,t,v):
    return trans_lorentz(x,y,z,t,-v)

'''
x, y, z, t, v = 10,0,0,0,0.1
print(v,trans_lorentz(x,y,z,t,v))

fixe = 5
# x variable, t fixe
x = np.linspace(0,10,10)
t =  np.linspace(fixe, fixe,10)
x2, y2, z2, t2 = trans_lorentz(x,y,z,t,v)
print(v,x2, t2)
plt.plot(x, label='x')
plt.plot(t, label='t')
plt.plot(x2, label='x2')
plt.plot(t2, label='t2')
plt.legend()
plt.show()

# t variable, x fixe
x =  np.linspace(fixe, fixe,10)
t = np.linspace(0,10,10)
x2, y2, z2, t2 = trans_lorentz(x,y,z,t,v)
print(v,x2, t2)
plt.plot(x, label='x')
plt.plot(t, label='t')
plt.plot(x2, label='x2')
plt.plot(t2, label='t2')
plt.legend()
plt.show()

# v 
v = 0.9
x = np.linspace(0,10,10)
t = np.linspace(fixe, fixe,10)
x2, y2, z2, t2 = trans_lorentz(x,y,z,t,v)
print(v,x2, t2)
plt.plot(x, label='x')
plt.plot(t, label='t')
plt.plot(x2, label='x2')
plt.plot(t2, label='t2')
plt.legend()
plt.show()
'''
#beta = v/c = v
#gamma = 1/sqrt(1-beta**2)
v = .5
beta = v/c
g = gamma(v)

# transform matrix
# x2 =         g*x - beta*g*c*t
# c*t2 = -beta*g*x + g*c*t
M = np.matrix([[g,0,0,-beta*g],
     [0,1,0,0],
     [0,0,1,0],
     [-beta*g,0,0,g]])

x, y, z, t = 0,0,0,5
coors = [x,y,z,t]

coors2 = M.dot(coors)
print('coors2', coors2)

M_inverse = np.matrix([[g,0,0,beta*g],
     [0,1,0,0],
     [0,0,1,0],
     [beta*g,0,0,g]])

print('coors', M_inverse.dot(coors2.A1))

def pseudonorme(x,y,z,t):
    return x**2+y**2+z**2-c**2*t**2

x, y, z, t = 10,0,0,0
print(v,trans_lorentz(x,y,z,t,v))
print(pseudonorme(x,y,z,t))

x, y, z, t = trans_lorentz(x,y,z,t,v)
print(lorentz_inverse(x, y, z, t, v))
print(pseudonorme(x,y,z,t))

# fonction hyperbolique
#beta = th(phi) = v/c
# ch(phi) = 1/sqrt(1-th(phi)**2) = gamma
# sh(phi) = th(phi)*ch(phi)
def get_angle(v,c=1):
    return np.arctanh(v/c)

phi = get_angle(v)
print(v, phi)

print(gamma(v), np.cosh(phi))

th = np.tanh(phi)
ch = np.cosh(phi)
sh = np.sinh(phi)

# matrix rotation by phi
M_phi = np.matrix([[ch,0,0,-th*ch],
     [0,1,0,0],
     [0,0,1,0],
     [-th*ch,0,0,ch]])

print(M, '\n',M_phi)

def compo_vitesse(v,u,c=1):
    return (u+v)/(1+u*v/c**2)

v, u = 0.5, 0.8
w = compo_vitesse(v,u)
print(v,u,w)

# th(psi+phi) = th(psi)+th(phi)/(1+th(psi)*th(phi)) = w/c
psi = get_angle(v)
phi = get_angle(u)
#psi = np.arctanh(v)
#phi = np.arctanh(u)
print(np.tanh(psi+phi),w)

print((np.tanh(psi)+np.tanh(phi))/(1+np.tanh(psi)*np.tanh(phi)))

def time_dilation(t1,t2,v,c=1):
    #proper_time to
    to = t2 - t1
    g = gamma(v)
    t = to * g
    return to,t

to, t = time_dilation(0, 5, 0.5)
print('référentiel mobile:',to, '- référentiel immobile:', t)

# gamma(v) est pair, on aussi dilatation vu de l'autre référentiel
# v négatif
to, t = time_dilation(0, 5, -0.5)
print('référentiel immobile:',to, '- référentiel mobile:', t)

def length_contraction(x1, x2,v):
    lo = x2 - x1
    g = gamma(v)
    l = lo / g
    return lo, l

lo, l = length_contraction(0, 5,0.5)
print('référentiel mobile:',lo, '- référentiel immobile:', l)

# gamma(v) est pair, on aussi contraction vu de l'autre référentiel
lo, l = length_contraction(0, 5, -0.5)
print('référentiel immobile:',lo, '- référentiel mobile:', l)

# https://fr.wikipedia.org/wiki/Calculs_relativistes
def trans_vitesse(vx,vy,vz,v,c=1):
    # v vitesse du référentiel mobile
    # vx, vy, vz = composants de vitesse d'un objet dans le référentiel mobile
    # vx, vy, vz < 1
    # Vx, Vy, Vz = composants de vitesse d'un objet vu du référentiel immobile
    beta = v/c
    g = gamma(v)
    ct = g * (1+beta*vx/c)
    Vx = c*(vx/c + beta)/(1+beta*vx/c)
    Vy = c*(vy/c)/ct
    Vz = c*(vz/c)/ct
    print(Vx,Vy,Vz)
    gV = 1 - ((Vx**2 + Vy**2 + Vz**2)/c**2)
    print(gV)
    gV2 = 1 - ((vx**2 + vy**2 + vz**2)/c**2)
    GV = 1/sqrt(gV)    # Lambda(V)
    GV2 =  1/sqrt(gV2) # Lambda(V')
    return beta,g,Vx,Vy,Vz,gV, GV, GV2    

vx, vy,vz = 0.5,0.5,.5
beta,g,Vx,Vy,Vz,gV, GV, GV2 = trans_vitesse(vx,vy,vz,0.8)
print(Vx,Vy,Vz,gV, GV, GV2)

# Lambd(V)*c = gamma*(Lambda(V')*c+beta*(Lambda(V')*vx
print(GV)
print(g*(GV2*c+beta*(GV2*vx)))