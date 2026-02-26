#Create a class 2D vector and use it to create a another 3DVectors 

class TwoDVector():
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The TwoDVecotr are: {self.i}i, {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(j,k)
        self.k = k
    
    def show(self):
        print(f"The ThreeDVector is {self.j}j, {self.k}k, {self.i}i")

a = TwoDVector(1,2)
a.show()
b = ThreeDVector(1,2,3)
b.show()
    