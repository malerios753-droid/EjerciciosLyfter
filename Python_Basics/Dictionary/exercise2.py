list_1 = ["first_name", "last_name", "subject"]
list_2 = ["Alejandra", "Rios", "English"]

student_dictionary = {}

for index in range(len(list_1)):
    key = list_1[index]
    value = list_2[index]
    student_dictionary[key] = value


print(student_dictionary)

