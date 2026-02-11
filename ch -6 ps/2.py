m1=int(input("enter marks"))
m2=int(input("enter marks"))
m3=int(input("enter marks"))
tp=(m1+m2+m3)/3
print(tp)
if(tp>40 and m1 >= 33 and m2 >= 33 and m3 >= 33  ):
    print("pass")

else:
    print("fail")