# #prime or not
# n=int(input("enter a number"))
# cnt=0
# for i in range(1,n+1 ):
#     if(n%i == 0):
#         cnt +=1
    
# if(cnt>2):

#      print("not prime")
# else:
#   print("prime")


n=int(input("enter a number"))
 
for i in range(2,n):
    if(n%i == 0):
        print("not prime")
        break
else:
    print("prime")
