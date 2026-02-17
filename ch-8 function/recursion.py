def recu(n):
    
    if(n==0 or n==1):#base condition
     return 1
    else:
       return n*recu(n-1) #function calling


n=int(input("enter a number"))
print( "factorial of a number =" ,recu(n))
# print( f"factorial of a number={recu(5) }") #using f string