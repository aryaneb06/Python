# f=open("file.txt" ,"r")
# data = f.read()
# print(data)
# f.close()

f=open("file.txt")
lines=f.readlines() #this command read the file line by line and then store that line in list
print(lines,type(lines)) 
f.close()
# there is another command is called "readline" - which read 1 line at a time untill it will not get empty line so u read about this with the help chatgpt