def long_word_filter(word_list, n):
    word_filter = []

    for word in word_list:
        if len(word) > n:
            word_filter.append(word)

    return word_filter


words = ["cielo", "sol", "maravilloso", "dia"]
minimum_letters = 4

result = long_word_filter(words, minimum_letters)
print(result)