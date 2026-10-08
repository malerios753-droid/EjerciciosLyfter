my_list =[1, 3, -5, -3, 6, 7, -9, 5, -1 , 3 , 4 , 5, 6 , 78, -6]
all_positive = True

for number in my_list:
    if number <= 0:
        all_positive = False
        break

if all_positive:
    print("Todos los numeros son positivos")
else:
    print("Hay al menos un numero negativo o cero")