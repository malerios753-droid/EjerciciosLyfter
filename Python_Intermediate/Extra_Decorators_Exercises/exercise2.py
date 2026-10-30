user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise PermissionError("Usuario no autenticado")

        return func(*args, **kwargs)

    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


# --- PRUEBA DEL EJERCICIO 2 ---

# Prueba 1: Con user_logged_in = False
try:
    view_profile()
except PermissionError as e:
    print(f"[!] Excepción capturada: {e}")

# Prueba 2: Cambiamos a True y volvemos a intentar
print("\n--- Iniciando sesión ---")
user_logged_in = True
view_profile()