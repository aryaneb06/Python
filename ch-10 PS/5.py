from random import randint #this is used to generate number between 2 ranges like --{1.10}
class tra():

    def __init__(self,trainNO):
        self.trainNO=trainNO

    def book(self,fro ,to):  #here "fro" and "to" are inbuilt function in python which is used for one dist to next dist
        print(f"ticket is booked in {self.trainNO} from {fro} to {to}")

    def getstatus(self):
        print(f"train is on time : {self.trainNO}")

    def fare(self,fro ,to):
        print(f"fare of train no is : {self.trainNO} from {fro} to {to} is {randint(222,555667)}")

t=tra(1233)
t.book("Jhunjhunu" , "Jaipur")
t.getstatus()
t.fare("Jhunjhunu" , "Jaipur")
