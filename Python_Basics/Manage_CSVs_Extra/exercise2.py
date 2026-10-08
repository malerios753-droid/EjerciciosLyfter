import csv


def count_games_by_genre(file_path):
    genre_counts = {}

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  

        
        for row in reader:
            if row and len(row) >= 2:
                genre = row[1].strip()
                genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def main():
    input_file = input("Archivo CSV de entrada: ")
    counts = count_games_by_genre(input_file)

    print("\nGéneros encontrados:")
    for genre, total in sorted(counts.items()):
        print(f"{genre}: {total}")


if __name__ == "__main__":
    main()
 