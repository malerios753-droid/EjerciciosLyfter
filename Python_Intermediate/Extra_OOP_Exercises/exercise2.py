class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Hace un sonido"

class Dog(Animal):
    def speak(self) -> str:
        return "Guau"

class Cat(Animal):
    def speak(self) -> str:
        return "Miau"


dog = Dog("Firulais")
print(dog.speak())

cat = Cat("Garfield")
print(cat.speak())

   
