list_of_keys = ["second_name", "level_els", "age"]
student = {"fisrt_name": "Maria", "second_name": "Alejandra", "last_name": "Rios", "level_els": 6, "session": "day school", "age": 25}

for key in list_of_keys:
    if key in student:
        student.pop(key)

print(student)
