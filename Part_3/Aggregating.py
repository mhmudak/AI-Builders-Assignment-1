from data.students import students

# Q8
ages = [student["age"] for student in students]
average_age = sum(ages) / len(ages)
print(f'the age average of students is {round(average_age, 2)} years old')

# Q9
hours_studied = [student["hours_studied"] for student in students]
total_hours_studied = sum(hours_studied)
print(f'Students studied a total of {total_hours_studied} hours.')

# Q10 ~ my code
# max_studied_hours = max(hours_studied)
# student_name_most_studied = [student["name"] for student in students if student["hours_studied"] == max_studied_hours]
# print(f'{student_name_most_studied[0]} is the student who studied the most hours: {max_studied_hours} hours')

# Q10 ~ with loop
max_hours = 0
top_student = None

for student in students:
    if student["hours_studied"] > max_hours:
        max_hours = student["hours_studied"]
        top_student = student

print(f'{top_student["name"]} studied the most: {max_hours} hours')

# Q11
for student in students:
    scores = student["scores"]
    average_score = sum(scores) / len(scores)
    print(f'The final grade for {student["name"]} is {round(average_score, 1)}')