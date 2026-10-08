def append_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

def main():
    target_file = input("Nombre del archivo donde agregarás texto: ")
    user_text = input("Escribe la línea que deseas agregar: ")

    append_to_file(target_file, user_text)
    print(f"Texto agregado correctamente a '{target_file}'.")

if __name__ == "__main__":
    main()