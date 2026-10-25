from data.students import students

# Q15 - Filter students by track
def filter_by_track(students, track):
    return [
        student for student in students
        if student["track"] == track
    ]


print("Q15 - AI students:")
print(filter_by_track(students, "AI"))

print("\nQ15 - Data students:")
print(filter_by_track(students, "Data"))


# Q16 - Calculate one student's average score
def average_score(student):
    scores = student["scores"]
    return sum(scores) / len(scores)


print("\nQ16 - Lara's average score:")
print(round(average_score(students[0]), 1))


# Q17 - Find student with highest average score
def top_student(students):
    best_student = max(students, key=average_score)
    return best_student["name"]


print("\nQ17 - Top student:")
print(top_student(students))


# Q18 - Generate a cohort summary
def summary(students):
    return {
        "total_students": len(students),
        "average_age": sum(
            student["age"] for student in students
        ) / len(students),
        "tracks": {student["track"] for student in students}
    }


print("\nQ18 - Cohort summary:")
print(summary(students))