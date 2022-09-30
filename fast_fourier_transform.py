import numpy as np
exp = np.exp
pi = np.pi


def DFT(n): # discreet fourier transform matrix
    m = np.zeros((n,n),complex)
    w = exp(2*pi*1j/n)
    if debug: print('w =',w)
    for i in range(n):        
        for j in range(n):
            if debug : print('w**',i*j,'=',w**(i*j))
            m[i][j] = w**(i*j)
    return m

def iDFT(n): # discreet fourier transform inverse matrix
    m = np.zeros((n,n),complex)
    w = exp(-2*pi*1j/n)
    if debug: print('w =',w)
    for i in range(n):        
        for j in range(n):
            if debug : print('w**',i*j,'=',w**(i*j))
            m[i][j] = w**(i*j)/n
    return m
#print('Discreet fourier transform matrix :\n',DFT(5))

def FFT(P):
    # P is a polynomial with [p0,p1,...p(n-1)] as coeff representation
    n = len(P)  # n must be a power of 2
     
    if debug: print('n :',n)
    if n==1:
        return P
    w = exp(2*pi*1j/n)
    Pe, Po = P[::2], P[1::2]
    ye, yo = FFT(Pe), FFT(Po)
    
    y = [0]*n
    # see t=19:52 youtube https://www.youtube.com/watch?v=h7apO7q16V0
    # P(x_j) = Pe(x_j**2) + x_j * Po(x_j**2)
    # P(-x_j) = Pe(x_j**2) - x_j * Po(x_j**2)
    # with j in [0, 1, ...., n/2-1]
    
    # paired points
    # x_j = w**j => P(x_j) = y[j]
    # -x_j = w**(j+n/2) => P(-x_j) = y[j+n/2]
    for j in range(int(n/2)):
        y[j] = ye[j] + w**j * yo[j]  
        y[j+int(n/2)] = ye[j] - w**j*yo[j]
        if debug: print(j,'y =', y)
    if debug:
        print('w:',w)
        print('Pe :',Pe,',Po :',Po)
        print('ye :',ye,'\nyo :',yo,'\n')
    return np.array(y)
 

def IFFT(P):
    # P is a polynomial with [P(w0),P(w1),...,P(w_n-1)] as value representation
    n = len(P)  # n must be a power of 2
    
    if debug: print('n :',n)
    if n == 1: # base case
        return P
    # division by n of w must be out of function IFFT because of recursive side effect
    w = exp(-2*pi*1j/n)
    Pe, Po = P[::2], P[1::2]
    ye, yo = IFFT(Pe), IFFT(Po)
    
    y = [0]*n
    for j in range(int(n/2)):
        y[j] = ye[j] + w**j * yo[j]
        y[j+int(n/2)] = ye[j] - w**j * yo[j]
    if debug:
        print('n:',n,',w:',w)
        print('Pe:',Pe,',Po:',Po)
        print('ye:',ye,'\nyo:',yo,'\n')
    #print('y',y)
    return np.array(y)

debug = False

if __name__ == "__main__":
    # execute only if run as a script 
    P = [1, 2, 0, 7, 1, 0, 0, 0]   # y = 1 + 2x + 7x**3 + x**4
    P = [0, 0, 1, 0]  # y = x**2
    

    # calc FFT of P
    fft = FFT(P) 
    print('FFT(P) =', fft, len(fft))

    # calc of iftt of fft
    # division by n must be out of function IFFT because of recursive side effect
    n = len(fft)
    ifft = 1/n * IFFT(fft)  # fft = [P(w0), P(w1), ..., P(wn-1)]
    print('IFFT =', ifft, len(ifft))
    print('IFFT(fft)=', ifft.real)

    # recap
    print('\nRecap=====================================')
    n = len(P)
    print(n,'P =',P)

    # FFT
    # by function FFT
    fft = FFT(P)
    print('FFT function result on P:\n',fft)

    # by matrix dft
    dft = DFT(n)
    if debug: print('The dft matrix:\n',dft)
    print('Apply dft matrix product on P:\n',np.dot(dft,P))
    print('comparing fft and dft product:\n',np.round(fft,2)==np.round(np.dot(dft,P),2)) # ok

    # inverse FFT
    # by function IFFT
    ifft = 1/len(fft) * IFFT(fft)
    print('IFFT function result on fft:\n',np.round(ifft))
    print(P,'\n') 

    # by matrix idft
    idft = iDFT(n)
    if debug: print('The idft matrix:\n', idft)
    print('Apply idft matrix product on fft:\n',np.round(np.dot(idft, fft)).real)
    print(P)
    print('comparing P and dft product:\n',np.round(P,2)==np.round(np.dot(idft, fft),2))     # ok

    # error in w expression inside IFFT(), division by n must be outside
    print(np.round(ifft,2))
    # by IFFT
    print(np.round(np.dot(idft, fft),2))
    # by iDFT matrix
    print('compare ifft and idft matrix product:\n',np.round(ifft,2)==np.round(np.dot(idft, fft),2))  # ok
