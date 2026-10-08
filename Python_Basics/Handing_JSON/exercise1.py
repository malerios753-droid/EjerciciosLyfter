import json



def load_pokemons(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



def collect_pokemon_data():
    print("--- REGISTRO DE NUEVO PÓKEMON ---")
    name = input("Nombre: ")
    p_type = input("Tipo principal: ")
    level = int(input("Nivel: "))
    weight_kg = float(input("Peso (kg): "))

    shiny_input = input("¿Es Shiny? (s/n): ").strip().lower()
    is_shiny = shiny_input in ["s", "si", "sí", "y", "yes"]

    held_item = input("Objeto equipado (deja vacío si no tiene): ").strip()
    if not held_item:
        held_item = None

    skills_raw = input("Habilidades (separadas por coma): ")
    skills = [s.strip() for s in skills_raw.split(",")]

    print("\n-- Estadísticas Base --")
    hp = int(input("HP: "))
    attack = int(input("Ataque: "))
    defense = int(input("Defensa: "))
    sp_attack = int(input("Ataque Especial: "))
    sp_defense = int(input("Defensa Especial: "))
    speed = int(input("Velocidad: "))

    new_pokemon = {
        "name": name,
        "type": p_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed,
        },
    }

    return new_pokemon



def save_pokemons(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def main():
    file_path = "pokemons.json"

    pokemons = load_pokemons(file_path)
    print(f"Se cargaron {len(pokemons)} Pokémon del archivo.")

    new_pkmn = collect_pokemon_data()
    pokemons.append(new_pkmn)

    save_pokemons(file_path, pokemons)

    print(f"\n¡Éxito! '{new_pkmn['name']}' fue agregado a '{file_path}'.")


if __name__ == "__main__":
    main()