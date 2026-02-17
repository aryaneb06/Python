class emp:
    lang="py"
    sal="122222" 

    def getinfo(self):  #u have to pass "self " as a parameter whether u use it or not
                        # here we can use anything as a parameter at "self" place like--(slf,aryan)
                        # but we use self so code looks good and improve readability

        print(f"language is : {self.lang}. The salary is : {self.sal} ")


aryan=emp()
aryan.getinfo() 
emp.getinfo(aryan) # this is another method of calling function method

