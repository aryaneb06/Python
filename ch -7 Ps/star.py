n=int(input("enter a number"))
# for i in range(1,n+1):
    # print(" " * (n-i),end="")
    # print("*" * (2*i-1))
    # # print(" ")
 # another pattern
 #  print("*" * (2*i-1))

#  another pattern
for i in range(1 ,n+1):
   if(i==1 or i==n):
      print("*" * n )

   else:
    #   print("*" *1 ,end="")
    #   print(" " *(n-2) ,end="")
    #   print("*" *1 ,end="")
    #   print(" ")
    #  other way to write else statement at a time 
      print("*" + " " * (n-2) + "*")
      
