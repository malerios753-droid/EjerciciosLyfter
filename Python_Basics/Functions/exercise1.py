def function_two():
    print("Hola desde la segunda funcion")


def function_one():
    print("Ejecutando la primera fucion...")
    function_two()


function_one()