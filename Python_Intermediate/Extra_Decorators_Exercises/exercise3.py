from datetime import datetime

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(f"[!] Error: El argumento '{arg}' no es un número.")

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"[!] Error: El argumento '{key}={value}' no es un número.")

        return func(*args, **kwargs)

    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(str(a) for a in args)
        now = datetime.now()
        print(f"func:{func.__name__} - args: {args_str} - [{now}] - Resultado: {result}")

        return result

    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b


# --- PRUEBA DEL EJERCICIO 3 ---

print("=== Prueba Ejercicio Extra 3 ===")
resultado = multiply(3, 4)
print(f"Resultado {resultado}")
        
