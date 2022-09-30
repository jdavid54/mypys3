import numpy as np
# sum of adjacent elements is a square
# all sequences with n>=25 has a solution, n is the sequence length
# impossible : 1-14, 18-22, 24
# ok : 15-17, 23, 25-.....
# seq25 = 23 2 14 22 3 13 12 4 21 15 10 6 19 17 8 1 24 25 11 5 20 16 9 7 18
# C++ : exe in downloads/sq
# run : ./squares -n 100 -screen 

sqrt = np.sqrt

seq = (1,80,64,36,85,84,16,48,73,71,50,94,75,69,100,96,4,5,76,24,97,72,49,95,74,47,17,19,45,99,22,59,62,82,
 39,25,11,70,51,30,91,53,28,93,7,57,43,78,66,34,87,13,68,32,89,55,9,27,54,90,31,18,46,98,2,14,86,35,65,
 79,42,58,63,81,40,41,23,26,38,83,61,60,21,15,10,6,3,33,67,77,92,52,29,20,44,37,12,88,56,8)

def test(seq):
    test = True
    for i,v in enumerate(seq[:-1]):
        s = sqrt(seq[i]+seq[i+1])
        test = test and int(s)==s
        #print (seq[i], seq[i+1], seq[i]+seq[i+1], s, int(s)==s)
        if test == False:
            print (i, seq[i], seq[i+1], seq[i]+seq[i+1], s, int(s)==s)
            return
    return test    
    
seq = (8,1,15,10,6,3,13,12,4,5,11,14,2,7,9)

def mul(seq,m):
    return list(m*i for i in seq)

def shift(seq,s):
    return list(v+s if i%2==0 else v-s for i,v in enumerate(seq))

def rev(seq):
    return list(reversed(seq))

def r_shift(seq,s):
    return list(reversed(list(v+s if i%2==0 else v-s for i,v in enumerate(seq))))

'''
seq4= mul(seq,4)
print(seq4)
print(sorted(seq4))


seq9= mul(seq,9)

for k in range(-4,5,1):
    print(shift(seq9,k))
'''    
rs0 = (1,8,28,21,4,32,17,19,6,30,34,15,10,26,23,13,12,24,25,11,5,20,29,35,14,2,7,18,31,33,16,9,27,22,3)


'''
seqs = []
s25 = mul(rs0,25)
for k in range(-12,13,1):
    seqs.append(shift(s25,k))
    print(shift(s25,k))
'''

def _next(s):
    s25 = mul(s,25)
    rs = [1]+shift(s25,-1)+shift(s25,1)+rev(shift(s25,-7))+shift(s25,6)+shift(s25,-6)+rev(shift(s25,0))
    rs += [11]+rev(shift(s25,-5))+[5,4,12]+shift(s25,-12)+shift(s25,12)+rev(shift(s25,7))+shift(s25,-8)+rev(shift(s25,2))
    rs += shift(s25,-3)+[9,7]+shift(s25,4)+shift(s25,-4)+[10,6]+shift(s25,5)+rev(shift(s25,-11))+[2]+shift(s25,-2)+[8]
    rs += shift(s25,3)+rev(shift(s25,-9))+rev(shift(s25,9))+shift(s25,-10)+shift(s25,10)+shift(s25,11)+rev(shift(s25,8))+[3]
    return rs

rs1 = _next(rs0)
print(rs1, len(rs1))

rs2 = _next(rs1)
print(rs2, len(rs2))
print(test(rs2))
'''
rs3 = _next(rs2)
print(rs3, len(rs3))
print(test(rs3))

# take more time to generate and test
rs4 = _next(rs3)
print(rs4, len(rs4))
'''


# seq ninja S, L
S = [1,8,41,40,9,27,37,12,24,25,39,10,26,38,11,5,4,32,17,19,6,30,34,15,21,28,36,13,23,2,7,18,31,33,16,20,29,35,14,22,3]
#L = [1,15,10,39,25,24,40,41,23,26,38,11,5,20,29,35,14,2,34,30,19,6,3,22,42,7,18,31,33,16,9,27,37,12,13,36,28,21,4,32,17,8]
L =[1,35,29,20,16,33,3,22,14,2,23,13,36,28,21,15,34,30,6,19,17,32,4,5,31,18,7,42,39,10,26,38,11,25,24,12,37,27,9,40,41,8]

s = sorted([i for n,i in enumerate(S) if n%2!=0])
l = sorted([i for n,i in enumerate(L) if n%2!=0])

S49 = mul(S,49)
L49 = mul(L,49)
Snew = [1,8]+r_shift(S49,-11)+r_shift(S49,-16)+shift(L49,-1)+r_shift(L49,1)+[14,22]
Snew += r_shift(L49,14)+[18]+r_shift(L49,10)+shift(L49,13)+[21,4]+shift(S49,-4)+r_shift(L49,6)
Snew += shift(L49,17)+shift(S49,-24)+shift(L49,24)+shift(S49,-17)+shift(S49,-10)+r_shift(L49,0)+shift(L49,2)
Snew += r_shift(S49,-8)+r_shift(S49,-19)+r_shift(L49,22)+r_shift(S49,-22)+r_shift(L49,19)
Snew += [13,12]+r_shift(L49,4)+shift(S49,-2)+r_shift(L49,8)+[24]+r_shift(L49,16)+shift(L49,7)
Snew += r_shift(S49,-3)+shift(S49,-14)+shift(S49,-13)+[10,6,19]+r_shift(L49,11)+shift(S49,-9)
Snew += shift(L49,9)+[17]+shift(L49,15)+[23,2,7,9,16,20]+r_shift(L49,12)+r_shift(S49,-12)
Snew += r_shift(S49,-15)+[15]+r_shift(S49,-18)+r_shift(L49,23)+r_shift(S49,-23)
Snew += r_shift(L49,18)+shift(L49,5)+r_shift(S49,-5)+[5,11]+shift(L49,21)+shift(S49,-20)
Snew += shift(S49,-7)+r_shift(L49,3)+shift(L49,20)+shift(S49,-21)+shift(S49,-6)

Lnew = [1]+shift(S49,-14)+r_shift(S49,-24)+r_shift(L49,17)+shift(L49,6)+r_shift(S49,-4)
Lnew += shift(S49,-13)+[10,6,19]+r_shift(L49,11)+[4,21]+r_shift(L49,13)+shift(L49,10)+[18]
Lnew += shift(L49,14)+[22,3]+r_shift(S49,-6)+shift(L49,8)+[16]+shift(L49,16)+[24]+shift(S49,-9)
Lnew += shift(L49,9)+[17]+shift(L49,15)+[23,2,14]+shift(L49,1)+[9,7]+r_shift(L49,-1)+shift(L49,24)
Lnew += shift(S49,-17)+r_shift(S49,-21)+r_shift(L49,20)+[12]+r_shift(L49,4)+shift(L49,-2)
Lnew += r_shift(L49,2)+shift(L49,21)+shift(S49,-20)+shift(S49,-7)+shift(L49,7)+[15]+r_shift(S49,-18)
Lnew += r_shift(L49,23)+shift(L49,0)+r_shift(S49,-10)+shift(L49,12)+[20,5]+r_shift(S49,-8)
Lnew += r_shift(S49,-19)+r_shift(L49,22)+r_shift(S49,-22)+r_shift(L49,19)+[13]
Lnew += r_shift(S49,-16)+shift(L49,18)+shift(S49,-23)+r_shift(S49,-15)+r_shift(S49,-12)
Lnew += shift(S49,-5)+r_shift(L49,5)+shift(S49,-3)+shift(L49,3)+[11]+shift(S49,-11)+[8]


