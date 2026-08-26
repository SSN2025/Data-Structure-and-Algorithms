import numpy as np
def greedyKnapsack(num,weight,capacity):
    c = np.array([num,weight])
    print(c)
    print("_______________________")
    c = c[np.argsort(c[:,0]/c[:,1])[::-1]]
    print(c)
    p =0
    n = len(c)
    for i in range(n):
        if(capacity > 0 and c[0][i]<capacity):
            capacity -= c[0][i]
            p += c[1][i]
        else: break
    if(capacity > 0):
        p += c[1][i] * (capacity/c[0][i])
    return p

a = np.array([25,24,15],dtype = float)
b = np.array([18,15,10],dtype = float)
print(greedyKnapsack(a,b,20))

    