
# Lesson 11: Modules and Imports — Practice Experiments

import math
import random
import statistics


print("=== Experiment 1: Importing the math module ===")

print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)


print("\n=== Experiment 2: Useful math functions ===")

print("Square root of 81:", math.sqrt(81))
print("Round up:", math.ceil(4.2))
print("Round down:", math.floor(4.8))
print("Factorial of 5:", math.factorial(5))
print("Power of 2 to 3:", math.pow(2, 3))


print("\n=== Experiment 3: Importing specific functions ===")

from math import sqrt, pi

print("Square root of 144:", sqrt(144))
print("Pi:", pi)


print("\n=== Experiment 4: Using an alias ===")

import math as m

print("Square root of 49:", m.sqrt(49))
print("Pi through alias:", m.pi)


print("\n=== Experiment 5: Generating random values ===")

subjects = ["Python", "Physics", "Mathematics"]

print("Random integer from 1 to 10:", random.randint(1, 10))
print("Random subject:", random.choice(subjects))

random.shuffle(subjects)
print("Shuffled subjects:", subjects)


print("\n=== Experiment 6: Calculating statistics ===")

scores = [80, 90, 85, 95, 90]

print("Scores:", scores)
print("Mean:", statistics.mean(scores))
print("Median:", statistics.median(scores))
print("Mode:", statistics.mode(scores))


print("\n=== Experiment 7: Understanding imports ===")

print("Math module name:", math.__name__)
print("Square root of 36:", math.sqrt(36))
print("The math module was imported successfully.")


print("\n=== Experiment 8: Creating reusable functions ===")


def calculate_average(numbers):
    if len(numbers) == 0:
        return None

    return sum(numbers) / len(numbers)


def classify_score(score):
    if not 0 <= score <= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Developing"
    else:
        return "Needs more practice"


sample_scores = [95, 82, 76, 91]
average = calculate_average(sample_scores)

print("Average:", average)
print("Classification:", classify_score(average))


print("\n=== Experiment 9: Import your own module ===")

# The study_tools.py file must be in this same folder.
import study_tools

module_scores = [95, 82, 76, 91]
module_average = study_tools.calculate_average(module_scores)

print("Average from study_tools:", module_average)
print("Grade from study_tools:",
      study_tools.classify_score(module_average))


print("\n=== Experiment 10: Student performance analyzer ===")

students = {
    "Tasnimul": [95, 88, 92, 85],
    "Nora": [78, 82, 75, 80],
    "Andria": [90, 94, 96, 92],
}

for student_name, student_scores in students.items():
    student_average = study_tools.calculate_average(student_scores)
    performance = study_tools.classify_score(student_average)

    print("\nStudent:", student_name)
    print(f"Average: {student_average:.2f}")
    print("Performance:", performance)


print("\n=== Experiment 11: Highest-scoring student ===")

averages = {}

for student_name, student_scores in students.items():
    averages[student_name] = study_tools.calculate_average(
        student_scores
    )

top_student = max(averages, key=averages.get)

print("Highest-scoring student:", top_student)
print(f"Average: {averages[top_student]:.2f}")


print("\n=== Experiment 12: Using statistics with student data ===")

for student_name, student_scores in students.items():
    median_score = statistics.median(student_scores)
    print(f"{student_name}'s median score: {median_score}")


print("\nAll 12 experiments completed!")