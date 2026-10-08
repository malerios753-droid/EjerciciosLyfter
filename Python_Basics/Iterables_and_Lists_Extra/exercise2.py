list_of_numbers = []
total_num = int(input("¿Cuántos números va a ingresar en la lista?: "))

for index in range (total_num):
    number = int(input(f"Ingrese el numero {index + 1}: "))
    list_of_numbers.append(number)


num_to_search = int(input("\nIngrese el numero que quiere buscar: "))

counter = 0 
for number in list_of_numbers:
    if number == num_to_search:
        counter = counter + 1

print(f"\nEl numero {num_to_search} aparece {counter} veces")