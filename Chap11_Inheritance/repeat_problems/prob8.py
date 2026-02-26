#Overwrite the  __len__ method on vector problem of 5 to display the dimension of vector    

class Vector():
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
a = Vector([1,2,3,4])
print(len(a))