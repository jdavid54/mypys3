# https://www.youtube.com/watch?v=as7Gkm7Y7h4
# https://datagenetics.com/blog/december12014/index.html
# https://www.youtube.com/watch?v=wTJI_WuZSwE

# Prisoner 1 walks in, sees a chessboard where each square has a coin on top,
#flipped either to heads or tails.  The warden places the key under one of
#the squares, which prisoner 1 sees.  Before he leaves, he must turn over
#one and only one coin.  Prisoner 2 then walks in and is supposed to be able
#to figure out which squares the key is in just by looking at the arrangement
#of coins.

import numpy as np
# importing functools for reduce()
import functools
from operator import xor

rand = True

def get_parity():
    filter={}
    parity=[]
    for k in range(6):
        mask = 2**k
        filter[k] = [i for i, bit in enumerate(bloc) if (bit and ((i & mask)==mask))]
        #print(mask,filter[k],len(filter[k]))
        parity.append('0' if (len(filter[k])%2==0) else '1')
    return parity


if not rand:
    # grid to test
    print('fixed block')
    bloc = np.array([
            0, 1, 1, 0, 1, 1, 0, 1,
            1, 0, 0, 0, 0, 1, 1, 1,
            1, 0, 1, 0, 0, 0, 1, 0,
            0, 0, 1, 1, 0, 1, 1, 0,
            0, 0, 1, 0, 0, 0, 1, 0,
            1, 0, 1, 1, 0, 1, 0, 1,
            1, 1, 1, 1, 1, 0, 1, 1,
            1, 1, 0, 1, 1, 0, 0, 0])
    # random blocks can be uncorrect coded blocks
    natural_parity = '001011'
else:
    print('random target')
    bloc = np.random.randint(0,2,64)
    
locations_w_ones = [i for i, bit in enumerate(bloc) if bit]
print(locations_w_ones )
print(bloc.reshape(8,8))

target = np.random.randint(0,64)
#target = 20
print('target =', target)

# compute parity
parity = get_parity()
parity.reverse()
      
if rand:
    natural_parity = ''.join(parity)
print('natural parity', int(natural_parity,2),natural_parity)

# case to flip
# flip = target xor natural_parity
flip = target ^ int(natural_parity,2)
print('case to flip',flip)

#print(bloc.reshape(8,8))
print('Bloc after flip')
# flip at case
bloc[flip] = not bloc[flip]
print(bloc.reshape(8,8))

# compute the 6-bit new parity from block after flip
# this will give the number of the target
parity = get_parity()
parity.reverse()
print(parity)

# the parity is the target case to be found
derived_target = int(''.join(parity),2)
print('original target =', target)
print('Derived target', derived_target)