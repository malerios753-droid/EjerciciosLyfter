class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"[✓] {person.name} subio al autobus.")
        else:
            print(f"[!] El autobus esta lleno. {person.name} no puede subir.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"[✓] {person.name} bajo del autobus.")
        else:
            print(f"[!] {person.name} no esta en el autobus.")



p1 = Person("Diego")
p2 = Person("Alejandro")
p3 = Person("Maria")
p4 = Person("Alejandra")

my_bus = Bus(max_passengers=3)

my_bus.add_passengers(p1)
my_bus.add_passengers(p2)
my_bus.add_passengers(p3)
my_bus.add_passengers(p4)

my_bus.remove_passenger(p1)
my_bus.add_passengers(p4)