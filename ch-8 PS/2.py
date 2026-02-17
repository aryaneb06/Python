def f_to_c(f):
    return 5*(f-32)/9

f=int(input("Enter temp in F :"))

# print("Temp in C : " ,f_to_c(f)) #readability of this code is not good so we can change it little bit just see
c=f_to_c(f)
print(f"{round(c,2)} in ° c") #here round fun means it round of decimal value till 2 like - 17.9989 == 17.99 
    