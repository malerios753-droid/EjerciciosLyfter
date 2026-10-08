import csv


def collect_videogames_data():
    games_list = []
    print("--- REGISTRO DE VIDEOJUEGOS (SEPARADO POR TABULACIONES) ---")

    while True:
        nombre = input("\nNombre del videojuego: ")
        genero = input("Género: ")
        desarrollador = input("Desarrollador: ")
        clasificacion = input("Clasificación ESRB: ")

        game = {
            "nombre": nombre,
            "genero": genero,
            "desarrollador": desarrollador,
            "clasificacion": clasificacion,
        }

        games_list.append(game)

        continuar = (
            input("\n¿Deseas agregar otro videojuego? (s/n): ").strip().lower()
        )
        if continuar in ["n", "no"]:
            break

    return games_list


def save_to_tsv(file_path, data):
    if not data:
        print("No hay información para guardar.")
        return

    headers = data[0].keys()

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")

        writer.writeheader()
        writer.writerows(data)


def main():
    output_file = input(
        "Ingresa el nombre del archivo de salida (ej. videojuegos.tsv): "
    )

    videogames = collect_videogames_data()
    save_to_tsv(output_file, videogames)

    print(
        f"\n¡Éxito! Archivo guardado con delimitador de tabulación en '{output_file}'."
    )


if __name__ == "__main__":
    main()