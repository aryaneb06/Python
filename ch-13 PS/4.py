from functools import reduce
ls=[2,0,5,10,15,100,24,25,80]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,ls))