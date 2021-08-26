import numpy as np
import random
import matplotlib.pyplot as plt

# benford's law
# value
l1 = 10000
# size
l2 = 100
freq=[0]*10
x = np.arange(1,10)

'''
a = np.random.randint(1,l1,(1,l2))
print(a)

for i in np.array(*a):
    n = int(str(i)[0])
    #print(n)
    freq[n] = freq[n]+1
print(freq)
plt.bar(x,freq[1:])
#plt.show()


for i in range(100):
    n = int(str(a[0][np.random.randint(0,l2)])[0])
    #print(n)
    freq[n] = freq[n]+1
print(freq)
plt.bar(x,freq[1:])
#plt.show()

'''
# loi benford
log_array=[]
for k in x:
    print((1+1/k, np.log10(1+1/k)))
    log_array.append(np.log10(1+1/k))

#print('sum',sum(log_array))  # sum=1
#plt.bar(x, np.log10(1+1/x)*100)
#plt.title('Loi Benford')
#plt.show()

# https://fr.wikipedia.org/wiki/Loi_de_Benford
# Par contre, dans une liste de 100 nombres obtenus comme produits de deux nombres
# ou plus tirés au hasard entre 1 et 10 000, les fréquences des chiffres 1 à 9 en
# première position suivent peu ou prou les valeurs de la loi de Benford.

val = 10000
numbers=[]
m = 5
kmin = 2 
kmax = 5
klist = []
benford=[np.log10(1+1/x) for x in range(1,10)]
print(benford)
benford_cumsum = np.cumsum(benford)
print(benford_cumsum)
# get 100 numbers as a product of k random numbers between 1 and val=10000
for i in range(m*100):
    p = 1
    k = random.randint(kmin,kmax)
    if k not in klist:
        klist.append(k)
    for i in range(k):
        p *= np.random.randint(1,val)    
    p0 = int(str(p)[0])
    numbers.append((k,p0,p))
    freq[p0] = freq[p0]+1
freq=[f/m for f in freq]
freq_cumul = np.cumsum(freq)
print(freq[1:])
print(klist)
print(numbers)
plt.bar(x-0.2,np.log10(1+1/x)*100,0.4, label='Benford\'s law')
plt.bar(x+0.2,freq[1:],0.4, label='Product of k random numbers')
plt.title(', '.join([str(round(s,1)) for s in freq[1:]]))
plt.legend()
plt.show()

plt.bar(x-0.2, benford_cumsum*100,0.4, label='Benford\'s cumul sum')
plt.bar(x+0.2,freq_cumul[1:],0.4, label='Product of k random numbers frequence cumul sum')
#plt.bar(x,freq_cumul[1:])
plt.title('Fréquences cumulées')
plt.legend()
plt.show()