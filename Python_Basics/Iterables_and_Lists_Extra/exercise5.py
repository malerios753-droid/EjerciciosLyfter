word_list = []
filterd_word = []

print("ingrese 5 palabras: ")
for index in range(5):
    word = input(f"palanra {index + 1}:")
    word_list.append(word)

for word in word_list:
    if len(word) >4:
        filterd_word.append(word)

print(f"\n Nueva lista: {filterd_word}")