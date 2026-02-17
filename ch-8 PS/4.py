def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)

n=int(input("enter a number"))
print(f"sum of n natural number is :  {sum(n)}")