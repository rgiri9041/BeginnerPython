#WAP to create a class Complex  to represent complex number along with overloaded operators "+" and "*"
# which add and multiply them

class Complex:
    def __init__(self, i, r):
        self. i = i
        self.r = r
    
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    def __str__(self):
        return f"{self.r}r + {self.i}i"

c1 = Complex(1,20)
c2 = Complex(2,3)
print(c1+c2)