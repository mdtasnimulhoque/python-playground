# Lesson 10: Functions — Write Once, Reuse Everywhere ⚙️

**Level:** 0 — Zero to Coder
**Prerequisites:** Lessons 1–9
**Estimated time:** 75–100 minutes
**Practice file:** `lessons/00-zero-to-coder/lesson_10.py`

---

## 1. Why Do We Need Functions?

Imagine you need to greet three students.

Without a function, you might write:

```python
print("Hello, Tasnimul!")
print("Hello, Amina!")
print("Hello, Rahul!")
```

Now imagine greeting 100 students. Repeating the same instructions would be tedious.

A **function** is a reusable block of code that performs a particular task.

Instead of writing the greeting instructions repeatedly, you can define a function once and call it whenever you need it.

```python
def greet():
    print("Hello, Python learner!")

greet()
greet()
greet()
```

Output:

```text
Hello, Python learner!
Hello, Python learner!
Hello, Python learner!
```

You wrote the instructions once but used them three times.

Functions help you:

* Reuse code.
* Organize programs into smaller pieces.
* Avoid unnecessary repetition.
* Test and debug individual parts.
* Make programs easier to understand and maintain.

---

## 2. Defining and Calling a Function

Let's examine the structure.

```python
def greet():
    print("Hello, Tasnimul!")

greet()
```

Each part has a purpose:

* `def` tells Python that you are defining a function.
* `greet` is the function's name.
* `()` contains the function's parameters, if any.
* `:` marks the beginning of the function body.
* The indented line contains the instructions.
* `greet()` calls the function and executes its body.

**Important:** Defining a function does not automatically execute its body. You must call it.

For example:

```python
def greet():
    print("Hello!")

print("Program started.")
```

Output:

```text
Program started.
```

The greeting doesn't appear because `greet()` was never called.

Now add:

```python
greet()
```

The function will execute when Python reaches that call.

---

## 3. Functions with Parameters

A function becomes more flexible when it accepts input.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Tasnimul")
greet("Amina")
greet("Rahul")
```

Output:

```text
Hello, Tasnimul!
Hello, Amina!
Hello, Rahul!
```

Here, `name` is a **parameter**. It acts as a variable that receives a value when the function is called.

The values `"Tasnimul"`, `"Amina"`, and `"Rahul"` are **arguments** supplied to the function.

A useful distinction:

* **Parameter:** A name written in the function definition.
* **Argument:** A value supplied in a function call.

You can have multiple parameters:

```python
def introduce(name, subject):
    print(f"My name is {name}, and I am learning {subject}.")

introduce("Tasnimul", "Python")
introduce("Amina", "Mathematics")
```

Output:

```text
My name is Tasnimul, and I am learning Python.
My name is Amina, and I am learning Mathematics.
```

---

## 4. Returning Values with `return`

So far, our functions have printed messages. But many functions need to calculate something and give the result back to the rest of the program.

That's what `return` does.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

The function calculates `a + b` and returns the result. The returned value is then stored in `result`.

### `print()` versus `return`

These are not the same.

```python
def add_and_print(a, b):
    print(a + b)

result = add_and_print(10, 20)

print("Stored result:", result)
```

Output:

```text
30
Stored result: None
```

Why does the variable contain `None`? Because the function printed the answer but didn't return a value.

Compare it with:

```python
def add_and_return(a, b):
    return a + b

result = add_and_return(10, 20)

print("Stored result:", result)
```

Output:

```text
Stored result: 30
```

**Remember:**

* `print()` displays information.
* `return` sends a value back to the code that called the function.

Use `return` when another part of your program needs to work with the result.

---

## 5. Functions Can Return Different Types of Values

A function can return numbers, strings, Booleans, lists, tuples, dictionaries, and more.

```python
def get_full_name(first, last):
    return f"{first} {last}"

def is_even(number):
    return number % 2 == 0

def get_subjects():
    return ["Python", "Physics", "Mathematics"]

