my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_pairs = []

for num in my_list:
    if num % 2 == 0:
        list_of_pairs.append(num)

print(list_of_pairs)