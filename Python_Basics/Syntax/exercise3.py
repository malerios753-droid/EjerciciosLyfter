
import random
print("Adivine el número secreto del 1 al 10")
number_win = random.randint(1, 10)
number = int(input("Ingrese el número: "))

while number != number_win:
    print("Aún no adivinas")
    number = int(input("Intenta de nuevo: "))

print(f"¡Felicidades! Adivinaste el número secreto, era el {number_win}")
