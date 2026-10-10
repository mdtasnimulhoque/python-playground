# Lesson 11: Modules and Imports — Organize Your Python Code

## What You Will Learn

By the end of this lesson, you will be able to:

* Explain what a module is.
* Import Python's built-in modules.
* Use `math`, `random`, and `statistics`.
* Import specific functions from a module.
* Give imported modules shorter names using aliases.
* Create and import your own Python modules.
* Understand why Python uses `if __name__ == "__main__":`.
* Organize code into reusable files.

---

## 1. What Is a Module?

Imagine building a large application. Keeping every instruction in one enormous file would make it difficult to understand and maintain.

Python lets you organize related code into separate files called **modules**.

A Python file ending in `.py` can be a module.

For example:

```text
python-playground/
├── lesson_11.py
└── calculator.py
```

The `calculator.py` file could contain mathematical functions, while `lesson_11.py` imports and uses them.

**Remember:**

* A function organizes reusable instructions.
* A module organizes reusable Python code in a file.
* A package organizes related modules into a directory structure.

## 2. Your First Import

Python includes many useful modules.

Try this:

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

Here, `import math` makes the `math` module available.

The dot in `math.sqrt` means we are accessing something inside the `math` module.

## 3. Explore the Math Module

```python
import math

print("Square root:", math.sqrt(81))
print("Round up:", math.ceil(4.2))
print("Round down:", math.floor(4.8))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Pi:", math.pi)
```

Expected output:

```text
Square root: 9.0
Round up: 5
Round down: 4
Factorial: 120
Power: 8.0
Pi: 3.141592653589793
```

Note that `math.factorial(5)` calculates \(5 \times 4 \times 3 \times 2 \times 1\).

## 4. Import Only What You Need

Instead of writing `math.sqrt`, you can import `sqrt` directly.

```python
from math import sqrt, pi

print(sqrt(144))
print(pi)
```

You can also use an alias:

```python
import math as m

print(m.sqrt(49))
print(m.pi)
```

Both approaches work. For beginners, `import math` is often easier to understand because it makes the source of each function clear.

## 5. Generate Random Values

The `random` module helps you generate pseudorandom values, select random items, and shuffle lists.

```python
import random

print(random.randint(1, 10))

subjects = ["Python", "Physics", "Mathematics"]

print(random.choice(subjects))

random.shuffle(subjects)
print(subjects)
```

Your output may differ each time. That is expected.

Important functions:

* `random.randint(a, b)`: returns an integer from `a` through `b`, including both endpoints.
* `random.choice(items)`: selects one item from a non-empty sequence.
* `random.shuffle(items)`: shuffles a mutable sequence in place.

Randomness is useful for games and simulations, but ordinary `random` functions are not suitable for security-sensitive secrets or passwords.

## 6. Calculate Statistics

The `statistics` module can calculate useful summaries of numerical data.

```python
import statistics

scores = [80, 90, 85, 95, 90]

print("Mean:", statistics.mean(scores))
print("Median:", statistics.median(scores))
print("Mode:", statistics.mode(scores))
```

Expected output:

```text
Mean: 88
Median: 90
Mode: 90
```

* **Mean:** the arithmetic average.
* **Median:** the middle value after sorting.
* **Mode:** the most frequently occurring value.

## 7. Understand Import Errors

Consider this code:

```python
import maths

print(maths.sqrt(25))
```

If no module named `maths` exists in your environment, Python raises `ModuleNotFoundError`.

The correct built-in module name is `math`.

Another common mistake is:

```python
import math

print(sqrt(25))
```

This raises `NameError` because `sqrt` was not imported directly. Use `math.sqrt(25)` or import it using `from math import sqrt`.

**Debugging rule:** Check the module name, the spelling of the function, and how you imported it.

## 8. Create Your Own Module

Let's create a reusable module.

In the same folder as your practice file, create:

`study_tools.py`

Put this code inside it:

```python
def calculate_average(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def classify_score(score):
    if not 0 <= score <= 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 75:
        return "Good"
    if score >= 50:
        return "Developing"

    return "Needs more practice"
```

Save the file.

Now, in `lesson_11.py`, write:

```python
import study_tools

scores = [95, 82, 76, 91]

average = study_tools.calculate_average(scores)

print("Average:", average)
print("Grade:", study_tools.classify_score(average))
```

Expected output:

```text
Average: 86.0
Grade: Good
```

Both files must be in the same directory for this simple example to work without extra configuration.

## 9. Why Use `if __name__ == "__main__":`?

A module can be imported by another file. Sometimes, you want certain code to run only when you execute the module directly, not when another file imports it.

Update `study_tools.py` by adding this at the bottom:

```python
if __name__ == "__main__":
    sample_scores = [80, 90, 100]
    print("Testing study_tools")
    print(calculate_average(sample_scores))
```

When you run `study_tools.py` directly, the test code runs.

When another file imports `study_tools`, the test code does not run automatically.

This pattern is common in real Python projects.

## 10. Mini Project: Student Performance Analyzer

Build a program that:

1. Imports your `study_tools` module.
2. Stores a student's scores in a list.
3. Calculates their average.
4. Classifies the average.
5. Prints a readable report.

Example:

```python
import study_tools

student_name = "Tasnimul"
scores = [95, 88, 92, 85]

average = study_tools.calculate_average(scores)

print("Student:", student_name)
print(f"Average: {average:.2f}")
print("Performance:", study_tools.classify_score(average))
```

Expected output:

```text
Student: Tasnimul
Average: 90.00
Performance: Excellent
```

### Boss Challenge

Extend the program to analyze three students. Store each student's scores in a dictionary, calculate each average, and print the highest-scoring student.

Bonus: Import `statistics` and display each student's median score.

## 11. Retrieval Practice

Answer these questions without looking back:

1. What is a Python module?
2. What does `import math` do?
3. What is the difference between `import math` and `from math import sqrt`?
4. Why might a program use `import random`?
5. What causes `ModuleNotFoundError`?
6. Why is it useful to create your own modules?
7. What does `if __name__ == "__main__":` help control?

## 12. Completion Checklist

* [ ] I understand what modules are.
* [ ] I used `math`, `random`, and `statistics`.
* [ ] I understand module aliases and direct imports.
* [ ] I created and imported `study_tools.py`.
* [ ] I understand the `__main__` guard.
* [ ] I completed the Student Performance Analyzer.

## What's Next?

**Lesson 12: Error Handling with `try`, `except`, `else`, and `finally`.**

You'll learn to build programs that handle invalid input and unexpected situations more gracefully.
