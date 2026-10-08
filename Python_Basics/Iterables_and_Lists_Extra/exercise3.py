my_list = [4, 5, 2, 10, 7, 8]
smallest = my_list[0]

for number in my_list:
    if number < smallest:
        smallest = number

print(f"El menor valor es {smallest}")