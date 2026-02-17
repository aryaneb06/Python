# def table(i):
#     if(i==11):
#         return 
#     else:
#         print(m*i)
#         table(i+1)
    
# m=int(input("enter a number :"))
# i=1
# table(i)

def table(n):
    for i in range(1,11):
        print(f"{n}X{i}  =  {n*i} ")
table(5)