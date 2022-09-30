import numpy as np

# heron's formula
# A = sqrt(s*(s-a)*(s-b)*(s-c))

def area(a,b,c):
    s = .5*(a+b+c)
    print(s-a,s-b,s-c,s)
    return  np.sqrt(s*(s-a)*(s-b)*(s-c))