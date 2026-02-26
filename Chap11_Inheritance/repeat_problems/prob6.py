#Write a class vector representing a vector of n dimension . overload the + and * operator and calculate  the sum and dot(.) product of them

class Vector():
    def __init__(self, i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        result = Vector(self.i+ other.i, self.j+other.j, self.k+other.k)
        return result
    
    def __mul__(self, other):
        result =  self.i*other.i + self.j*other.j + self.k*other.k
        return result
    
    def __str__(self):
        return f"Vector {self.i}, {self.j}, {self.k}"

a = Vector(1,2,3)
b = Vector(2,3,4)
c = Vector(3,4,5)
print(a+b)
print(a*b)
print(a+c)
print(a*c)