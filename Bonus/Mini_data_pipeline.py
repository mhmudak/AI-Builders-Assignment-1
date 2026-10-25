from data.students import students


# Q19 - Filter, transform, and sort student results
def report(students, min_hours):

    # Step 1 - Filter
    filtered_students = [
        student for student in students
        if student["hours_studied"] >= min_hours
    ]

    # Step 2 - Transform
    results = [
        {
            "name": student["name"],
            "average_score": round(
                sum(student["scores"]) / len(student["scores"]), 1
            )
        }
        for student in filtered_students
    ]

    # Step 3 - Sort from highest to lowest score
    results.sort(
        key=lambda student: student["average_score"],
        reverse=True
    )

    return results


# Test
print("Q19 - Students with at least 30 study hours:")
print(report(students, 30))