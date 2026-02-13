#WAP to create a 2-D vector class and use it to create a another class representing 3_D vector 

class TwoDVector:
    def __init__(self, i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vectore is {self.i}i and {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, k):
        super().__init__   # it directly brings the all property or functionality of TwoDVector
        self.k = k
    def show(self):
        print(f"the vectore are {self.i}i, {self.j}j and {self.k}k")

a = TwoDVector(1,2)
a.show()
b = ThreeDVector(10,20,30)

b.show()


