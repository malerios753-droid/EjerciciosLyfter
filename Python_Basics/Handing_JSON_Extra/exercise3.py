import json


def display_stats(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

            print("--- ESTADISTICAS PRINCIPALES ---")


            for pokemon in pokemons:
                print(f"Nombre: {pokemon['name']}")

                stats = pokemon.get("stats", {})


                print(f"Ataque: {stats.get('attack', 'N/A')}")
                print(f"Defensa: {stats.get('defense', 'N/A')}")
                print(f"Velocidad: {stats.get('speed', 'N/A')}")
                print("-" * 25)


    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")


def main():
    display_stats("pokemons.json")

if __name__ == "__main__":
    main()
