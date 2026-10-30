def log_execution(func):
    def wrapper(*args, **kwargs):

        print(f"[LOG] Ejecutar funcion: '{func.__name__}'")
        print(f"[LOG] Argumento posicionales (*args): {args}")
        print(f"[LOG] Argumentos nombrados (**kwargs): {kwargs}")

        
        result = func(*args, **kwargs)

        print(f"[LOG] Resultado devuelto: {result}")
        print("-" * 40)

        return result

    return wrapper


# -- PRUEBA DEL EJERCICIO 1 ---

@log_execution
def add_numbers(a,b, c=0):
    return a + b + c

suma1 = add_numbers(5, 10)
suma2 = add_numbers(10, 20, c=5)
    
