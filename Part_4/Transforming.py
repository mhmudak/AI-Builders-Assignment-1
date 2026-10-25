from data.students import students

# Q12 - Transform students into a list of dictionaries
student_results = [
    {
        "name": student["name"],
        "average_score": round(
            sum(student["scores"]) / len(student["scores"]), 1
        )
    }
    for student in students
]

print("Q12 - Student results:")
print(student_results)


# Q13 - Count students in each track
track_counts = {}

for student in students:
    track = student["track"]
    track_counts[track] = track_counts.get(track, 0) + 1

print("\nQ13 - Students per track:")
print(track_counts)


# Q14 - Unique tracks
# A set automatically eliminates duplicate values.
unique_tracks = {student["track"] for student in students}

print("\nQ14 - Unique tracks:")
print(unique_tracks)