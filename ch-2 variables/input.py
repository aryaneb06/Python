a=input("Enter number 1 is :")
# a=int(input("Enter number 1 is :"))
b=input("Enter number 2 is :")
b=int(input("Enter number 2 is :"))

print( "number 1 is ", a)
print("number 2 is " ,b)
# when u sum these number1 and number2 then it concatinate them like number 1=5 , number 2=6 then it shows as sum=56( in editor)
# but u expected that it shows sum as 11 but it does not like that because a and b take input as a string thats why it concatinates the both string
# so perform sum using input method first of all u have to convert the input into int(using typecasting ) . ok ,alright.
print("sum is", a+b ) 