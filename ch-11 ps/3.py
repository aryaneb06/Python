class emp():
    def __init__(self ,sal ,inc):
        self.sal = sal
        self.inc = inc
        # print(f"salary after increment: {self.sal + self.sal * (self.inc / 100)}")  #using after increment

    @property
    def salafterinc(self):
        return (self.sal + self.sal*(self.inc/100))

    
        

a=emp(10000 ,25)

print(a.salafterinc)
      