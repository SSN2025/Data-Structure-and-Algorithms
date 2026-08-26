import numpy as np


def split(a):
    mid = a.size//2
    a0 = a[0:mid]
    a1 = a[mid:a.size]
    return a0,a1,mid

def multiply(a,b):
    n = a.size
    m = b.size
    if(n==1 or m==1):
        return a*b
    a0,a1,power = split(a)
    b0,b1,temp  = split(b)


    a0b0 = multiply(a0,b0)
    a1b1 = multiply(a1,b1)


    middle = multiply((a0+a1),(b0+b1)) - a0b0 - a1b1
    result = np.zeros(n+m-1,dtype =int)
    result[:a0b0.size] += a0b0
    result[power:power+middle.size]+=middle
    result[2*power : 2*power+a1b1.size]+=a1b1

    return result
    
a = np.array([1, 5, 32, 1, 0, 0, 0 ,0])
b = np.array([1, 0, 0, 3, 45, 2, 0 ,0])
print(multiply(a,b))