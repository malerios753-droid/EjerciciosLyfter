import csv


def filter_by_developer(file_path, target_dev):

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  

        found = False
        print(f"\nVideojuegos desarrollados por {target_dev}:")

        for row in reader:
           
            if row and len(row) >= 3 and row[2].strip().lower() == target_dev.lower():
                
                classification = row[3] if len(row) >= 4 else "N/A"
                genre = row[1] if len(row) >= 2 else "N/A"
                print(f"- {row[0]} (Clasificación: {classification}, Género: {genre})")
                found = True

        if not found:
            print("No se encontraron videojuegos para ese desarrollador.")


def main():
    input_file = input("Archivo CSV de entrada: ")
    developer = input("Ingresa el nombre del desarrollador (ej. Ubisoft): ")
    filter_by_developer(input_file, developer)


if __name__ == "__main__":
    main()