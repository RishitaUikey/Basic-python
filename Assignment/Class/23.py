'''Write a Python class named Circle constructed from a radius and two methods that will 
compute the area and the perimeter of a circle.'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print("Area of the circle:", circle.compute_area())
print("Perimeter of the circle:", circle.compute_perimeter())
