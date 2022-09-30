import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=ovJcsL7vyrk

max = 50
start = 0.9

r = 3.1  # 2 branches if r > 3
r = 3.5  # 4 branches if r > 3.5
r = 0.5  # decrease to zero if 0 < r =< 1
r = 1.2 # increase if r > 1
r = 2.8

def next_(start):
    data = []
    result = start
    for g in range(max):
        data.append(round(result,5))
        result = r*result*(1-result)        
        #print(result)
        if result <0: break
        #print(result)
    return data

y = next_(0.9)
print(y)
x = range(max)

plt.title('r='+str(r))
plt.plot(x[max-10:],y[max-10:],'r-')
plt.show()