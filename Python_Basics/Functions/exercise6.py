def sort_words(string):
    list_of_words = string.split("-")
    list_of_words.sort()
    result = "-".join(list_of_words)
    return result


original_text = "espacio-busca-Aleja-del-cosas"
organized_text = sort_words(original_text)


print("Texto original:", original_text)
print("Texto ordenado:", organized_text)