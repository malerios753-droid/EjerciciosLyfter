import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


my_circle = Circle(5)
print(f"Radio: {my_circle.radius}")
print(f"Área: {my_circle.get_area():.2f}")