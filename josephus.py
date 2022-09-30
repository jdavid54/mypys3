def safe_seat(n):
    p=0
    l=n
    while l>=2**p:
        p+=1
        l=n
        l-=2**p 
    print(n,'\t',2*l+1) 

n = 50
print('n\tseat')    
for n in range(2,n+1):
    safe_seat(n)
    
print()
k=n
p=0
while k>1:
    p+=1
    k=k>>1
    print(k)
l=n-2**p
print(2**p, 2*l+1)

print()
print(2*n - 2**(p+1) +1)

# if n is a power of 2 + , ie. n=2**k then 2*n=2**(m+1) so we have 2**(m-p) + 1