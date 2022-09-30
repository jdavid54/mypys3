import numpy as np
import matplotlib.pyplot as plt

# average of factors of interger n


def average(n):
    # counting all the points with integer coordinates under the curve n/x for x=1 to n
    s = 0
    for k in range(1,n+1):
        s += n//k
        #print(n//k,s)
    return s/n

def plot_points(n):
    p = 0
    for i in range(1,n+1):
        for j in range(1,n//i+1):
            if j == n/i: # point on the curve
                plt.plot(i,j,'ro')
            else:
                plt.plot(i,j,'bo')
            p += 1
    return p

n = 100

fig,ax = plt.subplots()
x = np.linspace(1,n,100)
y = n/x
plt.plot(x,y)
p = plot_points(n)
plt.title(f'number of points under f(x): {n}/x = {p}')
#plt.legend()
plt.show()

l = np.log(n)
a = average(n)
e = round((a-l)/l*100,1)
print(a, l, e,'%')

fig,ax = plt.subplots()
x = np.arange(1,n)
y = [average(i) for i in x]
plt.plot(x,y)
plt.plot(x,np.log(x))
plt.title(f'error for {n}={e}%')
plt.show()