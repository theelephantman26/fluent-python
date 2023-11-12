from math import hypot

class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __abs__(self) -> int:
        return hypot(self.x, self.y)

    def __add__(self, vec2):
        return Vector2D(self.x + vec2.x, self.y + vec2.y)
    
    def __repr__(self):
        return "Vector (%r, %r) " % (self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __mul__(self, scalar):
        return Vector2D(scalar * self.x, scalar * self.y)
    
def printVector(v: Vector2D):
    print("This is a vector : %r \n" % v)
# create two vector
v1 = Vector2D(3, 4)
v2 = Vector2D(10, 1)

# print both vectors
printVector(v1)
printVector(v2)

# add two vectors to get a new vector
v3 = v1 + v2
printVector(v3)

# scale the vector by 2
v4 = v3 * 2
printVector(v4)

# what is the length of the vector
print(abs(v1), abs(v2), abs(v3), abs(v4))