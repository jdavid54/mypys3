import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.style.use(['science', 'notebook'])
import sympy as smp
# https://scikit-image.org/docs/stable/install.html
from skimage import color
from skimage import io
from scipy.fft import fftfreq
from scipy.fft import fft, ifft, fft2, ifft2

#  Fourier Transform (Continuous time and frequency)
t, f = smp.symbols('t, f', real=True)
t, f = smp.symbols('t, f', real=True)
k = smp.symbols('k', real=True, positive=True)
x = smp.exp(-k * t**2) * k * t
print(x)

from sympy.integrals.transforms import fourier_transform
x_FT = fourier_transform(x, t, f)
print(x_FT)

# Won't run
#x = smp.exp(-k * t**2) * smp.sin(k*t) * t**4
#fourier_transform(x, t, f)
from scipy.integrate import quad

def x(t, k):
    return np.exp(-k * t**2) * np.sin(k*t) * t**4

def get_x_FT(x, f, k):
    x_FT_integrand_real = lambda t: np.real(x(t, k)*np.exp(-2*np.pi*1j*f*t))
    x_FT_integrand_comp = lambda t: np.imag(x(t, k)*np.exp(-2*np.pi*1j*f*t))
    x_FT_real = quad(x_FT_integrand_real, -np.inf, np.inf)[0]
    x_FT_comp = quad(x_FT_integrand_comp, -np.inf, np.inf)[0]
    return x_FT_real + 1j*x_FT_comp

f = np.linspace(-4, 4, 100)
x_FT = np.vectorize(get_x_FT)(x, f, k=2)

# Plot
plt.plot(f, np.abs(x_FT))
plt.ylabel('$|\hat{x}(f)|$', fontsize=20)
plt.xlabel('$f$', fontsize=20)
plt.show()

# Fourier Series (Continuous Time, Discrete Frequency)
# Consider now only between t=0 to t=1
t = smp.symbols('t', real=True)
k, n, T = smp.symbols('k, n, T', real=True, positive=True)
fn = n/T
x = smp.exp(-k * t)
print(x)

# Compute the Fourier transform analytically:
x_FT = smp.integrate(1/T * x*smp.exp(-2*smp.pi*smp.I*fn*t), (t, 0, T)).simplify()
print(x_FT)
print(smp.Abs(x_FT).simplify())

get_FT = smp.lambdify([k, T, n], x_FT)
ns = np.arange(0, 20, 1)
xFT = get_FT(k=1, T=4, n=ns)

# Plot:
plt.figure(figsize=(10,3))
plt.bar(ns, np.abs(xFT))
plt.xticks(ns)
plt.ylabel('$|\hat{x}_n|$', fontsize=25)
plt.xlabel('$n$', fontsize=25)
plt.show()

def x(t, k):
    return np.exp(-k * t**2) * np.sin(k*t) / t

def get_x_FT(x, n, k, T):
    x_FT_integrand_real = lambda t: np.real(x(t, k)*np.exp(-2*np.pi*1j*(n/T)*t))
    x_FT_integrand_comp = lambda t: np.imag(x(t, k)*np.exp(-2*np.pi*1j*(n/T)*t))
    x_FT_real = quad(x_FT_integrand_real, 0, T)[0]
    x_FT_comp = quad(x_FT_integrand_comp, 0, T)[0]
    return x_FT_real + 1j*x_FT_comp

ns = np.arange(0, 20, 1)
xFT = np.vectorize(get_x_FT)(x, ns, k=2, T=4)

# Plot
plt.figure(figsize=(10,3))
plt.bar(ns, np.abs(xFT))
plt.xticks(ns)
plt.ylabel('$|\hat{x}_n|$', fontsize=25)
plt.xlabel('$n$', fontsize=25)
plt.show()


# 3. Discrete Fourier Transform (Discrete Time, Discrete Frequency)
T = 40 #seconds
N = 100 #measurements
t = np.linspace(0, T, N)
dt = np.diff(t)[0]

# Look at a couple particular frequencies
f1 = 20/(N*dt)
f2 = 10/(N*dt)
f3 = (10+5*N)/(N*dt)

# Get a few time series:
x1 = np.sin(2*np.pi*f1*t) + 0.3*np.sin(2*np.pi*f2*t) + 0.3*np.random.randn(len(t))
x2 = np.sin(2*np.pi*f2*t)+ 0.1*np.random.randn(len(t))
x3 = np.sin(2*np.pi*f3*t)+ 0.1*np.random.randn(len(t))
plt.plot(t, x1)
plt.xlabel('$t$ [seconds]', fontsize=20)
plt.ylabel('Signal [arb]')
plt.show()

f = fftfreq(len(t), np.diff(t)[0])
x1_FFT = fft(x1)

# Plot the first half of the spectrum (for  real, all information is contained in the first half)
plt.plot(f[:N//2], np.abs(x1_FFT[:N//2]))
plt.xlabel('$f_n$ [$s^{-1}$]', fontsize=20)
plt.ylabel('|$\hat{x}_n$|', fontsize=20)
plt.show()

print(f2)
print(f3)

plt.plot(t,x2)
plt.plot(t,x3)
plt.xlabel('$t$ [seconds]', fontsize=20)
plt.ylabel('Signal [arb]')
plt.show()


x2_FFT = fft(x2)
x3_FFT = fft(x3)
plt.plot(f[:N//2], np.abs(x2_FFT[:N//2]), label='$x_2$')
plt.plot(f[:N//2], np.abs(x3_FFT[:N//2]), 'r--', label='$x_3$')
plt.axvline(1/(2*dt), ls='--', color='k')
plt.xlabel('$f_n$ [$s^{-1}$]', fontsize=20)
plt.ylabel('|$\hat{x}_n$|', fontsize=20)
plt.show()


img = color.rgb2gray(color.rgba2rgb(io.imread('images/flower.PNG')))
print(img)

plt.imshow(img, cmap='gray')
plt.show()


img_FT = fft2(img)
fy = np.fft.fftfreq(img.shape[0],d=10) #suppose the spacing between pixels is 10mm, for example
fx = np.fft.fftfreq(img.shape[1],d=10)
print('{:.2f} correponds to fx={:.6f} and fy={:.6f}'.format(img_FT[10,20], fx[20], fy[10]))


plt.imshow(np.abs(img_FT), cmap='gray', vmax=50)
plt.colorbar()
plt.show()

img_FT_alt = np.copy(img_FT)
img_FT_alt[-2:] = 0 
img_FT_alt[:,-2:] = 0 
img_FT_alt[:2] = 0 
img_FT_alt[:,:2] = 0 
img_alt = np.abs(ifft2(img_FT_alt))
plt.imshow(img_alt, cmap='gray')
plt.colorbar()
plt.show()

# END