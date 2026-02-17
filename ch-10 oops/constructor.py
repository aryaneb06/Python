class emp:
    lang="Py"
    sala="1200000"

    def __init__(self ,name,sala,lang):  #here we define constructor it is self called at the time of object creation
        self.name=name
        self.lang=lang
        self.sala =sala
        print("i am creating a constructor")

aryan=emp("Aryan" , 1333333,"english")
print(aryan.lang ,aryan.sala) #now it returns (english ,1333333)