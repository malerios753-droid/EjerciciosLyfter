import csv


def filter_by_esrb(file_path, target_rating):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None) 

        found = False
        print(f"\nVideojuegos con clasificación '{target_rating.upper()}':")

        for row in reader:
            
            if row and len(row) >= 4 and row[3].strip().upper() == target_rating.upper():
                print(f"- {row[0]} ({row[1]} por {row[2]})")
                found = True

        if not found:
            print("No se encontraron videojuegos con esa clasificación.")


def main():
    input_file = input("Archivo CSV de entrada: ")
    rating = input("Ingresa la clasificación ESRB a buscar (ej. T, M, E): ")
    filter_by_esrb(input_file, rating)


if __name__ == "__main__":
    main()