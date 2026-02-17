# f=open("file.txt" ,"r")
# data = f.read()
# print(data)
# f.close()
 
#with the help of "with "  we dont need to write again and again close command
#same above thing we can write it like this 

with open("file.txt") as f :
    print(f.read())