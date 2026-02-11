p1="make a lot money"
p2="click this"
p3="buy now"
c=input("enter comment")

if((p1 in c ) or (p2 in c) or (p3 in c)):
    print("spam comment")

else:
    print("not spam")