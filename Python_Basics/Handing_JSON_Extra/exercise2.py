import json


def filter_by_type(file_path, target_type):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

            found = False
            print(f"\nLos Pokémon que existen del tipo '{target_type}' son:")

            
            for pokemon in pokemons:
                if pokemon["type"].strip().lower() == target_type.strip().lower():
                    print(f"- {pokemon['name']}")
                    found = True  

            
            if not found:
                print("No se encontraron Pokémon de ese tipo.")

    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")



def main():
    search_type = input(
        "Ingrese el tipo de Pokémon que desea buscar (Agua, Electric, Fire, Grass, etc.): "
    )
    filter_by_type("pokemons.json", search_type)


if __name__ == "__main__":
    main()