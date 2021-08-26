import numpy as np
import matplotlib.pyplot as plt

X = ['Group A','Group B','Group C','Group D']
Ygirls = [10,20,20,40]
Zboys = [20,30,25,30]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

Women = [115, 215, 250, 200]
Men = [114, 230, 510, 370]

n=4
r = np.arange(n)
width = 0.25


plt.bar(r, Women, color = 'b',
    width = width, edgecolor = 'black',
    label='Women')
plt.bar(r + width, Men, color = 'g',
    width = width, edgecolor = 'black',
    label='Men')

plt.xlabel("Year")
plt.ylabel("Number of people voted")
plt.title("Number of people voted in each year")

# plt.grid(linestyle='--')
plt.xticks(r + width/2,['2018','2019','2020','2021'])
plt.legend()

plt.show()
