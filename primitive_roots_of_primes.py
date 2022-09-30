# Primitive root of primes

# https://www.youtube.com/watch?v=DKy98FWHwdg
import numpy as np
import math
# import totient() method from sympy
from sympy.ntheory.factor_ import totient

from shanksbot import shanks

# import totient() method from sympy
from sympy.ntheory.factor_ import totient

mod = np.mod
debug = False

alpha = np.arange(2,20)

def isPrime(n):
    if n==1: return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def isPrime3(n):
    if totient(n) == n-1:
        return True
    return False

def euler_phi(n):    #totient
    m = 0
    l = []
    if n==1:
        return 1,[1]
    # number of coprimes of n from 1 to n
    for k in range(1,n):
        if math.gcd(n,k)==1:
            l.append(k)
            m += 1
    return m,l

# if len(l) = n-1 then n is prime
for n in range(1,20):        
    m,l = euler_phi(n)
    print(n,m,l,end='')
    if m == n-1:
        print('=>',n,'is prime',end='')
    print()


def ord_n(n,a):
    # the k smallest that m = a^k(mod n) = 1 
    for k in range(1,n):
        m = np.mod(np.power(a,k,dtype=np.int64),n)
        if m == 1:  # the first k is the smallest
            break
        #print(k,np.power(a,k,dtype=np.int64),m)
    #print(k,np.power(a,k,dtype=np.int64),m)
    return k

def primitive_root(p):
    # a is said to be a primitive root of prime number p, if a(mod p), a^2(mod(p),... ,a^(p-1) are distinct.
    # a is a primitive root of p if for 1<k<p, a^k(mod p) are distinct.
    pr = []
    for a in alpha:
        r = []
        ok = True
        #print(a)
        for k in range(1,p):            
            #m = np.mod(a**k,p)                           # problem with a=45,68 cause by default type = int32
            m = np.mod(np.power(a,k,dtype=np.int64),p)    # must force to int64
            if m in r:                                    # not distinct congruences         
                ok = False
                r.append(m)
                print(a,r,'repetition of',m)
                break
            r.append(m)
            
        if ok:
            pr.append(a)
            print(a,'is OK',pr,r)
            if debug:
                print(a,pr,r)
    return pr
'''
p = 7
print(f'shanks({p})',shanks(p))
print(primitive_root(p))

p = 17
print(f'\nshanks({p})',shanks(p))
print(primitive_root(p))
'''

# if ord_n(a) = phi(n) then a is a primitive root of n
print(ord_n(10,3)==euler_phi(10)[0])

n = 10
phi = euler_phi(n)[0]
print(n,phi)

pr = []
for a in range(2,15):
    p = ord_n(n,a)
    m = np.mod(np.power(a,p,dtype=np.int64),n)
    print(a,p==phi,end=' + ')
    if m != 1:
        print(' no good')
    elif p!=phi:
        print('not primitive root')
    else:
        print(a,'is primitive root of',n)
        pr.append(a)
print(pr)


def divisors(n):
    f =[]
    for k in range(1,int(n/2)+1):
        if n%k == 0:
            f.append(k)
    f.append(n)
    return f

def sum_of(n):
    # https://www.youtube.com/watch?v=zP09Dw5D8nY&t=908s
    # sum of phi(divisors) = n
    f = divisors(n)
    l = [euler_phi(i)[0] for i in f]
    print(f,l,sum(l))
    
sum_of(10)
sum_of(100)


#https://www.youtube.com/watch?v=zP09Dw5D8nY&t=908s

# if ord_n(a) = m then (a^k)%n = 1 <=> m|k
n = 12
p = euler_phi(10)[0]
a = 5
m = ord_n(n,a)

# find all k<n
for k in range(1,30):
    if (a**k)%n==1:  # a^k(mod n) = 1
        print(k,a**k,k%m==0)  # m divides k
        
# thus ord_n(a)|phi(n)
print('ord_n(a) divide Phi(n)',p,m,p%m==0)
