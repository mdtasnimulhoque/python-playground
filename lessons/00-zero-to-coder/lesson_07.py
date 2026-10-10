
# Lesson 7: Strings — Mastering Text in Python

print("=== Experiment 1: Creating strings ===")

name = "Tasnimul"
message = "I am learning Python"

print(name)
print(message)

print("\n=== Experiment 2: Combining strings ===")

first_name = "Tasnimul"
last_name = "Hoque"

full_name = first_name + " " + last_name
print(full_name)
print("Python! " * 3)

print("\n=== Experiment 3: Changing capitalization ===")

language = "python is interesting"

print(language.upper())
print(language.lower())
print(language.title())
print(language.capitalize())

print("\n=== Experiment 4: Cleaning spaces ===")

username = "   Tasnimul   "

print("Before:", repr(username))
print("After:", repr(username.strip()))

print("\n=== Experiment 5: Counting characters ===")

word = "Python"

print("Word:", word)
print("Characters:", len(word))
print("First character:", word[0])
print("Last character:", word[-1])

print("\n=== Experiment 6: Slicing strings ===")

language = "Python"

print("First three:", language[0:3])
print("Last three:", language[3:])
print("First four:", language[:4])

print("\n=== Experiment 7: Searching text ===")

message = "I am learning Python"

print("Contains Python:", "Python" in message)
print("Contains Java:", "Java" in message)
print("Position of Python:", message.find("Python"))
print("Position of Java:", message.find("Java"))

print("\n=== Experiment 8: Replacing text ===")

message = "I study mathematics"

updated_message = message.replace(
    "mathematics",
    "computer science"
)

print("Original:", message)
print("Updated:", updated_message)

print("\n=== Experiment 9: Splitting and joining ===")

subjects = "Python,Mathematics,Physics"

subject_list = subjects.split(",")

print("List:", subject_list)
print("Joined:", " | ".join(subject_list))

print("\n=== Experiment 10: Checking strings ===")

print("Starts with Py:", "Python".startswith("Py"))
print("Ends with pdf:", "report.pdf".endswith(".pdf"))
print("Is numeric:", "12345".isdigit())
print("Is alphabetic:", "Python".isalpha())

print("\n=== Experiment 11: Using f-strings ===")

student = "Tasnimul"
subject = "Python"
hours = 3

print(f"{student} studied {subject} for {hours} hours.")
print(
    f"After two more hours, "
    f"the total will be {hours + 2} hours."
)

print("\n=== Experiment 12: Strings are immutable ===")

word = "Python"

new_word = "J" + word[1:]

print("Original variable:", word)
print("New string:", new_word)

print("\n=== Experiment 13: Build an introduction ===")

person_name = "  tasnimul hoque  "
hobby = "singing"
goal = "build useful AI tools"

clean_name = person_name.strip().title()

introduction = (
    f"My name is {clean_name}. "
    f"I enjoy {hobby} and want to {goal}."
)

print(introduction)
print("Character count:", len(introduction))
print("Word count:", len(introduction.split()))
print("Mentions Python:", "python" in introduction.lower())