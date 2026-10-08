print("CALCULADORA DE NOTAS")
total_de_notas = int(input("Ingrese la cantidad de notas: "))
contador_de_nota = 1
cantidad_aprobadas = 0
cantidad_desaprobadas = 0

suma_aprobadas = 0
suma_desaprobadas = 0
suma_total = 0

while contador_de_nota <= total_de_notas:
    nota_actual = float(input(f"Ingrese la nota número {contador_de_nota}: "))
    
    suma_total = suma_total + nota_actual
    
    if nota_actual >= 70:
        cantidad_aprobadas = cantidad_aprobadas + 1
        suma_aprobadas = suma_aprobadas + nota_actual
    else:
        cantidad_desaprobadas = cantidad_desaprobadas + 1
        suma_desaprobadas = suma_desaprobadas + nota_actual
        
    contador_de_nota = contador_de_nota + 1


promedio_total = suma_total / total_de_notas

if cantidad_aprobadas > 0:
    promedio_aprobadas = suma_aprobadas / cantidad_aprobadas
else:
    promedio_aprobadas = 0

if cantidad_desaprobadas > 0:
    promedio_desaprobadas = suma_desaprobadas / cantidad_desaprobadas
else:
    promedio_desaprobadas = 0

print("\n--- RESULTADOS ---")
print(f"Notas aprobadas (>= 70): {cantidad_aprobadas}")
print(f"Promedio de notas aprobadas: {promedio_aprobadas:.2f}")

print(f"Notas desaprobadas (< 70): {cantidad_desaprobadas}")
print(f"Promedio de notas desaprobadas: {promedio_desaprobadas:.2f}")

print(f"Promedio total de todas las notas: {promedio_total:.2f}")