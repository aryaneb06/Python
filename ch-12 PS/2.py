l=[2,3,4,7,8,5,9,0,6,7]
# i=0   using for loop
# nl=[]
# for item in l:
#     if(i==2 or i==4 or i==6):
#      nl.append(item)
#     i+=1
# print(nl)


for i,item in enumerate(l):
    if i==2 or  i==4 or i==6:
        print(item)