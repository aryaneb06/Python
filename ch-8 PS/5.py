def patt(n):
    if(n== 0):
        return 
    else:
        print("*" *n)
        patt(n-1)

n=int(input("enter a number :"))
patt(n)


# using loop
# n=int(input("enter a number :"))
# for i in range(n,0,-1):
#     print("*"*i )