def validate_only_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(f"[!] Error: El parametro '{arg}' de tipo {type(arg).__name__} NO es un numero valido.")

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"[!] Error: El parametro '{key}={value}' No es un numero valido. ")

        return func(*args, **kwargs)

    return wrapper


# --- PRUEBA DEL EJERCICIO 2 ---

@validate_only_numbers
def multiply(a, b):
    return a * b

print("Resultado multiplicación:", multiply(4, 5))