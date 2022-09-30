import numpy as np


moessner2 = [i for n,i in enumerate(range(1,50)) if (n+1)%2!=0]
print(moessner2)
print(np.cumsum(moessner2))

moessner3 = [i for n,i in enumerate(range(1,50)) if (n+1)%3!=0]
print(moessner3)
print(np.cumsum(moessner3))
moessner3 = [i for n,i in enumerate(np.cumsum(moessner3)) if (n+1)%2!=0]
print(moessner3)
print(np.cumsum(moessner3))

print()
k=5
moessner5 = [i for n,i in enumerate(range(1,50)) if (n+1)%k!=0]
print(moessner5)
print(k,np.cumsum(moessner5))
k-=1
moessner5 = [i for n,i in enumerate(np.cumsum(moessner5)) if (n+1)%k!=0]
print(k,np.cumsum(moessner5))
k-=1
moessner5 = [i for n,i in enumerate(np.cumsum(moessner5)) if (n+1)%k!=0]
print(k,np.cumsum(moessner5))
k-=1
moessner5 = [i for n,i in enumerate(np.cumsum(moessner5)) if (n+1)%k!=0]
print(k,np.cumsum(moessner5))

def moessner_list(k):
    #k = 3
    moessner = [i for n,i in enumerate(range(1,50)) if (n+1)%k!=0]
    print('moessner :',moessner)
    print(k,np.cumsum(moessner))
    k-=1
    while k>=2:    
        moessner = [i for n,i in enumerate(np.cumsum(moessner)) if (n+1)%k!=0]
        print(k,np.cumsum(moessner))
        k-=1
    return np.cumsum(moessner)

k = 5    
m = moessner_list(k)
print([i**k for i in range(1,len(m)+1)])