import numpy as np

m = 7
# rows
n = m   # columns

def create(m,n):
    h = np.ndarray((m,n),dtype='float64')
    h.fill(0)
    #print(h)

    for r in range(m):
        h[r,0]=round(1/(r+1),5)
        #print(r,h[r,0])
        if r != 0:
            for c in range(1,r+1):
                h[r,c]=round(h[r-1,c-1]-h[r,c-1],5)        
    #print(h)
    return h

h = create(m,n)
print(h)


print()
from scipy.special import binom, comb
m = 6
n = m
h = create(m, n)
print(h)

k = 5
l = k-4
print(h[k,l])
print(1/(l*binom(k,l)))


def val(n,k):
    return 1/(n*binom(n-1,k-1))

def val2(n,k):
    return 1/(k*binom(n,k))

from scipy import integrate
x2 = lambda x: x**2
X = integrate.quad(x2, 0, 4)[0]

print(X)

def sum_diag(h,d):
    r = len(h)
    s = sum(h[:,d-1])
    return s

m = 500
h = create(m, m)
# sum of columns h[:,c] = h[c-1,c-1]

for i in range(1,5):
    print('sum of c = 1/(c-1)',i,sum(h[:,i]))

# diagonal d > 2
d = 7
print('sum_diag:',d, '=', round(sum_diag(h,d),2), 1/(d-1))

def sum_denom(h,r):   # property 1
    # sum of denominators in row r
    denoms = [round(1/v,2) for v in h[r-1] if v!=0]
    return int(sum(denoms)), r*2**(r-1)

r = 5
print('sum of denominators of row',r, sum_denom(h,r))

def f_integ(r,c):     # property 2
    # value = integral
    f = lambda x: x**(c-1)*(1-x)**(r-c)
    return integrate.quad(f, 0, 1)[0]

m,n = 10,5

h_m_n = val2(m,n)
H_m_n = f_integ(m,n)

print(h_m_n, H_m_n)