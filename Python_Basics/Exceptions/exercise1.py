def display_menu(current_number):
    """Muestra la interfaz del menú con el saldo/número actual."""
    print("\n" + "=" * 30)
    print(f" Numero actual: {current_number}")
    print("=" * 30)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado (Limpiar a 0)")
    print("6. Salir")
    print("-" * 30)


def calculate(option, current_num, new_num):
    """Aplica la operación matemática correspondiente y devuelve el nuevo número."""
    if option == "1":
        return current_num + new_num
    elif option == "2":
        return current_num - new_num
    elif option == "3":
        return current_num * new_num
    elif option == "4":
        if new_num == 0:
            raise ZeroDivisionError
        return current_num / new_num


def get_valid_number():
    """Solicita un número al usuario y valida que sea numérico (captura ValueError)."""
    while True:
        try:
            return float(input("Ingrese el numero para la operacion: "))
        except ValueError:
            print("Error: Ingresaste un valor numerico invalido. Intenta de nuevo.")


def calculator():
    """Coordinador principal del flujo del programa (Controlador)."""
    current_number = 0.0

    while True:
        display_menu(current_number)
        option = input("Seleccione una opcion (1-6): ").strip()

        if option == "6":
            print("¡Gracias por usar la calculadora! Hasta luego")
            break

        if option == "5":
            current_number = 0.0
            print("Resultado limpiado a 0.0")
            continue

        if option not in ["1", "2", "3", "4"]:
            print("Error: opcion invalida. Por favor elija un numero del menu (1-6).")
            continue

      
        new_number = get_valid_number()

        try:
            current_number = calculate(option, current_number, new_number)
            print(f"Operacion realizada con exito. Nuevo total: {current_number}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")



if __name__ == "__main__":
    calculator()