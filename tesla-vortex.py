
root = 1
multiplier = 240  # petals = multiplier-1
modulus = 100
seq = []
for k in range(10):
    n = root*multiplier**k
    r = n%modulus
    print(n, r)
    if r not in seq:
        seq.append(r)
print(seq)    