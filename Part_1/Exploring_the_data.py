from data.students import students

# Q1
print(students[0]["name"])
print(students[-1]["name"])


# Q2
for student in students:
    if student["name"] == "Rim":
        print(student["scores"])
        break

#Q3
for student in students:
    print(f'{student["name"]} is {student["age"]} years old and studies {student["track"]}')