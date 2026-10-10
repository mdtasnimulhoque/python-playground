
# Lesson 9: Tuples and Sets — Fixed Collections and Unique Values

print("=== Experiment 1: Creating a tuple ===")

coordinates = (10, 20)
student = ("Tasnimul", 20, "Python", 95)

print("Coordinates:", coordinates)
print("Student:", student)
print("Type:", type(coordinates))

print("\n=== Experiment 2: Accessing tuple items ===")

languages = ("Python", "Java", "C++", "JavaScript")

print("First language:", languages[0])
print("Second language:", languages[1])
print("Last language:", languages[-1])
print("First two:", languages[:2])

print("\n=== Experiment 3: One-item tuples ===")

single_value = (10,)
not_a_tuple = (10)

print("One-item tuple:", single_value)
print("Its type:", type(single_value))
print("Without comma:", type(not_a_tuple))

print("\n=== Experiment 4: Tuple methods ===")

scores = (95, 88, 95, 76, 95)

print("Number of scores:", len(scores))
print("Occurrences of 95:", scores.count(95))
print("Index of 88:", scores.index(88))
print("Contains 76:", 76 in scores)

print("\n=== Experiment 5: Tuple unpacking ===")

student_record = ("Tasnimul", 95, "Python")

name, score, subject = student_record

print("Name:", name)
print("Score:", score)
print("Subject:", subject)

print("\n=== Experiment 6: Swapping variables ===")

a = 10
b = 20

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)

print("\n=== Experiment 7: Creating sets ===")

numbers = {10, 20, 10, 30, 20, 40}

print("Set with duplicates:", numbers)
print("Unique number count:", len(numbers))

empty_set = set()

print("Empty set:", empty_set)
print("Empty set type:", type(empty_set))

print("\n=== Experiment 8: Adding set items ===")

languages = {"Python", "Java"}

languages.add("C++")
languages.add("Python")
languages.update(["JavaScript", "Go"])

print("Languages:", languages)
print("Language count:", len(languages))

print("\n=== Experiment 9: Removing set items ===")

languages.discard("Ruby")
print("No error when Ruby is absent:", languages)

languages.remove("Java")
print("After removing Java:", languages)

print("\n=== Experiment 10: Union ===")

python_students = {"Amina", "Tasnimul", "Rahul"}
java_students = {"Rahul", "Sara", "Tasnimul"}

everyone = python_students | java_students

print("All unique students:", sorted(everyone))

print("\n=== Experiment 11: Intersection ===")

both = python_students & java_students

print("Students in both groups:", sorted(both))

print("\n=== Experiment 12: Difference ===")

only_python = python_students - java_students
only_java = java_students - python_students

print("Only Python:", sorted(only_python))
print("Only Java:", sorted(only_java))

print("\n=== Experiment 13: Symmetric difference ===")

different = python_students ^ java_students

print("In exactly one group:", sorted(different))

print("\n=== Experiment 14: Set relationships ===")

programming = {"Python", "Java", "C++"}
beginner = {"Python", "Java"}
other_subjects = {"Biology", "History"}

print("Beginner is a subset:", beginner.issubset(programming))
print("Programming is a superset:", programming.issuperset(beginner))
print("Disjoint sets:", programming.isdisjoint(other_subjects))

print("\n=== Experiment 15: Converting collections ===")

subjects = ["Python", "Physics", "Python", "Mathematics"]

unique_subjects = set(subjects)
print("Unique subjects:", sorted(unique_subjects))

ordered_unique_subjects = list(dict.fromkeys(subjects))
print("Unique subjects in original order:", ordered_unique_subjects)

print("\n=== Experiment 16: Course enrollment analyzer ===")

python_students = {"Amina", "Tasnimul", "Rahul", "Sara"}
ai_students = {"Tasnimul", "Rahul", "Imran"}
web_students = {"Sara", "Rahul", "Nadia"}

print("Python or AI:", sorted(python_students | ai_students))
print("Python and AI:", sorted(python_students & ai_students))
print("Python but not AI:", sorted(python_students - ai_students))
print("Exactly one of Python and AI:", sorted(python_students ^ ai_students))

all_students = python_students | ai_students | web_students

print("Every unique student:", sorted(all_students))
print("Total unique students:", len(all_students))
print("Every AI student is in Python:", ai_students.issubset(python_students))

print("\n=== Experiment 17: Bonus challenge ===")

location = (25.01, 88.14)

latitude, longitude = location

print("Latitude:", latitude)
print("Longitude:", longitude)

print("\nAll 17 experiments completed!")