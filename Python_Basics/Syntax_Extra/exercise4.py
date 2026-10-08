number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

total_sum = number1 + number2 + number3

if number1 == 30 or number2 == 30 or number3 == 30 or total_sum == 30:
    print("correcto")
else:
    print("incorrecto")