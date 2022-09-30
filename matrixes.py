import numpy as np

def test():
    # matrixes
    n = 5
    M1 = np.round(np.random.rand(n,n),2)
    print(M1)

    M2= np.random.randint(0, 10, (n,n))
    print(M2)

    print()
    A = np.array([1,0,-3,-4,5])
    B = np.array([1,2,3,4,5])
    C = np.array([list(B)*5]).reshape(n,n)
    I = np.eye(n, k=0, dtype=int)  # k=0 by default
    all_one = np.ones((n,n))

    print('AI\n', A*I)
    print('AIB\n',A*I*B)
    print('CA\n',C*A)

def test2():    
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(a)

    #array([[1, 2, 3],
    #       [4, 5, 6],
    #       [7, 8, 9]])

    print(a[np.triu_indices(3)])
    #or
    LU = list(a[np.triu_indices(3)])

    # https://numpy.org/doc/stable/reference/generated/numpy.triu.html
    print(np.triu(a))
    print(np.tril(a))


    A2= rotate(A,-1)
    print(A2)

    a = np.array([A,rotate(A,-1)])
    print(a.T)
    print(np.tril(a.T))


def rotate(l, n):
    return l[n:] + l[:n]

def make_mat(P1,P2):
    # get rid of zero end trail
    #P1 =  np.trim_zeros(P1, trim='b')
    #P2 =  np.trim_zeros(P2, trim='b')
    m = len(P1)
    n = len(P2)
    deg1 = m-1
    deg2 = n-1
    deg_max = deg1 + deg2
    # P1 must have bigger degree than P2
    if m < n:
        P1,P2 = P2,P1
        m=len(P1)
        n=len(P2)
    if deg_max > m: # add zero only if final max degree is more than number of coefficients of P1
        P1.extend([0]*(n-1))
    print('P1\n',P1)
    a = []
    for k in range(n): 
        a.append(rotate(P1,-k))
    a = np.array(a).T
    print(deg_max,m)
    if deg_max <= m :
        a = np.tril(a)
    print('matrice a\n',a)
    print('P2\n',P2)
    b = np.array(P2).reshape(n,1)
    
    c = np.dot(a,b) 
    return a,b,c.T 

A = [1,5,3,4,5,1,5,6,7]
'''
B = [1,1]
a,b,c = make_mat(A,B)
print(c)
a,b,c = make_mat(B,A)
print(c)
a,b,c = make_mat(A,A)
print(c)
'''
C = [0,0,0,0,0,0,1]
a,b,c = make_mat(A, C)
print(c)

A = [1,5,3,4]
B = [1,3,3]
a,b,c = make_mat(A, B)
print(c)
