def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowels_count = 0


    for char in text:
        if char in vowels:
            vowels_count += 1

    return vowels_count


input_text = "Hola mundo"
result = count_vowels(input_text)

print(" Texto original:", input_text)
print("Texto de vocales:", result)
        