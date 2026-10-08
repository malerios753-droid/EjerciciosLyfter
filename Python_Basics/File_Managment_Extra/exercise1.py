
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()



def join_lines(lines):
    cleaned_words = [line.strip() for line in lines if line.strip()]
    return " ".join(cleaned_words)


def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    input_file = input("Nombre del archivo de entrada: ")
    output_file = input("Nombre del archivo de salida: ")

    lines = read_file(input_file)
    single_line_text = join_lines(lines)
    write_file(output_file, single_line_text)

    print(f"\n¡Listo! Contenido unido en '{output_file}'.")


if __name__ == "__main__":
    main()