def conver_to_integer(elements):
    print("Resultado:")
    for element in elements:
        try:
            integer = int(element)
            print(f'"{element}" convertido a {integer}')
        except ValueError:
            print(f"No se pudo convertir el elemento: {element}")


my_list = ["4", "hola", "10", "5.6"]
conver_to_integer(my_list)