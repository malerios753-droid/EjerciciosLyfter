class Rectangle:
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Existe un valor negativo, los valores deben ser positivos.")
        self.width = width
        self.height = height
    
    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)


try:
    height = float(input("Ingrese la altura: "))
    width = float(input("Ingrese el ancho: "))

    rectangle = Rectangle(width, height)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
except ValueError as e:
    print(e)
    