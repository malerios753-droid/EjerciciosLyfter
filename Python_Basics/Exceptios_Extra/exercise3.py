def sum_values(input_list):
    total_sum = 0.0

    for element in input_list:
        try:
            float_value = float(element)
            total_sum += float_value
            print(f"{float_value} sumado correctamente")
        except ValueError:
            print(f"Elemento inválido: {element}")

    print(f"Total de la suma: {total_sum}")


my_list = ["10", "manzana", "5.5", "3", "n/a"]
sum_values(my_list)
    