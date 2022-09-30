import numpy as np

x = 4
print(hex(id(x)))

x = 5
y = 4
w = 9999
v = 9999
a = 12345678
b = 12345678
print(hex(id(x)))
print(hex(id(y)))
print(hex(id(w)))
print(hex(id(v)))
print(hex(id(a)))
print(hex(id(b)))

# https://docs.python.org/3/library/ctypes.html

import ctypes
from ctypes import *

bufstr = ctypes.create_string_buffer(b"Test",10)
print(type(bufstr))
print(ctypes.addressof(bufstr))

print(sizeof(bufstr), repr(bufstr.raw))

p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
print(sizeof(p), repr(p.raw))

p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
print(sizeof(p), repr(p.raw))

print(repr(p.value))

p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
print(sizeof(p), repr(p.raw))

p.value = b"Hi"
print(sizeof(p), repr(p.raw))


print('kernel',windll.kernel32)  

print('cdll.msvcrt:', cdll.msvcrt)      

# defining libc
libc = cdll.msvcrt      
libc.printf

print('\ncreate some ctypes variables')
i = c_int()
f = c_float()
s = create_string_buffer(b'\000' * 32)
print('i:',i.value, ',f:',f.value, ',s:', repr(s.value))

print('libc.sscanf==============================================')
libc.sscanf(b"1 3.14 Hello", b"%d %f %s", byref(i), byref(f), s)

print('i:',i.value, ',f:',f.value, ',s:', repr(s.value))

print(libc.time(None))  

print(hex(windll.kernel32.GetModuleHandleA(None)))

# create some ctypes variables
i = c_int(42)
print(i)            # c_long(42)
print(i.value)      # 42

i.value = -99
print(i.value)

s = "Hello, World"
c_s = c_wchar_p(s)
print(c_s)          # c_wchar_p(2022411515472)

print(c_s.value)    # Hello, World

c_s.value = "Hi, there"
print(c_s)              # the memory location has changed c_wchar_p(2022411515472)
print(c_s.value)        # Hi, there

print(s)                # first object is unchanged

# printf
print('91 printf===============================================')
printf = libc.printf
printf(b"Hello, %s\n", b"World!")
printf(b"Hello, %S\n", "World!")
printf(b"%d bottles of beer\n", 42)
printf(b"An int %d, a double %f\n", 1234, c_double(3.14))

# try:
#     printf(b"%f bottles of beer\n", 42.5)
# except:
#     print("""
#     printf(b"%f bottles of beer\n", 42.5)
#     # Traceback (most recent call last):
#     #   File "<stdin>", line 1, in <module>
#     # ArgumentError: argument 2: exceptions.TypeError: Don't know how to convert parameter 2
#     """)
#     
printf(b"An int %d, a double %f\n", 1234, c_double(3.14))
print('109 printf===============================================')




# https://www.quora.com/How-is-a-float-or-double-value-stored-in-memory-in-java
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
import struct
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

print(binary(1.0))
print(binary(10.13))
f = 10.13

def binary(num):
    # Struct can provide us with the float packed into bytes. The '!' ensures that
    # it's in network byte order (big-endian) and the 'f' says that it should be
    # packed as a float. Alternatively, for double-precision, you could use 'd'.
    packed = struct.pack('!f', num)
    #print(type(packed),list(packed))
    print('Packed: %s' % list(packed))

    # For each character in the returned string, we'll turn it into its corresponding
    # integer code point
    # 
    # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
    integers = list(packed)   #[ord(c) for c in list(packed)]
    print([hex(c) for c in list(packed)])
    print('Integers: %s' % integers)

    # For each integer, we'll convert it to its binary representation.
    binaries = [bin(i) for i in integers]
    print('Binaries: %s' % binaries)

    # Now strip off the '0b' from each of these
    stripped_binaries = [s.replace('0b', '') for s in binaries]
    print('Stripped: %s' % stripped_binaries)

    # Pad each byte's binary representation's with 0's to make sure it has all 8 bits:
    #
    # ['00111110', '10100011', '11010111', '00001010']
    padded = [s.rjust(8, '0') for s in stripped_binaries]
    print('Padded: %s' % padded)

    # At this point, we have each of the bytes for the network byte ordered float
    # in an array as binary strings. Now we just concatenate them to get the total
    # representation of the float:
    return ''.join(padded)

