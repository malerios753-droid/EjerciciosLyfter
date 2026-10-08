def count_upper_and_lower_letters(text):
    uppercase = 0
    lowercase = 0

    for character in text:
        if character.isupper():
            uppercase += 1
        elif character.islower():
            lowercase += 1

    print(f"Mayusculas: {uppercase}")
    print(f"Minusculas: {lowercase}")


phrase = "Me Encanta La Naturaleza"
count_upper_and_lower_letters(phrase)