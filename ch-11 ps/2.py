class animals():
    pass



class pets(animals):
    pass



class dog(pets):
    @staticmethod   #static method m apn ko self ki jarurt nhi padti
    def bark():
    # def __init__(self): # u can do it as well as using  constructor
       
        print("BOw Bow")
  

d=dog()
d.bark()