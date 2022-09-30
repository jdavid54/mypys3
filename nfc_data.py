import numpy as np
np.set_printoptions(formatter={'int':hex})
#np.array([1,2,3,4,5])

block = [0xFF]*16
print(block)
h =np.array(block)
print(h)
H = h.reshape(16,1)
print(H)

bl=[chr(x) for x in block]
print(bl)

import binascii
a='45222f'
#a="deadbeef00"
s=binascii.unhexlify(a)
print(s)
b=[chr(x) for x in s]

A = bytearray.fromhex(a)
print('A=',A)
B = [hex(i) for i in block]
print('B=',B)

a = [[1,2],[3,4]]
print([list(map(hex, l)) for l in a])

a = [6, 234, 8, 9, 10, 1234, 555, 98]
print('\n'.join([hex(i) for i in a]))

'''
def twos(val_str, bytes):
    import sys
    if '0x' in val_str:
        val_str=format(int(val_str,16),'08b')
        #print('vs',val_str)
    val = int(str(val_str), 2)
    #print(val)
    b = val.to_bytes(bytes, byteorder=sys.byteorder, signed=False)                                                          
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)

print('bin',twos('11111111',1))
print('bin',twos('01111111',1))

print('hex',twos('0xFF',1))
print('hex',twos('0x7F',1))

# https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros

The format() function simply formats the input following the Format Specification mini language.
The # makes the format include the 0b prefix,
the 010 size formats the output to fit in 10 characters width, with 0 padding;
2 characters for the 0b prefix, the other 8 for the binary digits.
with the 032b size formats an output of 4 bytes (32 bits)
'''
print('0x87d61200',format(0x87d61200,'032b'))
print('0x7829edff',format(0x7829edff,'032b'))

print('0x11',format(0x11,'08b'))
print('0xEE',format(0xee,'08b'))

# keys
# All keys are set to FFFF FFFF FFFFh at chip delivery
#and the bytes 6, 7 and 8 are set to FF0780h.


# sector trailer 16 bytes
#                   111111 
# 012345    6789    012345
#  keyA    access    keyB
#  6bytes  4bytes    6bytes

'''
C13, C23, C33 read, write → 3 sector trailer
C12, C22, C32 read, write, increment, decrement,transfer, restore → 2 data block
C11, C21, C31 read, write, increment, decrement,transfer, restore → 1 data block
C10 ,C20, C30 read, write, increment, decrement,transfer, restore → 0 data block
'''

# access bits
# b : bar or 1's complement
# C23 : C2 for block 3

# byte 6 : C23b, C22b, C21b, C20b, C13b, C12b, C11b, C10b
# byte 7 : C13,  C12,  C11,  C10,  C33b, C32b, C31b, C30b
# byte 8 : C33,  C32,  C31,  C30,  C23,  C22,  C21,  C20
# byte 9 : user data

# access sector trailer (Block 3)
# N:never, A:keyA, B:keyB, A|B:keyA or keyB
# C1 C2 C3   readKeyA  writeKeyA  readAccess writeAccess readKeyB writeKeyB
#  0  0  0      N          A          A          N          A        A
#  0  1  0      N          N          A          N          A        N
#  1  0  0      N          B         A|B         N          N        B
#  1  1  0      N          N         A|B         N          N        N
#  0  0  1      N          A          A          A          A        A
#  0  1  1      N          B         A|B         B          N        B
#  1  0  1      N          N         A|B         B          N        N
#  1  1  1      N          N         A|B         N          N        N

'''         
FF0780 : 1111 1111 = C2b C1b
         0000 0111 = C1  C3b
         1000 0000 = C3  C2
                                       
Bl 3210                  
C1 0000
C2 0000
C3 1000

         C1   C2   C3    rA,wA,ra,wa,rB,wB
Block3 :  0    0    1    (N, A, A, A, A, A)

         C1   C2   C3      r,   w,  inc, d|t|r
Block2 :  0    0    0     (A|B, A|B, A|B, A|B)
Block1 :  0    0    0     (A|B, A|B, A|B, A|B)
Block0 :  0    0    0     (A|B, A|B, A|B, A|B)

===============================================
7F0788  : 0111 1111    (puce raffin)
          0000 0111
          1000 1000

Bl 3210                  
C1 0000
C2 1000
C3 1000

         C1   C2   C3    rA, wA,  ra, wa,rB,wB
Block3 :  0    1    1    (N,  B, A|B,  B, N, B)

         C1   C2   C3        r,   w, inc, d|t|r
Block2 :  0    0    0     (A|B, A|B, A|B, A|B)
Block1 :  0    0    0     (A|B, A|B, A|B, A|B)
Block0 :  0    0    0     (A|B, A|B, A|B, A|B)
'''


# access data blocks
# C1 C2 C3     read       write    increment   decr,trf,rest
#  0  0  0     A|B         A|B        A|B          A|B
#  0  1  0     A|B          N          N            N
#  1  0  0     A|B          B          N            N
#  1  1  0     A|B          B          B           A|B
#  0  0  1     A|B          N          N           A|B
#  0  1  1      B           B          N            N
#  1  0  1      B           N          N            N
#  1  1  1      N           N          N            N