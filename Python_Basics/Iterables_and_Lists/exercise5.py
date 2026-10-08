numbers = []

for i in range(10):
    num = int(input(f"Ingresa el numero {i + 1}: "))
    numbers.append(num)

top_number = max(numbers)
print(f"{numbers}. El mas alto fue {top_number}.")