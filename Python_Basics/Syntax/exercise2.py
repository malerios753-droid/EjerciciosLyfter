print("Identificador de ciclo de vida")
name = input("Ingrese su nombre:")
last_name = input("Ingrese su apellido")
age = int(input("¿Cuantos años tiene?:"))

if age < 1: 
    category = "Bebe"
    message = ("Tu viaje apenas inicia")
elif age <= 9:
    category = "Niño"
    message = ("La mejor etapa para jugar")
elif age <= 12:
    category = "Preadolescente"
    message = ("Empezaras a experimentar muchos cambios")
elif age <= 19:
    category = "Adolescente"
    message = ("Aún te queda mucho por aprender")
elif age <= 39:
    category = "Adulto joven"
    message = ("Encuentra tu pasion")
elif age <= 64:
    category = "Adulto"
    message = ("Disfruta de tu experiencia de vida")
else:
    category = "Adulto mayor"
    message = ("Seguro sabes dar buenos concejos")


print(f"{name}, {last_name}, tu etapa de vida actual es: {category}")
print(message)