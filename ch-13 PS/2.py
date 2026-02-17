n=int(input("enter a number :"))
table=[str(n*i) for i in range(1,11)]  #insert ls using list comprehension

vertical = "\n".join(table)
print(vertical)