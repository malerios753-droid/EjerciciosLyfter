number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication table for {number}:")
for index in range (1, 11):
    result = number * index
    print(f"{number} x {index} = {result}")