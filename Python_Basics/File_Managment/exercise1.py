def read_songs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def sort_songs(songs):
    cleaned_songs = [song.strip() for song in songs if song.strip()]
    cleaned_songs.sort()
    return cleaned_songs


def write_songs(file_path, sorted_songs):
    with open(file_path, 'w', encoding='utf-8') as file:
        for song in sorted_songs:
            file.write(f"{song}\n")


def main():
   
    input_file = input("Ingresa el nombre del archivo de entrada (ej. canciones.txt): ")
    output_file = input("Ingresa el nombre para el archivo de salida (ej. canciones_ordenadas.txt): ")


    songs_list = read_songs(input_file)
    sorted_list = sort_songs(songs_list)
    write_songs(output_file, sorted_list)

    print(f"\n¡Listo! Las canciones han sido ordenadas y guardadas en '{output_file}'.")



if __name__ == "__main__":
    main()