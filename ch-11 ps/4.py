class com():
    def __init__(self ,r,i):  #this is cons for pass parameter
        self.r=r 
        self.i=i

    def __add__(self,c2):    #this oprator overload of add
        return com(self.r + c2.r ,self.i + c2.i)
    
    def __mul__(self, c2):   #this oprator overload of add
        return com(self.r * c2.r - self.i * c2.i,
               self.r * c2.i + self.i * c2.r)
     
    def __str__(self):       #this is used for convert com number in 5+6i type
        return f"{self.r} + {self.i}i"
    

c1=com(2,3)
c2=com(4,5)
print(c1+c2)
print(c1*c2)
