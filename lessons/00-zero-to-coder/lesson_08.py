
# Lesson 8: Dictionaries — Organize Information with Keys and Values

print("=== Experiment 1: Creating a dictionary ===")

student = {
    "name": "Tasnimul",
    "age": 20,
    "subject": "Python",
    "score": 95
}

print(student)

print("\n=== Experiment 2: Accessing values ===")

print("Name:", student["name"])
print("Subject:", student["subject"])
print("Score:", student["score"])

print("\n=== Experiment 3: Handling missing keys ===")

print("Age:", student.get("age"))
print("City:", student.get("city"))
print("City with default:", student.get("city", "Not provided"))

print("\n=== Experiment 4: Adding information ===")

student["city"] = "Malda"
student["level"] = "Beginner"

print(student)

student.update({
    "hobby": "Singing",
    "goal": "Build useful AI tools"
})

print("After update:", student)

print("\n=== Experiment 5: Updating values ===")

student["score"] = 98

print("Updated score:", student["score"])

print("\n=== Experiment 6: Removing information ===")

removed_city = student.pop("city")

print("Removed city:", removed_city)
print("Remaining information:", student)

print("\n=== Experiment 7: Inspecting a dictionary ===")

print("Number of fields:", len(student))
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Key-value pairs:", list(student.items()))

print("\n=== Experiment 8: Looping through a dictionary ===")

for key, value in student.items():
    print(f"{key}: {value}")

print("\n=== Experiment 9: Checking keys and values ===")

print("Has name key:", "name" in student)
print("Has city key:", "city" in student)
print("Has Tasnimul value:", "Tasnimul" in student.values())

print("\n=== Experiment 10: Lists inside dictionaries ===")

profile = {
    "name": "Tasnimul",
    "subjects": ["Python", "Physics", "Mathematics"]
}

print("Subjects:", profile["subjects"])
print("First subject:", profile["subjects"][0])

profile["subjects"].append("Computer Science")

print("Updated subjects:", profile["subjects"])

print("\n=== Experiment 11: Nested dictionaries ===")

students = {
    "student_1": {
        "name": "Tasnimul",
        "score": 95
    },
    "student_2": {
        "name": "Amina",
        "score": 89
    },
    "student_3": {
        "name": "Rahul",
        "score": 92
    }
}

print("First student:", students["student_1"]["name"])
print("Second student's score:", students["student_2"]["score"])

students["student_1"]["score"] = 98

print("Updated first score:", students["student_1"]["score"])

print("\n=== Experiment 12: Student score tracker ===")

scores = {
    "Python": 95,
    "Mathematics": 88,
    "Physics": 91
}

for subject, score in scores.items():
    print(f"{subject}: {score}")

scores["Mathematics"] = 92
scores["Computer Science"] = 97
scores.pop("Physics")

print("\nUpdated scores:")

for subject, score in scores.items():
    print(f"{subject}: {score}")

print("Number of subjects:", len(scores))

print("\n=== Experiment 13: Calculate student average ===")

total_score = 0

for record in students.values():
    total_score += record["score"]

average_score = total_score / len(students)

print(f"Average student score: {average_score:.2f}")

top_student = max(
    students.values(),
    key=lambda record: record["score"]
)

print("Highest-scoring student:", top_student["name"])
print("Highest score:", top_student["score"])

print("\n=== Experiment 14: Personal profile manager ===")

person = {
    "name": "Tasnimul Hoque",
    "location": "Malda",
    "hobby": "Singing",
    "language": "Python",
    "goal": "Learn AI and machine learning"
}

person["current_project"] = "Python Playground"
person["goal"] = "Build useful AI tools"

print("Hobby exists:", "hobby" in person)
print("Total profile fields:", len(person))

for key, value in person.items():
    print(f"{key.replace('_', ' ').title()}: {value}")