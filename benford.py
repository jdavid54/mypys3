import matplotlib.pyplot as plt
import numpy as np
log10=np.log10
import random

x=np.linspace(1,9,100)
plt.plot(x,log10(x), label='log10(x)')
plt.plot(x,log10(x+1), label='log10(x+1)')
plt.plot(x,log10(1+1/x), label='Benford curve')
plt.grid()
plt.legend()
plt.title('Loi de Benford')
plt.show()

max = 10000
freq=[0]*10
print(freq)
for k in range(100):
    p=1
    for m in range(np.random.randint(2,10)):
        p *= np.random.randint(1,max)
    f=int(str(p)[0])
    if k==50: print(m,p,f)
    freq[f]+=1
print(freq)
x=np.array([i for i in range(1,10)])
plt.bar(x-0.2,np.log10(1+1/x)*100,0.4, label='Benford\'s law')
plt.bar(x+0.2,freq[1:],0.4, label='My random')
plt.grid()
plt.legend()
plt.title('Loi de Benford '+str(max))
plt.show()