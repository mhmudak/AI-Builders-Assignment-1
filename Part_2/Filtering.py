from data.students import students

# Q4
ai_students = []

for student in students:
    if student["track"] == "AI":
        ai_students.append(student)

print(f'There are {len(ai_students)} students in the AI track')

# Q5 - List Comprehension
ai_students_comprehension = [student for student in students if student["track"] == "AI"]
print(f'List Comprehension: There are {len(ai_students_comprehension)} students in the AI track')

# Q6
students_over_30_hours = [student["name"] for student in students if student["hours_studied"] > 30]
print(students_over_30_hours)

# Q7
ai_students_over_24 = [student for student in students if student["age"] > 24 and student["track"] == "AI"]
print(ai_students_over_24)