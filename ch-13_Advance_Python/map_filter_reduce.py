from functools import reduce # u have to import this for reduce function
# ls=[1,3,4,5,7]

# sq=lambda x:x*x

#map function
# sqlist=map(sq,ls) 
# print(list(sqlist))

#filter  -- it select values from true and falses u have to give the condition

# def even(n):
#     if(n%2 == 0):
#         return True
#     return False

# newls=filter(even,ls)   # {either u can write this whole filter code like -ls = [1, 3, 4, 5, 7]

#                              # even = list(filter(lambda x: x % 2 == 0, ls)) -- direct define the function
#                              # print(even)      }

# print(list(newls))  #return [4]


#reduce
ls=[1,3,4,5,7]
sum=lambda a,b :a+b
print(reduce(sum,ls))