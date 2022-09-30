import numpy as np

import fast_fourier_transform as fft
# import all functions explicitly
#from fast_fourier_transform import *    

# activate debug in fast_fourier_transform
# debug = False
#fft.debug = True

P = [0, 0, 1, 0]
fft_P = fft.FFT(P)
print(fft_P)


# product of polynomials
def A(x):
    return x**2+2*x+1

def B(x):
    return x**2-2*x+1

def C(x):
    return x**4 -2*x**2 + 1

X = np.array([-2,-1,0,1,2])

Ax = list(map(A, X))
Bx = list(map(B, X))
print(Ax, Bx)
# product Ax, Bx
P = [a*b for a,b in zip(Ax,Bx)]
print(P)
set = [(a,b) for a,b in zip(X,P)]
print(set)

Cx = list(map(C, X))
print(Cx, Cx==P)

print()
# length must be power of 2 and length > degree of C which is 4 => l = 8
coeff_A = np.array([1,2,1,0,0,0,0,0])
coeff_B = np.array([1,-2,1,0,0,0,0,0])
coeff_C = np.array([1,0,-2,0,1,0,0,0])

# FFT
fft_A = fft.FFT(coeff_A)
fft_B = fft.FFT(coeff_B)
print('fft_A',fft_A)
print('fft_B',fft_B)

product = fft_A*fft_B

print('product',product)

# IFFT
n = len(product)
ifft_c = 1/n*fft.IFFT(product)
print('ifft_c', np.round(ifft_c.real))

test = [int(k) for k in np.round(ifft_c.real)]
print(test == coeff_C)
