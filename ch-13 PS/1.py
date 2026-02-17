name=input("enter a number :")
marks=int(input("enter marks :"))
phno=int(input("enter phone no :"))


# print(f" name is :{name}\n marks is :{marks}\n phone no is :{phno}") #using f string

#using format function
s="name  is : {}\n marks is : {} \n  phone no is : {}".format(name,marks,phno)
print(s)