m=[]
m1=int(input("Enter the marks"))
m.append(m1)
m2=int(input("Enter the marks"))
m.append(m2)
m3=int(input("Enter the marks"))
m.append(m3)
m4=int(input("Enter the marks"))
m.append(m4)
m5=int(input("Enter the marks"))
m.append(m5)
m6=int(input("Enter the marks"))
m.append(m6)

m.sort()  # if we didnt change the type of input then sort function sorts the list in alphabatical order(since input function always contain string data type 
# so that s why we change the data type from string into int  so that we can get our desired output)
print(m) 
