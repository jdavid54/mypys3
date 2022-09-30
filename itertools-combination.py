import itertools
# https://inventwithpython.com/blog/2021/07/03/combinations-and-permutations-in-python-with-itertools/

nl = '\n'


# The permutations and combinations of the set {'A', 'B', 'C'} are:

# Permutations                   Combinations
# ABC, ACB, BAC, BCA, CAB        (none), A, B, C, AB, AC, BC, ABC

# Permutations of n   Values       Combinations of n Values
# Without Repetition   n!                2^n
# With Repetition      n^n       "2n choose n", that is, (2n)! / (n!)^2

# Permutations with Repetition/replacement    
# AAA, AAB, AAC, ABA, ABB, ABC, ACA, ACB, ACC, BAA, BAB, BAC, BBA, BBB, BBC, BCA, BCB, BCC, CAA, CAB, CAC, CBA, CBB, CBC, CCA, CCB, CCC   

# Combinations with Repetition/replacement
# (none), A, B, C, AA, AB, AC, BB, BC, CC, AAA, AAB, AAC, ABB, ABC, ACC, BBB, BBC, BCC, CCC

# permutations no replacement
print(list(itertools.permutations(['A', 'B', 'C'])))
print(nl)

# combinations no replacement
# 2 elements from ['A', 'B', 'C']
print('no repetition',list(itertools.combinations(['A', 'B', 'C'], 2)))
print(nl)
# 3 elements from set
_set = ['A', 'K', 'Q', 'J','10','9','8','7']
print('3 from set',list(itertools.combinations(_set, 3)))
print(nl)


print('with replacement',list(itertools.combinations_with_replacement(['A', 'B', 'C'], 2)))
print(nl)
      

# To get permutations with repetition/replacement, call itertools.product() and pass the size of the iterable object for its repeat argument.
print(list(itertools.product(['A', 'B', 'C'], repeat=3)))
print(nl)