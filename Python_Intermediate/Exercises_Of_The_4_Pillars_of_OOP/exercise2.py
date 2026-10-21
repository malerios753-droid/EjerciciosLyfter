import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Metodo abstracto: no tiene codigo aqui, obliga a las clases hijas a definirlo."""
        pass 

    @abstractmethod
    def calculate_perimeter(self):
        """Metodo abstracto obligatorio para calcular el perimetro. """
        pass 

class Circle(Shape):
    def __init__(self, radius):
            self.radius = float(radius)

    def calculate_area(self):
            return math.pi * (self.radius)

    def calculate_perimeter(self):
            return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
          self.side = float(side)

    def calculate_area(self):
          return self.side ** 2

    def calculate_perimeter(self):
          return 4 * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
          self.width = float(width)
          self.height = float(height)

    def calculate_area(self):
          return self.width * self.height

    def calculate_perimeter(self):
          return 2 * (self.width + self.height)




print("\n=== Prueba Ejercicio 2 ===")

shapes = [
      Circle(radius=5),
      Square(side=4),
      Rectangle(width=3, height=6)
]

for s in shapes:
      print(f"Figura: {s.__class__.__name__}")
      print(f"  Área: {s.calculate_area():.2f}")
      print(f"  Perímetro: {s.calculate_perimeter():.2f}")
      print("-" * 30)
            
          



        
        
