
class calc():

    def __init__(self,n):
        self.n=n  #pass a number 

    def sq(self):
            print(f"square is : {self.n * self.n}")
        

    def cb(self):
            print(f"cube is : {self.n * self.n * self.n}")
        

    def sqr(self):
            print(f"square root is : {self.n ** 0.5}") #in python we define the square by "**"
        
    
    @staticmethod  #this is static method
    def hello():
      print("hello brother, good morning")




a=calc(16)
a.sq()
a.sqr()
a.cb() 
a.hello()