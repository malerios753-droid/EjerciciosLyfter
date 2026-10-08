my_list = [100, 200, 300, 400, 500, 600]
total_sum = sum(my_list)
total_elem = len(my_list)

average = total_sum / total_elem

above_average = []

for number in my_list:
    if number > average:
        above_average.append(number)

print(f"promedio: {int(average)}")
print(f"nueva lista: {above_average}")