import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
plt.style.use(['science', 'notebook'])
import sympy as smp

# Problem 1
#part A
theta, alpha = smp.symbols(r'\theta \alpha', real=True, positive=True)
theta, alpha = smp.symbols(r'\theta \alpha', real=True, positive=True)
dsdo = smp.Rational(1,2)*(1+smp.cos(theta)**2)/(1+alpha*(1-smp.cos(theta)))**2 * \
            ( 1 + alpha**2 * (1-smp.cos(theta))**2 / ((1+smp.cos(theta)**2)*(1+alpha*(1-smp.cos(theta)))))
dsdt = 2*smp.pi*dsdo*smp.sin(theta)
dsdt = dsdt.simplify()
print(dsdt)

#part B
s = smp.integrate(dsdt, (theta, 0, smp.pi))
s = s.simplify().simplify()
print(s)

'''
# part C
pdf_theta = dsdt / s
pdf_theta=pdf_theta.simplify()
print(pdf_theta)

pdf_omega = dsdo / s
pdf_omega=pdf_omega.simplify()
print(pdf_omega)

pdf_theta_f = smp.lambdify([theta,alpha], pdf_theta)
pdf_omega_f = smp.lambdify([theta,alpha], pdf_omega)

the = np.linspace(0, np.pi, 1000)
pdf_t = pdf_theta_f(the, 0.1)
pdf_o = pdf_omega_f(the, 0.1)

fig, axes = plt.subplots(1,2,subplot_kw={'projection': 'polar'})
axes[0].plot(the, pdf_t)
axes[0].set_title(r'$f(\theta)$', fontsize=20)
axes[1].plot(the, pdf_o)
axes[1].set_title(r'$g(\theta, \phi)$', fontsize=20)
plt.show()

theta = np.linspace(0, np.pi, 1000)
alphas = 10.0** np.linspace(-3,4,300)
pdfs = [pdf_theta_f(theta, alpha) for alpha in alphas]

#make animation
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ln, = plt.plot([], [])

def animate(i):
    ax.clear()
    ax.plot(theta, pdfs[i])
    ax.set_title(r'$\alpha=$'+f'{alphas[i]:.2f}')
    
# ani = animation.FuncAnimation(fig, animate, frames=299, interval=50)
# ani.save('ani3.gif',writer='pillow',fps=30,dpi=100)
'''
# Problem 2
#part A

E, Ep, alpha, T, theta = smp.symbols(r"E E' \alpha T \theta", real=True, positive=True)

Ep_expr = E/(1+alpha*(1-smp.cos(theta)))
print(Ep_expr)

print(Ep - Ep_expr)

theta_expr = smp.solve(Ep-Ep_expr, theta)[1]
print(theta_expr)

pdf_Ep = 1/s * dsdt / smp.diff(Ep_expr, theta)
print(pdf_Ep)

# substitute theta by E'
pdf_Ep = pdf_Ep.subs(theta, theta_expr).simplify()
print(pdf_Ep)

test = smp.integrate(pdf_Ep, (Ep, E, E/(1+2*alpha))).simplify()
print(test)

# part B
T_expr = E*alpha*(1-smp.cos(theta))/(1+alpha*(1-smp.cos(theta)))
theta_expr = smp.solve(T-T_expr, theta)[1]
pdf_T = 1/s * dsdt / smp.diff(T_expr, theta)
pdf_T = pdf_T.subs(theta, theta_expr).simplify()
print(pdf_T)

test = smp.integrate(pdf_T, (T, 0, 2*E*alpha/(1+2*alpha))).simplify()
print(test)

# animation
pdf_Ep_f = smp.lambdify([Ep, E, alpha], pdf_Ep)
pdf_T_f = smp.lambdify([T, E, alpha], pdf_T)

m = 0.511
alpha = 2
E = alpha*m
Ep = np.linspace(E/(1+2*alpha), E, 1000)
T = np.linspace(0, 2*E*alpha/(1+2*alpha), 1000)

plt.figure(figsize=(6,3))
#plt.plot(100*Ep/(E), -pdf_Ep_f(Ep, E, alpha), label='Outgoing Photon')
plt.plot(100*T/(E), pdf_T_f(T, E, alpha), label='Outgoing Electron')
plt.xlabel('% Incoming Energy')
plt.ylabel('Probability Density')
#plt.legend(ncol=1, fontsize=10, facecolor='white', framealpha=1, frameon=True, loc='upper center')
plt.grid()
plt.savefig('samp.png', dpi=200)
plt.show()

# grid of alphas
alphas = 10.0** np.linspace(-3,4,300)
Eps = [np.linspace(alpha*m/(1+2*alpha), alpha*m, 1000) for alpha in alphas]
Ts = [np.linspace(0, 2*alpha*m*alpha/(1+2*alpha), 1000) for alpha in alphas]
pdfs_Ep = [-pdf_Ep_f(Ep, alpha*m, alpha) for (alpha, Ep) in zip(alphas, Eps)]
pdfs_T = [pdf_T_f(T, alpha*m, alpha) for (alpha, T) in zip(alphas, Ts)]

fig, ax = plt.subplots(figsize=(8,5))

def animate(i):
    alpha = alphas[i]; Ep=Eps[i]; T = Ts[i]
    E = m*alpha
    ax.clear()
    ax.plot(100*Ep/E, -pdf_Ep_f(Ep, E, alpha), label='Outgoing Photon')
    ax.plot(100*T/E, pdf_T_f(T, E, alpha), label='Outgoing Electron')
    ax.set_xlabel('% Incoming Energy')
    ax.set_ylabel('Probability Density')
    ax.legend(ncol=1, fontsize=10, facecolor='white', framealpha=1, frameon=True, loc='upper center')
    ax.set_title(r'$\alpha=$'+f'{alpha:.2f}')
    
ani = animation.FuncAnimation(fig, animate, frames=299, interval=50)
ani.save('ani4.gif',writer='pillow',fps=30,dpi=100)

# end https://github.com/lukepolson/youtube_channel/blob/main/Python%20Metaphysics%20Series/vid30.ipynb
