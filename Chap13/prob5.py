#WAP to find the maximum of number in a list using reduce function

from functools import reduce

l = [10,1100,30,240,400,49]

def max(a,b):
    if(a>b):
        return a
    return b

a = reduce(max,l)
print(a)