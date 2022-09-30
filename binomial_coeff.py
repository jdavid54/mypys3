from scipy.special import binom, comb

# 
# comb(N,k) : The number of combinations of N things taken k at a time.

# https://en.wikipedia.org/wiki/Binomial_coefficient
# binom(x,y) = x! / y!(x-y)!    [x,y] reals

x, y = 3, 2
bc = (binom(x, y), comb(x, y), comb(x, y, exact=True))

print(bc)

x, y = 43, 23
bc=(binom(x, y), comb(x, y), comb(x, y, exact=True))

print(bc)