import numpy as np
import matplotlib.pyplot as plt

sqrt = np.sqrt
cumsum = np.cumsum

n = 10000
s = [1/sqrt(k) for k in range(1,n)]
a = [6*k**2 for k in s]  # surface cube
v = [k**3 for k in s]    # volume cube
A = cumsum(a)
V = cumsum(v)

fig, ax = plt.subplots()
#ax.set_yscale('log')
plt.plot(A)
plt.plot(V)
plt.show()

plt.plot(a[:100])
plt.plot(v[:100])
plt.show()