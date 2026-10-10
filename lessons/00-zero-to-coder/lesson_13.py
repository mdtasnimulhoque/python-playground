
# Lesson 13: Files and Data — Practice Experiments

import json
from pathlib import Path

# Store generated files in a dedicated folder beside this script.
SCRIPT_FOLDER = Path(__file__).resolve().parent
DATA_FOLDER = SCRIPT_FOLDER / "lesson_13_data"
DATA_FOLDER.mkdir(exist_ok=True)


print("=== Experiment 1: Creating a text file ===")

notes_path = DATA_FOLDER / "notes.txt"

with open(notes_path, "w", encoding="utf-8") as file:
    file.write("I am learning Python.\n")
    file.write("Today I learned about files.\n")

print("Created:", notes_path.name)


print("\n=== Experiment 2: Reading a text file ===")

with open(notes_path, "r", encoding="utf-8") as file:
    contents = file.read()

print(contents, end="")


print("\n=== Experiment 3: Reading line by line ===")

with open(notes_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.rstrip()}")


print("\n=== Experiment 4: Appending to a file ===")

with open(notes_path, "a", encoding="utf-8") as file:
    file.write("Appending adds new information.\n")

with open(notes_path, "r", encoding="utf-8") as file:
    print(file.read(), end="")


print("\n=== Experiment 5: Exploring file paths ===")

print("File name:", notes_path.name)
print("Extension:", notes_path.suffix)
print("Exists:", notes_path.exists())
print("Parent folder:", notes_path.parent.name)


print("\n=== Experiment 6: Handling a missing file ===")

missing_path = DATA_FOLDER / "missing.txt"

try:
    with open(missing_path, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Handled correctly: the file does not exist.")


print("\n=== Experiment 7: Creating JSON data ===")

student = {
    "name": "Tasnimul",
    "score": 92,
    "subjects": ["Python", "Physics", "Mathematics"]
}

student_path = DATA_FOLDER / "student.json"

with open(student_path, "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Saved student data to:", student_path.name)


print("\n=== Experiment 8: Loading JSON data ===")

with open(student_path, "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print("Name:", loaded_student["name"])
print("Score:", loaded_student["score"])
print("Subjects:", loaded_student["subjects"])


print("\n=== Experiment 9: JSON strings ===")

json_text = json.dumps(student, indent=2)
print(json_text)

restored_student = json.loads(json_text)
print("Restored name:", restored_student["name"])


print("\n=== Experiment 10: Handling invalid JSON ===")

invalid_json = '{"name": "Tasnimul",}'

try:
    json.loads(invalid_json)
except json.JSONDecodeError:
    print("Handled correctly: the JSON format is invalid.")


print("\n=== Experiment 11: Saving multiple student records ===")

students = [
    {"name": "Tasnimul", "score": 92},
    {"name": "Nora", "score": 84},
    {"name": "Andria", "score": 96}
]

students_path = DATA_FOLDER / "students.json"

with open(students_path, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

with open(students_path, "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

for record in loaded_students:
    print(f"{record['name']}: {record['score']}")


print("\n=== Experiment 12: Building a study tracker ===")

study_sessions = [
    {
        "subject": "Python",
        "topic": "File handling",
        "minutes": 45
    },
    {
        "subject": "Physics",
        "topic": "Laws of Motion",
        "minutes": 60
    },
    {
        "subject": "Mathematics",
        "topic": "Functions",
        "minutes": 30
    }
]

sessions_path = DATA_FOLDER / "study_sessions.json"

with open(sessions_path, "w", encoding="utf-8") as file:
    json.dump(study_sessions, file, indent=4)

try:
    with open(sessions_path, "r", encoding="utf-8") as file:
        saved_sessions = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("Could not load the study sessions.")
else:
    total_minutes = 0

    for session in saved_sessions:
        print(
            f"{session['subject']} — {session['topic']}: "
            f"{session['minutes']} minutes"
        )
        total_minutes += session["minutes"]

    print("Total study time:", total_minutes, "minutes")


print("\n=== Experiment 13: Checking saved files ===")

for path in sorted(DATA_FOLDER.iterdir()):
    print(f"{path.name}: {path.stat().st_size} bytes")


print("\nAll 13 experiments completed!")