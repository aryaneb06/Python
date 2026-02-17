# class emp():
#     comp="Microsoft"
#     lang="PY"
#     sala="2200000"

# rohan=emp()
# rohan.name="ROhan"
# print(rohan.comp,rohan.sala ,rohan.name)
# rohan=emp()

# using  constructor

class emp():

    def __init__(self,name,sala,comp):
        self.name=name
        self.sala=sala
        self.comp=comp
        print("This is my working company")

p=emp("Aryan" , 120000 , "Microsoft")

print(p.name,p.sala,p.comp)