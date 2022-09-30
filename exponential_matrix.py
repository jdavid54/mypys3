import numpy as np
pi = np.pi
decimal = 5

def exp(x,n=150):
    v = 0
    for i in range(n):
        v += x**i/np.math.factorial(i)
#         print(v)
    return np.real(v),np.imag(v)

#  with real numbers
print(exp(2))
print(exp(3))

#  with complex numbers
print(exp(complex(0,pi)))

# with matrices
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

def add(m1,m2): # m1,m2 are 2x2 matrices
    a1 = m1[0][0]
    b1 = m1[0][1]
    c1 = m1[1][0]
    d1 = m1[1][1]
    a2 = m2[0][0]
    b2 = m2[0][1]
    c2 = m2[1][0]
    d2 = m2[1][1]
    return [[a1+a2,b1+b2],[c1+c2,d1+d2]]

def _pow(m,p):
    if p==0:
        return [[1,0],[0,1]]
    v = m
    for i in range(p-1):
        v = product(m,v)
    return v

def scale(s,m):
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    return [[s*a,s*b],[s*c,s*d]]

def exp_matrix(m, n=17):
    v = [[0,0],[0,0]]
    for i in range(n+1):
        f = np.math.factorial(i)
        s = 1/f
        p = _pow(m,i)
        w = scale(s,p)
        print(i,f,s)
        print(p)
        print('_v=',v)
        v = add(w,v)
        

pi= np.pi
M = [[np.cos(pi/2),-np.sin(pi/2)],[np.sin(pi/2),np.cos(pi/2)]]
N = [[0,-pi],[pi,0]]
print('M =',M)
print('M**2 =',product(M,M))

# print(exp_matrix(M,5))
# print(exp_matrix(N))

#  matrix 3x2
A=np.array([[1,2],[3,4],[5,6]])
#  matrix 2x3
B=np.array([[1,2,3],[3,4,5]])
#  matrix 3x3
print(np.dot(A,B))

C = np.array([[3,1,4],[1,5,9],[2,6,5]],dtype=np.longdouble)

from numpy.linalg import matrix_power
def exp_mat(m, n=17):
    v = np.zeros(m.shape,dtype=np.int64) # get dimension of m and create zero matrix = [[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(n+1):
        f = np.math.factorial(i)
        s = 1/f
#         if i==0:
#             p = np.eye(m.shape[0])
#         else:
#             p = np.dot(p,m)
        p = matrix_power(m,i)
        w = s*p
        print(i,f,s)
        print(p)
        print('_v=',v)
        v = w+v       
        print('w=',w,w.dtype)
        print('v=',v)
        print()
    return v.round(decimals=2)

print(exp_mat(C,46))