print(get_full_name("Tasnimul", "Hoque"))
print(is_even(8))
print(get_subjects())
```

Output:

```text
Tasnimul Hoque
True
['Python', 'Physics', 'Mathematics']
```

A returned value can be stored, printed, passed into another function, or used in a condition.

```python
def square(number):
    return number * number

if square(5) > 20:
    print("The square is greater than 20.")
```

Output:

```text
The square is greater than 20.
```

---

## 6. Functions with Multiple Parameters

A function can accept several inputs.

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(50, 3)

print(f"Total cost: {total}")
```

Output:

```text
Total cost: 150
```

By default, positional arguments are matched to parameters in order.

```python
def describe_student(name, subject, score):
    return f"{name} studies {subject} and scored {score}."

print(describe_student("Tasnimul", "Python", 95))
```

Output:

```text
Tasnimul studies Python and scored 95.
```

The number of required arguments must normally match the function's parameters.

For example, calling `describe_student("Tasnimul")` would raise a `TypeError` because two required arguments are missing.

---

## 7. Keyword Arguments

You can specify which parameter receives which value by using keyword arguments.

```python
def introduce(name, subject, score):
    print(f"{name} studies {subject} and scored {score}.")

introduce(
    score=95,
    name="Tasnimul",
    subject="Python"
)
```

Output:

```text
Tasnimul studies Python and scored 95.
```

Keyword arguments make calls more readable and allow you to supply arguments by name rather than relying only on their position.

Positional arguments generally come before keyword arguments in a function call.

---

## 8. Default Parameter Values

Sometimes a function should use a default value when the caller doesn't provide one.

```python
def greet(name="learner"):
    print(f"Hello, {name}!")

greet()
greet("Tasnimul")
```

Output:

```text
Hello, learner!
Hello, Tasnimul!
```

The parameter `name` has a default value of `"learner"`.

You can also provide defaults for multiple parameters:

```python
def calculate_price(price, quantity=1):
    return price * quantity

print(calculate_price(100))
print(calculate_price(100, 3))
```

Output:

```text
100
300
```

Parameters with defaults must come after required parameters in a standard function definition.

---

## 9. Understanding Scope

**Scope** describes where a variable can be accessed.

### Local variables

A variable created inside a function is normally local to that function.

```python
def calculate():
    result = 10 + 20
    print(result)

calculate()
```

Output:

```text
30
```

Trying to access `result` outside the function raises a `NameError` because it is a local variable.

```python
def calculate():
    result = 10 + 20

calculate()
print(result)  # NameError
```

To use the result outside the function, return it:

```python
def calculate():
    result = 10 + 20
    return result

answer = calculate()
print(answer)
```

Output:

```text
30
```

### Global variables

A variable defined outside a function is global within its module.

```python
language = "Python"

def show_language():
    print(language)

show_language()
```

Output:

```text
Python
```

Functions can read global variables, but it's usually clearer to pass required values as parameters and return results rather than relying on many global variables.

---

## 10. A Function Can Call Another Function

Functions become especially useful when you combine them.

```python
def square(number):
    return number * number

def sum_of_squares(a, b):
    return square(a) + square(b)

result = sum_of_squares(3, 4)

print(result)
```

Output:

```text
25
```

Here's what happens:

1. `sum_of_squares(3, 4)` receives `3` and `4`.
2. `square(3)` returns `9`.
3. `square(4)` returns `16`.
4. The function returns `9 + 16`, which is `25`.

Breaking a problem into smaller functions makes each part easier to test and reuse.

---

## 11. Docstrings: Documenting Your Functions

A **docstring** explains what a function does. It is written as a string immediately inside the function body.

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width

