import numpy as np
import matplotlib.pyplot as plt
# https://www.youtube.com/watch?v=aVwxzDHniEw


dim = 10
t = np.linspace(0,1,dim)
t_powers = np.array([[t**3],[t**2],[t],[np.ones(dim)]]).reshape(4,dim)

# beziers matrices
# matrice somme puissance de t
M_P = np.matrix([[-1,3,-3,1],
                 [3,-6,3,0],
                 [-3,3,0,0],
                 [1,0,0,0]])

Mp = M_P.dot(t_powers)
print(Mp)
# Mp[0]=y1
# matrice somme de puissances de t identique à matrice somme points

# matrice vitesse
# matrice somme puissance de t
M_V = np.matrix([[0,-3,6,-3],
                 [0,9,-12,3],
                 [0,-9,6,0],
                 [0,3,0,0]])
Mv = M_V.dot(t_powers)
print(Mv)

# matrice accélération
# matrice somme puissance de t
M_A = np.matrix([[0,0,-6,6],
                 [0,0,18,-12],
                 [0,0,-18,6],
                 [0,0,6,0]])
Ma = M_A.dot(t_powers)
print(Ma)

#position
def position(t):
    return -t**3 + 3*t**2 - 3*t + 1, 3*t**3 - 6*t**2 + 3*t,-3*t**3 + 3*t**2, t**3

#velocity
def vitesse(t):
    return -3*t**2 + 6*t - 3, 9*t**2 - 12*t + 3, -9*t**2 + 6*t, 3*t**2

# acceleration
def acceleration(t):
    return -6*t + 6, 18*t - 12, -18*t + 6, 6*t

# jerk
def jerk(t):
    return -6, 18, -18, 6

y1, y2, y3, y4 = position(t)
#print(y1,'\n', M[0])
plt.plot(t,y1,label='yA')
plt.plot(t,y2,label='yB')
plt.plot(t,y3,label='yC')
plt.plot(t,y4,label='yD')
plt.title('Position(t)')
plt.legend()
plt.show()

# some points or vectors
A = (0.1,0)
xA, yA = A
B = (0.2,1)
xB, yB = B
C = (0.5,1.2)
xC, yC = C
D = (0.5,-.5)
xD, yD = D

def segment(P1, P2):
    #(P1_x + (P2_x - P1_x)*t, (P1_y + (P2_y - P1_y)*t
    return P1[0]*(1-t) + P2[0]*t,  P1[1]*(1-t) + P2[1]*t

coords = np.matrix([[x,y,z,w] for x,y,z,w in zip(A,B,C,D)]).T  # coordinates of A,B,C,D in columns

P_AB = segment(A,B)   
P_BC = segment(B,C)   
P_CD = segment(C,D)  
plt.plot(*P_AB)
plt.plot(*P_BC)
plt.plot(*P_CD)
#plt.show()

# P as sum of power of t
P = (xA*y1 + xB*y2 + xC*y3 + xD*y4, yA*y1 + yB*y2 + yC*y3 + yD*y4)
plt.plot(xA, yA,'x')
plt.plot(xB, yB,'x')
plt.plot(xC, yC,'x')
plt.plot(xD, yD,'x')
plt.plot(*P)
plt.grid()
plt.show()

# P with sum of vectors
# one by one
s3 = (-xA + 3*xB -3*xC + xD, -yA + 3*yB -3*yC + yD)
s2 = (3*xA -6*xB + 3*xC, 3*yA -6*yB + 3*yC)
s1 = (-3*xA + 3*xB, -3*yA + 3*yB)
s0 = (xA, yA)  # = A
print(s3,s2,s1,s0)

# or all together
s = M_P.dot(coords)  # [s3,s2,s1,s0]
print(s)
# calcul par matrice somme de puissances de t
Ps = np.array(s.T.dot(t_powers))

# Pv calcul par matrice de somme de vecteurs-points 
P2 = (t**3*s3[0] + t**2*s2[0] + t*s1[0] + s0[0], t**3*s3[1] + t**2*s2[1] + t*s1[1] + s0[1])
plt.plot(*A,'x')
plt.plot(*B,'x')
plt.plot(*C,'x')
plt.plot(*D,'x')
plt.plot(*P_AB)
plt.plot(*P_BC)
plt.plot(*P_CD)
plt.plot(*P2, label='P2')
plt.plot(*Ps,label='Ps')
plt.title('Béziers position')
plt.grid()
plt.legend()
plt.show()

y1, y2, y3, y4 = vitesse(t)
V2 = (xA*y1 + xB*y2 + xC*y3 + xD*y4, yA*y1 + yB*y2 + yC*y3 + yD*y4)

# matrice somme de vecteurs-points
M_V2 = np.matrix([[0,0,0,0],
                 [-3,9,-9,3],
                 [6,-12,6,0],
                 [-3,3,0,0]])

# on multiplie par le vecteur des points
v = M_V2.dot(coords)  # [s3,s2,s1,s0]
print(v)
# ensuite on multiplie par le vecteur des puissances de t
Vs = np.array(v.T.dot(t_powers))
plt.plot(xA, yA,'x')
plt.plot(xB, yB,'x')
plt.plot(xC, yC,'x')
plt.plot(xD, yD,'x')
plt.plot(*P_AB)
plt.plot(*P_BC)
plt.plot(*P_CD)
plt.plot(*V2, label='V2')
plt.plot(*Vs, label='Vs')
plt.title('Béziers vitesse')
plt.legend()
plt.grid()
plt.show()

# accélération
y1, y2, y3, y4 = acceleration(t)
A2 = (xA*y1 + xB*y2 + xC*y3 + xD*y4, yA*y1 + yB*y2 + yC*y3 + yD*y4)

# matrice somme de puissances de t
M_A2 = np.matrix([[0,0,0,0],
                 [0,0,0,0],
                 [-6,18,-18,6],
                 [6,-12,6,0]])

# on multiplie par le vecteur des points
a = M_A2.dot(coords)  
print(a)
# ensuite on multiplie par le vecteur des puissances de t
As = np.array(a.T.dot(t_powers))

plt.plot(xA, yA,'x')
plt.plot(xB, yB,'x')
plt.plot(xC, yC,'x')
plt.plot(xD, yD,'x')
plt.plot(*P_AB)
plt.plot(*P_BC)
plt.plot(*P_CD)
plt.plot(*A2, label='A2')
plt.plot(*As, label='As')
plt.grid()
plt.legend()
plt.title('Béziers accélération')
plt.show()


y1, y2, y3, y4 = jerk(t)

P4 = (xA*y1 + xB*y2 + xC*y3 + xD*y4, yA*y1 + yB*y2 + yC*y3 + yD*y4)
plt.plot(xA, yA,'x')
plt.plot(xB, yB,'x')
plt.plot(xC, yC,'x')
plt.plot(xD, yD,'x')
plt.plot(*P4,'ro')
plt.grid()
plt.title('Béziers jerk')
plt.show()
