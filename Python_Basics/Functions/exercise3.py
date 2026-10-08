def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum



my_list = [7,9,8,2,10]
result = sum_list(my_list)
print("La suma total es:", result)