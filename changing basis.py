import numpy as np

decimal = 5

#  system 1
i = [1,0]
j = [0,1]
# second coordinate system
i2 = [2,1]
j2 = [-1,1]

# matrix A is composed of i2, j2 in columns
A = [[2,-1],[1,1]]
A_inv = [[1/3,1/3],[-1/3,2/3]]

#  matrix of rotation with coordinates in system 1
#  [1,0] is transformed to [0,1]
#  [0,1] is transformed to [-1,0]
rot90 = [[0,-1],[1,0]]
M = rot90

def det_2d(m):   # matrix 2x2
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    return a*d - b*c

def inverse(m):
    # 
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    det = det_2d(m)
    if det!= 0:
        return [[round(d/det,decimal),round(-b/det,decimal)],[round(-c/det,decimal),round(a/det,decimal)]]
    else:
        print('no inverse matrix')

def product1(m1,m2): # m2 is a column vector
    a1 = m1[0][0]
    b1 = m1[0][1]
    c1 = m1[1][0]
    d1 = m1[1][1]
    a2 = m2[0]
    b2 = m2[1]    
    return [round(a1*a2+b1*b2,decimal),round(c1*a2+d1*b2,decimal)]

def product(m1,m2): # m1,m2 are 2x2 matrices
    a1 = m1[0][0]
    b1 = m1[0][1]
    c1 = m1[1][0]
    d1 = m1[1][1]
    a2 = m2[0][0]
    b2 = m2[0][1]
    c2 = m2[1][0]
    d2 = m2[1][1]
    return [[round(a1*a2+b1*c2,decimal),round(a1*b2+b1*d2,decimal)],[round(c1*a2+d1*c2,decimal),round(c1*b2+d1*d2,decimal)]]


print(inverse(A))
print(A_inv)

v = [1,2]    # in system2 coordinates
#  where is v landing after rotation of 90 using the system2 coordinates ?
print(product(A_inv,A))


#  rotation of vectors i,j
print(product(M,[i,j]))
#  A.v
r1 = product1(A,v)
print('r1',r1)
#  M.A.v
r2 = product1(M,r1)
print('r2',r2)
#  A_inv.M.A.v
r3 = product1(A_inv,r2)
print('r3',r3)

#  A
r1 = A
print(r1)
#  M.A
r2 = product(M,r1)
print('M.A=',r2)
#  A_inv.M.A.v
r3 = product(A_inv,r2)
print('A_inv.M.A =',r3)

#  https://www.youtube.com/watch?v=P2LTAUO1TdA&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=13
print('A_inv.M.A.v =',product1(r3,v))