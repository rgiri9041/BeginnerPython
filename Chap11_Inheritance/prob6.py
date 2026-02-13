#WAP to write __str__ method to print the following
# 7i + 8J +10k

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, next):
        return Vector(self.i + next.i,
                      self.j + next.j,
                      self.k + next.k)
    
    def __str__(self):
        return f"Vector {self.i}i + {self.j}j + {self.k}k"
    
v1 = Vector(1,2,3)
v2 = Vector(1,2,3)

print(v1+v2)