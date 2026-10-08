import csv


def read_and_display_games(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)


        next(reader, None)

        print("--- LISTADO DE VIDEOJUEGOS ---")
        for row in reader:
            if row and len(row) >= 4:
                print(f"Nombre: {row[0]}")
                print(f"Genero: {row[1]}")
                print(f"Desarrollador: {row[2]}")
                print(f"Clasificación: {row[3]}")
                print("-" * 25)



def main():
    input_file = input(
        "Ingresa el nombre del archivo CSV (ej. videojuegos.csv): "
    )
    read_and_display_games(input_file)


if __name__ == "__main__":
    main()