print('1:', binary(1))
print('10.13:', binary(10.13))

r = bin(struct.unpack('!i',struct.pack('!f', f))[0])
print(r)


import bitstring
f1 = bitstring.BitArray(float=f, length=32)
print('with bitstring',f1.bin)

int32bits = np.asarray(f, dtype=np.float32).view(np.int32).item()  # item() optional

print(hex(int32bits))
s = '{:032b}'.format(int32bits)
print('with format   ',s)

exponant = '0b'+s[1:9]
exp = int(exponant,2)-127
print(exp, 2**exp)
mantis = s[9:]
print(mantis)

somme = 1
for k,c in enumerate(mantis):
    #print(-(k+1),int(c),sum)
    if int(c):
        somme += 2**-(k+1)
        print(-(k+1),int(c),2**-(k+1),'\t',somme)
result = 2**exp*somme    
print('result:', result)
print(result-f)

int32bits = np.float32(f).view(np.int32).item()
print(hex(int32bits))

#========================================================================
f = 1.0
def float32_bit_pattern(value):
    print(struct.pack('f', value))
    what = [(i,hex(b)) for i,b in enumerate(struct.pack('f', value))]
    print(what)
    return sum(b << 8*i for i,b in enumerate(struct.pack('f', value)))

def int_to_binary(value, bits):
    return bin(value).replace('0b', '').rjust(bits, '0')

pattern = float32_bit_pattern(f)
print(hex(pattern))
 
result = int_to_binary(pattern, 32)
print(result)

# With these two simple functions (Python >=3.6) you can easily convert a float number to binary
# and vice versa, for IEEE 754 binary64.

def bin2float(b):
    ''' Convert binary string to a float.

    Attributes:
        :b: Binary string to transform.
    '''
    h = int(b, 2).to_bytes(8, byteorder="big")
    return struct.unpack('>d', h)[0]


def float2bin(f):
    ''' Convert float to 64-bit binary string.

    Attributes:
        :f: Float number to transform.
    '''
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:064b}'

print(float2bin(1.618033988749894))
print(float2bin(3.14159265359))
print(float2bin(5.125))
print(float2bin(13.80))

print(bin2float('0011111111111001111000110111011110011011100101111111010010100100'))
print(bin2float('0100000000001001001000011111101101010100010001000010111011101010'))
print(bin2float('0100000000010100100000000000000000000000000000000000000000000000'))
print(bin2float('0100000000101011100110011001100110011001100110011001100110011010'))


print(float2bin(10.13))
print(bin2float('0100000000100100010000101000111101011100001010001111010111000011'))


BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


def binary(num):
    return [bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num)]


def binary_str(num):
    bits = ''.join(binary(num))
    return ''.join([BLUE, bits[:1], GREEN, bits[1:10], CYAN, bits[10:], RESET])


def binary_str_fp16(num):
    bits = ''.join(binary(num))
    return ''.join([BLUE, bits[:1], GREEN, bits[1:10][-5:], CYAN, bits[10:][:11], RESET])

x = 0.7
print(x, "as fp32:", binary_str(0.7), "as fp16 is sort of:", binary_str_fp16(0.7))

print('269 binrep')
def binRep(num):
    binNum = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value)[2:]
    print("bits: " + binNum.rjust(32,"0"))
    mantissa = "1" + binNum[-23:]
    print("sig (bin): " + mantissa.rjust(24))
    mantInt = int(mantissa,2)/2**23
    print("sig (float): " + str(mantInt))
    base = int(binNum[-31:-23],2)-127
    print("base:" + str(base))
    sign = 1-2*("1"==binNum[-32:-31].rjust(1,"0"))
    print("sign:" + str(sign))
    print("recreate:" + str(sign*mantInt*(2**base)))

print(binRep(-0.75))