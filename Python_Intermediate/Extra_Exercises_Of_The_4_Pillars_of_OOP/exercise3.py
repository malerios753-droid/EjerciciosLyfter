class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        """devuelve la informacion general del vehiculo."""
        return f"{self._brand} ({self._year})"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - {self.doors} puertas"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Tipo: {self.bike_type}"


print("\n=== Prueba Ejercicio Extra 3 ===")
vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())
print(vehicle2.get_info())

