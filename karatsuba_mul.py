import numpy as np
debug=False

def kolmogorov(a,b):
    N = len(str(a))
    result= np.zeros(2*N)
    num1 = list(str(a))
    num1.reverse()
    num2 = list(str(b))
    num2.reverse()
    print(num1, num2)
    for i in range(3):        
        for j in range(N):
            sum = 0
            print(i,j,num1[j],num2[i])
            sum += int(num1[j]) * int(num2[i])
            print('sum',sum)
            sum = result[-j-1-i] + sum
            result[-j-1-i] = sum%10 #units
            result[-j-2-i] += (sum - (sum%10))/10 #tens       
            print(result)
    return result   

def karatsuba(a,b):
    global k
    k+=1
    na = len(str(a))//2
    nb = len(str(b))//2
    n = min(na,nb)
    da = a//10
    ua = a%10
    db = b//10
    ub = b%10
    if debug:print(k,':',a,b,da,ua,db,ub,na,nb)
    if a<10 or b<10:
        return a*b
    p = karatsuba((da+ua),(db+ub))
    ac = karatsuba(da,db)
    bd = karatsuba(ua,ub)
    bcad = p-ac-bd
    if debug:print('p:',p,ac,bcad,bd)
    return ac*100+bcad*10+bd


def karatsuba2(a,b):
    global k
    k+=1
    na = len(str(a))//2
    nb = len(str(b))//2
    n = min(na,nb)
    da = a//10**n
    ua = a%10**n
    db = b//10**n
    ub = b%10**n
    if debug:print(k,':',a,b,da,ua,db,ub,na,nb)
    if a<10 or b<10:
        return a*b
    p = karatsuba((da+ua),(db+ub))
    ac = karatsuba(da,db)
    bd = karatsuba(ua,ub)
    bcad = p-ac-bd
    if debug:print('p:',p,ac,bcad,bd)
    return ac*10**(2*n) + bcad*10**n + bd


a = 56
b = 1234123456

def test(a,b):
    global k
    print('k1')
    k = 0
    k1 = (karatsuba(a,b),k)
    print(k1)
    print('\nk2')
    k = 0
    k2 = (karatsuba2(a,b),k)
    
    print(k2)
