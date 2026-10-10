
# Lesson 6: Lists — Store Many Values Together

print("=== Experiment 1: Create a list ===")

subjects = ["Python", "Mathematics", "Physics"]
print(subjects)

print("\n=== Experiment 2: Access items ===")

print("First subject:", subjects[0])
print("Last subject:", subjects[-1])

print("\n=== Experiment 3: Update an item ===")

subjects[1] = "Biology"
print(subjects)

print("\n=== Experiment 4: Add items ===")

subjects.append("Chemistry")
subjects.insert(1, "English")
subjects.extend(["History", "Geography"])
print(subjects)

print("\n=== Experiment 5: Remove items ===")

subjects.remove("History")
removed_subject = subjects.pop(0)
print("Removed:", removed_subject)
print("Remaining subjects:", subjects)

print("\n=== Experiment 6: Count items ===")

print("Total subjects:", len(subjects))

print("\n=== Experiment 7: Loop through a list ===")

for number, subject in enumerate(subjects, start=1):
    print(f"{number}. {subject}")

print("\n=== Experiment 8: Build a task list ===")

tasks = []
tasks.append("Learn Python")
tasks.append("Practise loops")
tasks.append("Explore lists")

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print("Total tasks:", len(tasks))