import json


def calculate_average_level_by_type(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

            type_data = {}

           
            for pokemon in pokemons:
                p_type = pokemon["type"].strip().capitalize()
                level = pokemon["level"]

                
                if p_type not in type_data:
                    type_data[p_type] = {"total_level": 0, "count": 0}

                
                type_data[p_type]["total_level"] += level
                type_data[p_type]["count"] += 1

            
            print("\n--- PROMEDIO DE NIVEL POR TIPO ---")
            for p_type, data in type_data.items():
                average = data["total_level"] / data["count"]
                print(f"Tipo: {p_type} → Promedio de nivel: {average:.1f}")

    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")


def main():
    calculate_average_level_by_type("pokemons.json")


if __name__ == "__main__":
    main()
    

