def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


# --- FUNCIÓN DE PRUEBA ---

@repeat_twice
def say_hello(name):
    print(f"Hola, {name}")


# --- PRUEBA DEL EJERCICIO 1 ---
say_hello("Jeanca")