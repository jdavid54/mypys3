import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('science')  # need latex

x = np.linspace(0,15,30)
y = np.sin(x) + 0.1*np.random.randn(len(x))
plt.plot(x,y)
plt.show()