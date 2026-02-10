a=(1,4,6,"aryan" ,'b' , 6)
print(type(a))  #tuple are immutable which means u cant change tuples
# a[1] = 7 
# print(a) # this shows error because tuples are immutable and u are trying to change it

# no=a.index("aryan") # 3 -- it gives the index value of element
# print(a.count(6))   # 2-- it counts the total frequency of a particular element(which we pass)

# print(no)

print(a[0])  # accesing the tuple element - 1
print(a[-1])  # accesing the tuple element - 6

#create a single element tuple
b=(1) # it is not a single element tuple its an integer data type
b=(1,) # this is the correct way to declare an element
print(type(b))

#slicing
print(a[1:5])