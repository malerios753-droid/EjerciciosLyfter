def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    return len(text.split())

def main():
    input_file = input("Archivo a contar palabras: ")
    content = read_file(input_file)
    total = count_words(content)
    print(f"Este archivo contiene {total} palabras.")

if __name__ == "__main__":
    main()