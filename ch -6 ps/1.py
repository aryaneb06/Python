ls=[] #u can do it simply but i tried little bit different using list and u can watch it from harry
nu=int(input("enter the num"))
ls.append(nu)

nu=int(input("enter the num"))
ls.append(nu)
nu=int(input("enter the num"))
ls.append(nu)
nu=int(input("enter the num"))
ls.append(nu)

if(ls[0] > ls[1]  and ls[0] > ls[2] and ls[0] > ls[3]):
    print(ls[0])

elif(ls[1] > ls[2]  and ls[1] > ls[0] and ls[1] > ls[3]):
    print(ls[1])

elif(ls[2] > ls[1]  and ls[2] > ls[0] and ls[2] > ls[3]):
    print(ls[2])

elif(ls[3] > ls[1]  and ls[3] > ls[0] and ls[3] > ls[2]):
    print(ls[3])