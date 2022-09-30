import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def recur(m, n):
    global s
    if n == 1:        
        s = 'x/(1-'+s+')'
        m = x/(n-m)
        if not isinstance(x, np.ndarray) and debug:
            print(n,s,m)
        return m
    else:
        s = 'x**2/('+str(n)+'-'+s+')'
        m = x2/(n-m)
        if not isinstance(x, np.ndarray) and debug:
            print(n,s,m)
        return recur(m,n-2)

def _tan(x, n=13, r=True):
    # y = x/(1-x**2/(3-x**2/(5-x**2/(7-x**2/9)))) for n=9
    global s, x2
    m = x2/n
    s = 'x**2/'+str(n)
    if not isinstance(x, np.ndarray) and debug:
        print(n,s,'=',m)
    k = int((n-1)/2)
    if not r:
        for i in range(k-1):
            n = n-2
            m = x2/(n-m)
            s = 'x**2/('+str(n)+'-'+s+')'
            if debug:
                print(n,s,'=',m)
        n = n-2
        s = 'x/(1-'+s+')'
        m = x/(1-m)
        if debug:
            print(n,s,'=',m)
    else:
        m = recur(m,n-2)     
    return m


def recur2(n):
    global s,m,x2

    if n == 1:        
        s = 'x/(1-'+s+')'
        m = x/(n-m)
        if not isinstance(x, np.ndarray) and debug:
            print(n,s,'=',m)
        return m
    else:
        if s=='':
            s = 'x**2/'+str(n)
        else:
            s = 'x**2/('+str(n)+'-'+s+')'
        m = x2/(n-m)
        if not isinstance(x, np.ndarray) and debug:
            print(n,s,'=',m)
        return recur2(n-2)


def _tan2(x, n=15):
    global m,s, x2
    x2 = x*x
    return recur2(n)

debug = True
s = ''
m = 0
x = pi/7


print(_tan2(x), np.tan(x))
'''
print(_tan(x, n=17, r=False), np.tan(x))
#print(_tan(x),np.tan(x),_tan(x,debug=True)-np.tan(x))
'''
#plt.figure(figsize=(8,8))
fig,ax = plt.subplots()
#gs = gridspec.GridSpec(2, 2)
ax.set_xlim((-2*pi, 2*pi))
ax.set_ylim((-5, 5))
#ax = fig.add_subplot(gs[0, :])
x = np.linspace(-2*pi,2*pi,100)
y = np.tan(x)
plt.plot(x,y,label='tan')
n = 17
y = _tan2(x,n)  
plt.plot(x,y,label='-tan')
plt.title('_tan2(x) with n='+str(n))
plt.grid()
plt.legend()
plt.show()
