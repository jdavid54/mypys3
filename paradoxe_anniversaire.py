import numpy as np
import matplotlib.pyplot as plt

N = 365

p = []

for n in range(1,N+1):
    #print(n)
    p.append((N-n+1)/N)

p_cumprod = np.cumprod(p)   
p_nc =  [k*100 for k in p_cumprod]  
p_c = [(1-k)*100 for k in p_cumprod]

# plotting
fig, ax = plt.subplots()
plt.plot(p_nc[:100],label='Non coinc.')
plt.plot(p_c[:100], label='Coinc.')
plt.plot(22,p_c[22],'o',label='23p : '+str(round(p_c[22],2))+'%')
plt.plot(21,p_c[21],'o',label='22p : '+str(round(p_c[21],2))+'%')
plt.plot(59,p_c[59],'o',label='60p : '+str(round(p_c[59],2))+'%')
plt.plot((0,100),(50,50),'r-.')
plt.xticks(np.arange(0,101,step=10),np.arange(1,102,step=10))
ax.set_xlabel("Nombre de personnes réunies")
ax.set_ylabel("Probabilité en %")
plt.legend(loc='upper right',bbox_to_anchor=(.9, .9))
plt.grid()
plt.show()

n = 23
# p[a] = prob de a+1 personnes
print(p_c[n-3:n+3])

print(p_c[n-1])  # prob pour 23 personnes

def fact(n):
    if n == 0: return 1
    if n == 1: return 1
    return n*fact(n-1)

def prob_non_coincidence(N,n):
    return fact(N)//fact(N-n)*1/N**n  # division entière, float numbers don't handle big numbers

#for k in range(120):
#    print(k,prob(365,k))
max = 365
n = range(1,max)
p_nc = [prob_non_coincidence(365,k) for k in range(1,max)]
p_c = [1-k for k in p_nc]
fig, ax = plt.subplots()
plt.plot(n,p_nc)
#plt.plot(n,p_c)
ax.set_yscale('log')
plt.grid()
plt.title('Non coincidence')
ax.set_xlabel("Nombre de personnes réunies")
ax.set_ylabel("Probabilité (log)")
plt.show()

def approx_prob(N,n): # p(n)
    return  1 - np.exp(-n*(n-1)/(2*N))

def person(N,p): # inverse function pf p(n) : n(p)
    return np.sqrt(2*N*np.log(1/(1-p)))

for p in np.arange(0,1,0.05):
    print(p, person(365, p))

# equation n**2-s*n+prod
p = 0.5
s = 1
prod = -2*N*np.log(1/(1-p))
m = s/2
n1= m+np.sqrt(1/4-prod)
n2= m-np.sqrt(1/4-prod)
print(n1,n2,n1+n2,n1*n2)

def raleigh(x):
    return 1-np.exp(-x**2/2)

x = np.linspace(0,10,100)
y = raleigh(x)
plt.plot(x,y)
plt.title('Loi de Raleigh')
plt.show()

import random
def test_raleigh():
    boites = np.zeros(365)
    go = True
    n = 0
    while go:
        b =random.randint(1,365)        
        if boites[b-1] == 0:
            print(b,end=',')
            boites[b-1] += 1
            n += 1
        else:
            print('\nend',b, n)
            go = False

test_raleigh()