ls=[2,0,5,10,15,100,24,25,80]

nls=filter(lambda x : x%5 == 0 ,ls)
#either def divisible5(n):
#     if (n%5 == 0):
#        return True
# return false
# nls=filter(divisible5,ls)

print(list(nls))