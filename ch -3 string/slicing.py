a="Aryan"
# slicing means break the string and 
# it starts from 0 to n-1  

print(a[1:4]) # it will consider form 0 to excluding 4 which means till 3
print(a[1:]) # "ryan"
print(a[:]) # "Aryan"
print(a[:4]) # "Arya"

# now negartive slicing
print(a[-4:-1]) # it same as print(a[1:4]) -- short trick
print(a[-5:]) #it same as print(a[:5])
print(a[4:])

#now skiping the value
c="abcdefghijklmnopqrstuvwxyz"
print(c[0:9:3]) # Here 0 to 9 means 'abcdefgh' and 3 means jump with 3 alphabets