print(calculate_area(5, 4))
print(calculate_area.__doc__)
```

Output:

```text
20
Return the area of a rectangle.
```

Docstrings are useful when other people need to understand your code.

For a function with more complex behavior, explain its purpose, important parameters, and returned value.

---

## 12. Type Hints: Making Intent Clear

Type hints indicate the kinds of values a function is intended to receive and return.

```python
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4, 5))
```

Output:

```text
20
```

In this example:

* `a: int` suggests that `a` should be an integer.
* `b: int` suggests that `b` should be an integer.
* `-> int` indicates that the function is expected to return an integer.

**Important:** Python generally does not enforce type hints at runtime. They help humans, editors, and static analysis tools understand your code.

---

## 13. Common Mistakes and Debugging

### Mistake 1: Forgetting to call the function

```python
def greet():
    print("Hello!")
```

Nothing is printed until you call:

```python
greet()
```

### Mistake 2: Forgetting the colon

Incorrect:

```python
def greet()
    print("Hello!")
```

Correct:

```python
def greet():
    print("Hello!")
```

### Mistake 3: Incorrect indentation

The function body must be indented.

```python
def greet():
    print("Hello!")
```

Use consistent indentation, usually four spaces.

### Mistake 4: Confusing `print()` with `return`

A printed value isn't automatically returned. If another part of your program needs the result, return it explicitly.

### Mistake 5: Returning before completing the function

```python
def example():
    return 10
    print("This will not run")

print(example())
```

Output:

```text
10
```

Execution exits the function when Python reaches `return`. Statements after that return in the same execution path won't run.

### Mistake 6: Passing the wrong number of arguments

```python
def add(a, b):
    return a + b

print(add(5))
```

This raises a `TypeError` because the function requires two arguments.

Correct:

```python
print(add(5, 3))
```

---

## 14. Coding Lab: Personal Calculator 🧮

Build a calculator using separate functions.

Your program should define functions for:

* Addition
* Subtraction
* Multiplication
* Division

Each function should accept two numbers and return the result.

Then:

1. Call every function.
2. Display the results with clear labels.
3. Handle division by zero before dividing.
4. Add a function called `calculate_average()` that accepts a list of numbers and returns their average.
5. Test your functions with different values.

**Hints:**

```python
def add(a, b):
    return a + b
```

For division, check whether the second number is zero before performing the calculation. Decide whether your function should return a message or raise an exception for invalid input, and be consistent.

---

## 15. Boss Challenge: Student Grade Analyzer 🏆

Create a small grade analyzer using functions.

Your program should:

* Define a function that calculates the average of a list of scores.
* Define a function that determines a grade category from an average.
* Define a function that returns a formatted student report.
* Use parameters instead of hardcoding all values inside the functions.
* Return values so the functions can be reused.
* Test the program with at least three different score lists.

You may use these example categories:

* 90 or above: Excellent
* 75–89: Good
* 50–74: Developing
* Below 50: Needs more practice

Decide how your program should handle an empty list and scores outside the range 0–100. Explain your decision in a comment.

---

## 16. Retrieval Practice

Answer these questions without looking back.

1. What is a function?
2. What does `def` do?
3. What is the difference between defining and calling a function?
4. What is the difference between a parameter and an argument?
5. What does `return` do?
6. How does `return` differ from `print()`?
7. What is a default parameter?
8. What is a keyword argument?
9. What does scope mean?
10. Why is returning a value often better than relying on a global variable?
11. What is a docstring?
12. Do Python type hints automatically enforce types at runtime?

---

## 17. Completion Checklist

Before moving to Lesson 11, make sure you can:

* [ ] Define and call a function.
* [ ] Use parameters and arguments.
* [ ] Return values.
* [ ] Explain `print()` versus `return`.
* [ ] Use multiple parameters.
* [ ] Use keyword arguments.
* [ ] Define default parameter values.
* [ ] Understand local and global scope.
* [ ] Call one function from another.
* [ ] Write useful docstrings.
* [ ] Read and write basic type hints.
* [ ] Build the Personal Calculator.
* [ ] Attempt the Student Grade Analyzer.

**Next lesson:** Modules and Imports — Organize Code Across Files.

The key idea is simple: a good function does one clear job, accepts the information it needs, and returns a useful result when appropriate.
