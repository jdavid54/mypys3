import numpy as np
import matplotlib.pyplot as plt

a = np.arange(4)
p = np.linspace(0, 100, 6001)
ax = plt.gca()
lines = [
    ('linear', None),
    ('higher', '--'),
    ('lower', '--'),
    ('nearest', '-.'),
    ('midpoint', '-.'),
]
for interpolation, style in lines:
    ax.plot(
        p, np.percentile(a, p, interpolation=interpolation),
        label=interpolation, linestyle=style)
ax.set(
    title='Interpolation methods for list: ' + str(a),
    xlabel='Percentile',
    ylabel='List item returned',
    yticks=a)
ax.legend()
plt.show()

# percentile

a = np.array([[10, 7, 4], [3, 2, 1]])
print(a)
# array([[10,  7,  4],
#        [ 3,  2,  1]])
print('50%',np.percentile(a, 50))
#3.5
print('50% axis=0', np.percentile(a, 50, axis=0))
#array([6.5, 4.5, 2.5])
print('50% axis=1', np.percentile(a, 50, axis=1))
#array([7.,  2.])
print('50% axis=1 keepdims=True',np.percentile(a, 50, axis=1, keepdims=True))
#array([[7.],
#       [2.]])
m = np.percentile(a, 50, axis=0)
out = np.zeros_like(m)  #output
print('50% axis=0 out=out', np.percentile(a, 50, axis=0, out=out))
#array([6.5, 4.5, 2.5])
print('50% axis=0', m)
#array([6.5, 4.5, 2.5])
b = a.copy()
print('50% axis=1 overwrite', np.percentile(b, 50, axis=1, overwrite_input=True))
#array([7.,  2.])
assert not np.all(a == b)
#assert np.all(a == b)  # assertion error