contador = 1
suma = 0
numero_limite = int(input("Ingrese numero: "))

while contador <= numero_limite:
    suma = suma + contador
    contador = contador + 1
else:
    print(f"La suma total es: {suma}")