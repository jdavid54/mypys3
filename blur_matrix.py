import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid


def mul(m, kernel):
    m = np.array(m).reshape((3,3))
    val = 0
    for i in range(3):
        for j in range(3):
            val += m[i][j] * kernel[i][j]
    return val

original = np.ones((10,10))

two_zeros = [1,1,1,1,0,0,1,1,1,1]
three_zeros = [1,1,1,0,0,0,1,1,1,1]
four_zeros = [1,1,1,0,0,0,0,1,1,1]

original[2] = two_zeros
original[4] = two_zeros
original[5] = two_zeros
original[6] = two_zeros

original[3] = three_zeros
original[7] = four_zeros

print(original)

# kernel
box_blur = 1/9*np.ones((3,3))

gauss = np.array([[1/16,1/8,1/16],
         [1/8,1/4,1/8],
         [1/16,1/8,1/16]])

sharpen = np.array([[0, -1, 0],
         [-1, 5, -1],
         [0, -1, 0]])

edge_detection = np.array([[-1, -1, -1],
         [-1, 8, -1],
         [-1, -1, -1]])

kernels = [box_blur, gauss, sharpen, edge_detection]
k_names = ['box_blur', 'gauss', 'sharpen',  'edge_detection']



k = 1
kernel = kernels[k]
print(kernel, k_names[k])

o = np.copy(original)
m = np.ones((3,3))
blur = np.ones((10,10))

for i in range(1,9):
    for j in range(1,9):
        m = [[o[i-1][j-1], o[i-1][j], o[i-1][j+1]],
            [o[i][j-1], o[i][j], o[i][j+1]],
            [o[i+1][j-1], o[i+1][j], o[i+1][j+1]]]
        #val = np.sum(1/9*np.array(m))
        #val = mul(m, kernel)
        val = np.sum(m*kernel)
        #print(i,j,val)
        blur[i][j] = np.round(val, decimals=2)

print(blur)

cmap='gist_gray'
cmap = 'binary'
cmap = 'gist_yarg'
cmap='gray'

t = 10

fig, (ax1,ax2) = plt.subplots(2)
ax1.imshow(original, cmap=cmap)
ax2.imshow(blur, cmap=cmap)
ax2.set_xlabel(k_names[k])
ax1.set_xticks(np.arange(0, t, 1));
ax1.set_yticks(np.arange(0, t, 1));
ax2.set_xticks(np.arange(0, t, 1));
ax2.set_yticks(np.arange(0, t, 1));
fig.tight_layout()
plt.show()

