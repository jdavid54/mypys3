# The Notorious Question Six (cracked by Induction) - Numberphile
# Featuring Zvezdelina Stankova
# https://www.youtube.com/watch?v=NcaYEaVTA4g

a = 30
b = 112

def f(a,b):
    return (a**2+b**2)/(1+a*b)

r = f(a,b)
print(r)

def down(a,b):
    while a != 0 and b != 0:
        if r*b-a < r*a-b:
            a,b = (r*b-a, b)
        else:
            a,b = (a, r*a-b)
        print(a,b,f(a,b))

down(a,b)

n = 500000
def up(a,b):
    while a < n and b < n:
        if r*b+a > r*a+b:
            a,b = (r*b-a, b)
        else:
            a,b = (a, r*a-b)
        print(a,b,f(a,b))

up(a,b)