class lenth():
    def __init__(self , l): #pass list
        self.l=l

    def __len__(self):   #this define the lenth function
     return len(self.l)
l=lenth([1,3,4])
print(len(l))
