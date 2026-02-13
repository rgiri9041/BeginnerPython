#WAP to creat a class vector representing a vectore of n dimension.
#overload the + and * operators which calculate the sum and dot(.) product of them

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        return Vector(self.i + other.i,
                      self.j + other.j,
                      self.k + other.k)
    
    def __mul__(self, other):
        # dot product
        return self.i * other.i + self.j * other.j + self.k * other.k
    
    def __str__(self):
        return f"Vector({self.i}, {self.j}, {self.k})"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)   # Vector(5, 7, 9)
print(v1 * v2)   # 32
