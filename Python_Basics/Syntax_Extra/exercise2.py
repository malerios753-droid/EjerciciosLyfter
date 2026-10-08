segundos_meta = 600
segundos_ingresado = int(input("Ingrese el tiempo en segundos: "))
if segundos_ingresado > segundos_meta:
    print("Mayor")
elif segundos_ingresado == segundos_meta:
    print("Igual")
else:
    faltante = segundos_meta - segundos_ingresado
    print(f"Fatltan segundos: {faltante}")
    