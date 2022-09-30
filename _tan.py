import numpy as np
pi = np.pi


def recur(m,n):
	if n==1:
		m=x/(n-m)
		return m
	else:
		m=recur(m,n-2)
		return x2/(n-m)

def _tan(x, n=21):
	k=int((n-1)/2)
	x2=x*x
	m=x2/n
	print(n,m)
	'''
	for i in range(k-1):
		n-=2
		m=x2/(n-m)
		print(n,m)
	'''
	m=recur(m,n)
	return x/(1-m)

x=pi/7	
print(_tan(x))
print(np.tan(x))