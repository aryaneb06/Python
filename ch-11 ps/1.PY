class tdv():  #2d vector
    def __init__(self,i,j):
        self.i =i
        self.j=j

    def show(self):
            print(f"2 d vecor is : {self.i}i + {self.j}j")

class thdv(tdv): #3d vector child class
    def __init__(self,i,j,k):
        super().__init__(i,j) #which means it inherites all the attributes from parent class(tdv) which means we dont need to write t
                              #     self.   #   self.j=j
        self.k =k
      
     
    def show(self):
            print(f"2 d vecor is : {self.i}i + {self.j}j + {self.k}k")

a=tdv(1,2)
a.show()
b=thdv(2,4,5)
b.show()