# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. Implement 
# subclasses for different shapes like circle, triangle, and square.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

square = Square(4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())
