def get_valid_name():
    """Solicita y valida que el nombre no sea puramente numérico."""
    name = input("Ingrese su nombre: ").strip()
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero")
    return name


def get_valid_age():
    """Solicita y convierte la edad a entero."""
    age_str = input("Ingrese su edad: ").strip()
    return int(age_str)


def request_user_data():
    """Función principal que coordina el flujo."""
  
    try:
        name = get_valid_name()
    except ValueError:
        print("El nombre no puede ser un numero")
        return

    try:
        age = get_valid_age()
    except ValueError:
        print("Numero no valido")
        return

  
    print(f"Hola {name}, su edad es {age}")


if __name__ == "__main__":
    request_user_data()