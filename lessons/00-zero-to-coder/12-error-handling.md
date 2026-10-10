# Lesson 12: Error Handling — Make Your Programs Resilient

## 1. What Is Error Handling?

Errors are a normal part of programming. A user might enter text when a program expects a number, a file might not exist, or a calculation might be invalid.

Error handling lets us respond to expected problems instead of allowing them to stop the entire program unexpectedly.

Consider this example:

```python
age = int(input("Enter your age: "))
print("Your age is:", age)
```

This works when the user enters a valid integer. But entering `hello` causes a `ValueError`.

We can handle that situation using `try` and `except`.

## 2. Understanding `try` and `except`

* `try`: Contains code that might raise an error.
* `except`: Handles a matching error if it occurs.

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a whole number.")
```

Try entering `19`, then run the program again and enter `hello`.

Notice how the program responds differently without showing a traceback to the user.

**Important:** Handle specific exceptions whenever possible. Avoid catching every possible error without understanding it.

## 3. Common Python Exceptions

### ValueError

An operation receives a value of the correct general type but cannot use its contents.

```python
number = int("hello")
```

### TypeError

An operation receives an inappropriate type.

```python
result = "Age: " + 19
```

### ZeroDivisionError

A number is divided by zero.

```python
result = 10 / 0
```

### IndexError

A sequence is accessed using an index that does not exist.

```python
colors = ["red", "blue"]
print(colors[5])
```

### KeyError

A dictionary is accessed using a missing key.

```python
student = {"name": "Tasnimul"}
print(student["grade"])
```

### FileNotFoundError

A program attempts to open a file that cannot be found.

```python
with open("missing_file.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

These examples deliberately demonstrate errors. Do not combine them into one program without handling them.

## 4. Handling More Than One Exception

A program may encounter different types of errors.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That was not a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Result:", result)
```

Each `except` block handles a different problem.

## 5. Understanding `else`

The `else` block runs only when the `try` block finishes without raising an exception.

```python
try:
    score = int(input("Enter a score: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    print("Your score is:", score)
```

Use `else` for code that should run only when the risky operation succeeds.

## 6. Understanding `finally`

The `finally` block runs whether an exception occurs or not, making it useful for cleanup tasks.

```python
try:
    print("Starting an operation.")
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Division failed.")
finally:
    print("Operation finished.")
```

The `finally` block is often useful when releasing resources or completing cleanup.

## 7. Raising Exceptions With `raise`

Sometimes a program must reject an invalid value deliberately.

```python
def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    return price * (1 - discount_percent / 100)


print(calculate_discount(1000, 20))
```

The function raises a `ValueError` when its inputs violate the rules.

The caller can decide whether to handle that exception:

```python
try:
    print(calculate_discount(1000, 120))
except ValueError as error:
    print("Could not calculate discount:", error)
```

## 8. Validation Is Not the Same as Error Handling

Error handling responds to exceptions. Validation checks whether data follows the rules of your program.

```python
score = 85

if 0 <= score <= 100:
    print("Valid score")
else:
    print("Score must be between 0 and 100")
```

A score of `150` is an integer, but it is not a valid score under these rules. The program should validate it even though converting it to an integer would succeed.

## 9. Common Mistakes to Avoid

1. Using `except:` without specifying an exception.
2. Catching an exception and silently ignoring it.
3. Putting an entire program inside one large `try` block.
4. Assuming error handling makes invalid data valid.
5. Forgetting to handle expected user input errors.
6. Using `raise` without providing a meaningful explanation when one would help.
7. Catching an exception that the program cannot reasonably recover from.

## 10. Practice Checklist

By the end of this lesson, you should be able to:

* [ ] Explain why error handling is useful.
* [ ] Use `try` and `except`.
* [ ] Handle `ValueError`, `TypeError`, and `ZeroDivisionError`.
* [ ] Handle multiple exception types separately.
* [ ] Explain the purpose of `else` and `finally`.
* [ ] Raise an exception with a meaningful message.
* [ ] Distinguish input validation from exception handling.
* [ ] Build a program that handles invalid input gracefully.

## 11. Challenge

Create a score-entry program that:

1. Asks the user to enter a score.
2. Handles non-integer input.
3. Rejects scores below 0 or above 100.
4. Prints the score only when it is valid.
5. Displays a clear, helpful message when the input is invalid.

Do not use `except:` to catch every possible exception.

**Next lesson:** Lesson 13 — Files and Data.
