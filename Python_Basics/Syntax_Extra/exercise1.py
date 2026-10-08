precio_del_producto = float(input("Ingrese el precio del producto: "))

if precio_del_producto < 100:
   descuento = precio_del_producto * 0.02
else:
    descuento = precio_del_producto * 0.10

precio_final = precio_del_producto - descuento

print(f"El precio final es: {precio_final}")