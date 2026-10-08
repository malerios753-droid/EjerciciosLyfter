def count_characters(text, character):
    count = text.count(character)
    return count



text_input = "la evolucion es el unico camino"
charatcter_search = "o"



result = count_characters(text_input, charatcter_search)


print(f"Se ha encontrado {result} veces el caracter")