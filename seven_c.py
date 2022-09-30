import numpy as np

# functions
def b2u(name,l):
    print(name,'=',[(b1[n],i,u[n]) for n,i in enumerate(list(l.flat)) if i!= 0])
    
def b2v(name,l):
    print(name,'=',[(b2[n],i,v[n]) for n,i in enumerate(list(l.flat)) if i!= 0])
    
def b2w(name,l):
    print(name,'=',[(b3[n],i,w[n]) for n,i in enumerate(list(l.flat)) if i!= 0])
    
def flat(l):
    return list(l.flat)

b1 = ['T','L','M','I','θ','J','N']
u = ['s','m','kg','A','K','cd','mol']
b2 = ['f','v','E','Q','θ','J','N']
v = ['1/s','m/s','kg.m^2/s','C','K','cd','mol']

#Planck basis
b3 = ['c','G','hbar','e0','kB']
w = ['m/s','m^3/(kg.s^2)','J.s','F/m','J/K']

# matrix of conversion from b2 to b1 basis
M2_1 = np.array([[-1,-1,-2,1,0,0,0],
      [0,1,2,0,0,0,0],
      [0,0,1,0,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,0,1,0,0],
      [0,0,0,0,0,1,0],
      [0,0,0,0,0,0,1]])

#length
L = np.array([0,1,0,0,0,0,0]).reshape(7,1)
# area = LxL = L^2
A = np.array([0,2,0,0,0,0,0]).reshape(7,1)

# volume L*A
V = L + A    # multiplication = addition of exponants
b2u('volume=area*length',V)

# mass
M = np.array([0,0,1,0,0,0,0]).reshape(7,1)
b2u('Mass',M)

# other definitions in b1 basis
capacitance = np.array([4,-2,-1,2,0,0,0]).reshape(7,1)
thermal_conductivity = np.array([-3,1,1,0,-1,0,0]).reshape(7,1)
position_derivative99th = np.array([-99,1,0,0,0,0,0]).reshape(7,1)

# show power and unit in b1 basis
b2u('Length',L)
b2u('Area',A)
b2u('Volume',V)

# v^-2*E in b2 basis
vm2E = np.array([0,-2,1,0,0,0,0]).reshape(7,1)
# show
b2v('v^2*E',vm2E)
M = M2_1.dot(vm2E)
#print(list(M.flat))
# show result in b1 basis after matrix multiplication
b2u('Mass',M)

# show in b1 basis
b2u('Capacitance',capacitance)
b2u('Thermal comductivity',thermal_conductivity)
b2u('99th derivative of position',position_derivative99th)

# inverse matrix of CB
# matrix of conversion from b1 to b2 basis
M1_2 = np.mat(M2_1).I

C1 = np.array([4,-2,-1,2,0,0,0]).reshape(7,1)
C2 = np.array([0,0,-1,2,0,0,0]).reshape(7,1)

#C = T^4*L^-2*M^-1*I^2 = E^-1*Q^2
C = M1_2.dot(C1)
print(flat(C)==flat(C2))

# capacitance in b3 basis
cap = np.array([-2,1,1,1,0]).reshape(5,1)
b2w('cap',cap)

# matrix of conversion from b2 to b1 basis
M_planck = np.array([[-2.5,-1.5,0.5,3,2.5],
                     [0.5,0.5,-0.5,-0.5,-0.5],
                     [0.5,0.5,-0.5,0,0.5],
                     [0,0,0,0.5,0],
                     [0,0,0,0,-1]])

tP = np.array([-2.5,0.5,0.5,0,0]).reshape(5,1)
#v_tP = M_planck.dot(tP)
b2w('tP',tP)

lP = np.array([-1.5,0.5,0.5,0,0]).reshape(5,1)
#v_lP = M_planck.dot(lP)
b2w('lP',lP)


# matrix to go from planck to b1 basis ??????

# u=['s','m','kg','A','K','cd','mol']
p2u = np.array([[-2.5,-1.5,0.5,3,2.5],
                [0.5,0.5,-0.5,-0.5,-0.5],
                [0.5,0.5,0.5,0,0.5],
                [0,0,0,0.5,0],
                [0,0,0,0,-1]])

v_lP = M_planck.dot(lP)
b2u('v_lP',v_lP)