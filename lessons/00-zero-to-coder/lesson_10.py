# Lesson 10: Functions — Practice Experiments

print("=== Experiment 1: Define and call a function ===")


def greet():
    print("Hello, Python learner!")


greet()
greet()


print("\n=== Experiment 2: Functions with parameters ===")


def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Tasnimul")
greet_person("Nora")
greet_person("Andria")


print("\n=== Experiment 3: Multiple parameters ===")


def introduce(name, subject):
    print(f"My name is {name}, and I am learning {subject}.")


introduce("Tasnimul", "Python")


print("\n=== Experiment 4: Returning a value ===")


def add(a, b):
    return a + b


result = add(10, 20)
print("Result:", result)
print("Result multiplied by 2:", result * 2)


print("\n=== Experiment 5: Print versus return ===")


def print_sum(a, b):
    print(a + b)


def return_sum(a, b):
    return a + b


printed_result = print_sum(5, 3)
returned_result = return_sum(5, 3)

print("Printed function result:", printed_result)
print("Returned function result:", returned_result)


print("\n=== Experiment 6: Default parameters ===")


def greet_with_default(name="learner"):
    print(f"Welcome, {name}!")


greet_with_default()
greet_with_default("Tasnimul")


print("\n=== Experiment 7: Keyword arguments ===")


def describe_student(name, subject, score):
    return f"{name} studies {subject} and scored {score}."


report = describe_student(
    score=95,
    name="Tasnimul",
    subject="Python",
)

print(report)


print("\n=== Experiment 8: Returning different values ===")


def square(number):
    return number * number


def is_even(number):
    return number % 2 == 0


print("Square of 6:", square(6))
print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))


print("\n=== Experiment 9: One function calling another ===")


def sum_of_squares(a, b):
    return square(a) + square(b)


print("Sum of squares of 3 and 4:", sum_of_squares(3, 4))


print("\n=== Experiment 10: Local variables ===")


def calculate_total(price, quantity):
    total = price * quantity
    return total


total_cost = calculate_total(50, 3)
print("Total cost:", total_cost)


print("\n=== Experiment 11: Docstrings and type hints ===")


def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b


print("Product:", multiply(4, 5))
print("Documentation:", multiply.__doc__)
print("Function name:", multiply.__name__)


print("\n=== Experiment 12: Personal calculator ===")


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        return "Error: division by zero is not allowed."
    return a / b


print("Addition:", add(12, 4))
print("Subtraction:", subtract(12, 4))
print("Multiplication:", multiply(12, 4))
print("Division:", divide(12, 4))
print("Division by zero:", divide(12, 0))


print("\n=== Experiment 13: Calculate an average ===")


def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


scores = [85, 90, 95, 80]

print("Scores:", scores)
print("Average:", calculate_average(scores))
print("Empty list average:", calculate_average([]))


print("\n=== Experiment 14: Student grade analyzer ===")


def determine_grade(average):
    if not 0 <= average <= 100:
        return "Invalid score"
    elif average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 50:
        return "Developing"
    else:
        return "Needs more practice"


def create_student_report(name, scores):
    if len(scores) == 0:
        return f"No scores available for {name}."

    if any(score < 0 or score > 100 for score in scores):
        return f"Invalid score found for {name}."

    average = calculate_average(scores)
    grade = determine_grade(average)

    return (
        f"Student: {name}\n"
        f"Average: {average:.2f}\n"
        f"Grade: {grade}"
    )


print(create_student_report("Tasnimul", [95, 92, 98]))
print()
print(create_student_report("Nora", [78, 82, 75]))
print()
print(create_student_report("Andria", [40, 45, 48]))
print()
print(create_student_report("Student X", []))
print()
print(create_student_report("Student Y", [90, 105, 80]))


print("\nAll 14 experiments completed!")