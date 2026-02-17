class demo():
    a=4


o=demo()
print(o.a) #it return 4 because object instance is not present
o.a=3
print(o.a) #it return 3 because object instance is present
print(demo.a) # after creating object instance class attribute "does not change" it still return 4