def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def to_uppercase(lines):
    return [line.upper() for line in lines]

def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def main():
    input_file = input("Archivo de entrada: ")
    output_file = input("Archivo de salida en mayúsculas: ")

    lines = read_file(input_file)
    upper_lines = to_uppercase(lines)
    write_file(output_file, upper_lines)
    print("¡Archivo en mayúsculas creado exitosamente!")

if __name__ == "__main__":
    main()