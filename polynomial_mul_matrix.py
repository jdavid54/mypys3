import numpy as np

def rotate(l, n):
    return l[n:] + l[:n]

def polymul_bymatrix(P1, P2):
    # get rid of zero end trail
    P1 =  np.trim_zeros(P1, trim='b')
    P2 =  np.trim_zeros(P2, trim='b')
    m = len(P1)
    n = len(P2)    
    # P1 must have bigger degree than P2
    if m < n:
        P1,P2 = P2,P1 # swap
        m=len(P1)
        n=len(P2)
    deg1 = m-1
    deg2 = n-1
    deg_max = deg1 + deg2
    P1.extend([0]*(deg2))
    print('\nP1\n',P1)
    # create the matrix M with the rotating coefficients of P1
    M = []
    for k in range(n): 
        M.append(rotate(P1,-k))
    M = np.array(M).T

    print('Matrix\n', M)
    B = np.array(P2).reshape(n,1)
    print('P2 in column',B)
    result = list(np.dot(M, B).T.flatten())
    return M, B, result

A = [1,5,3,4,5,1,5,6,7]
B = [1,1,2]
matrix, b, c = polymul_bymatrix(A, B)
print('Result',c)

C = [0,0,0,0,0,0,1]

matrix, b, c = polymul_bymatrix(A, C)
print('Result',c)

A = [1,-5,3]
B = [0,-1,1]
matrix, b, c = polymul_bymatrix(A, B)
print('Result',c)

A = [1, 1]  # y = x+1
matrix, b, c = polymul_bymatrix(A, A)
print('Squared',c)

matrix, b, c = polymul_bymatrix(A, c)
print('Cube',c)