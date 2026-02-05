#WAP to create a class Calculator which is capable of finding square, cube and squareroot of a number.

class Calculator:

    def __init__(self, number):
        self.number = number
    
    def square(self):
        print(f"The square of {self.number} is {self.number *self.number}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number * self.number * self.number}")
    
    def squareroot(self):
        print(f"The square root of {self.number} is {self.number **0.5}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()