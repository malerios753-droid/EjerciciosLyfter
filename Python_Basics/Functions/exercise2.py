def confidential():
    secret_message = "Soy una variable local"
    print("Dentro de la funcion:", secret_message)


confidential()
#print(secret_message) con esta me marca error



x = 10 


def fun():
    global x 
    x = 20


print("Valor inicial de x:", x)
fun()
print("Valor final de x:", x)