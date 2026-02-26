#Write a __str__ method to print the follows
# 3i + 4j+ 6k

class Vector:
    def __init__(self, i, j ,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        result = Vector(self.i+other.i, self.j+other.j, self.k+other.k)
        return result

    def __str__(self):
        return f"{self.j}j, {self.k}k, {self.i}i"
    
a =Vector(1,2,3)
b = Vector(2,3,4)

print(a+b)