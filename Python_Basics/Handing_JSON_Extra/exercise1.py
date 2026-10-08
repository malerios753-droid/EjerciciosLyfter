import json


def list_all_pokemons(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

            print("---- LISTADO COMPLETO DE POKEMONS ---")
            for pokemon in pokemons:
                print(f"Nombre: {pokemon['name']}")
                print(f"Tipo: {pokemon['type']}")
                print(f"Nivel: {pokemon['level']}")
                print("-" * 25)

    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")


def main():
    list_all_pokemons("pokemons.json")


if __name__ == "__main__":
    main()

