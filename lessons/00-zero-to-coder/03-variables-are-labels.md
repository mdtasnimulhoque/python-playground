# Lesson 3: Variables Are Labels 🏷️

**Time:** 20–25 minutes · **Prerequisites:** Lessons 1–2

## 🎯 Mission

By the end of this lesson, you will be able to:

* Create a variable and store a value in it.
* Read and update a variable.
* Choose clear, meaningful variable names.
* Use variables in calculations and messages.
* Recognize and fix common variable mistakes.

## 1. The Hook: Give Your Information a Name

Imagine you have a box with a label that says `score`. The label helps you refer to the information stored there.

Python lets us do something similar.

```python
score = 10
print(score)
```

**Output:**

```text
10
```

Let's understand each part:

* `score` is the variable name.
* `=` is the assignment operator.
* `10` is the value being assigned.
* `print(score)` tells Python to display the value associated with the name `score`.

### Important: `=` does not mean the same thing as in mathematics

In Python, this line:

```python
score = 10
```

means: **assign the value `10` to the name `score`.**

It does not mean that Python is checking whether two mathematical expressions are equal.

Think of assignment as giving a name a value you can use later.

## 2. Create Your First Variables

A variable can store different kinds of values.

```python
name = "Mira"
age = 16
height = 1.62
is_learning_python = True

print(name)
print(age)
print(height)
print(is_learning_python)
```

**Output:**

```text
Mira
16
1.62
True
```

Notice how each value has a different type:

* `"Mira"` is a string (`str`) because it is text.
* `16` is an integer (`int`) because it is a whole number.
* `1.62` is a float (`float`) because it is a decimal number.
* `True` is a Boolean (`bool`) because it represents a truth value.

You learned about these types in Lesson 2. Variables give us a way to store and reuse them.

## 3. Change a Variable's Value

Variables are useful because their values can change.

```python
score = 10
print(score)

score = 15
print(score)
```

**Output:**

```text
10
15
```

The first assignment gives `score` the value `10`. The second assignment replaces that value with `15`.

When Python reaches `print(score)` the second time, it displays `15`.

### Your turn: Predict before running

What do you think this program will print?

```python
level = 1
print(level)

level = 2
level = 3
print(level)
```

Write down your prediction before running the code.

**Answer:** It prints `1`, followed by `3`. The value `2` is assigned to `level`, but nothing prints it before the next assignment changes the value to `3`.

## 4. Variables Can Work with Other Variables

You don't have to use only fixed numbers. You can use variables to calculate new values.

```python
coins = 3
coins = coins + 2
print(coins)
```

**Output:**

```text
5
```

Let's break down the second line:

```python
coins = coins + 2
```

Python first looks up the current value of `coins`, which is `3`. It adds `2`, producing `5`, and assigns that result back to `coins`.

This is a common programming pattern: **use the current value to calculate an updated value.**

Try another example:

```python
apples = 5
apples = apples - 2
print(apples)
```

**Output:**

```text
3
```

You can add, subtract, multiply, or divide values using variables.

## 5. Choose Meaningful Variable Names

Compare these two programs.

**Program A**

```python
x = "Mira"
y = 25
z = 3

print(x, y, z)
```

**Program B**

```python
player_name = "Mira"
points = 25
lives = 3

print(player_name, points, lives)
```

Both programs work. However, Program B is easier to understand because its names explain what the values represent.

Good variable names make code easier to read, understand, and maintain.

### Python naming rules

* Use letters, digits, and underscores (`_`).
* Do not start a variable name with a digit.
* Do not use spaces in variable names.
* Variable names are case-sensitive: `points` and `Points` are different names.
* Avoid Python keywords such as `if`, `for`, and `class` as variable names.
* Prefer descriptive names such as `student_name` over unclear names such as `sn`.

Python programmers commonly use **snake_case** for variable names.

For example:

```python
student_name = "Ayan"
total_marks = 450
favorite_subject = "Physics"
```

## 6. Combine Variables with Text

Variables can help you create messages that change when their values change.

```python
name = "Mira"
score = 25

print("Player:", name)
print("Score:", score)
```

**Output:**

```text
Player: Mira
Score: 25
```

The `print()` function can display multiple values separated by commas.

You can also use an **f-string** to insert variable values into text:

```python
name = "Mira"
score = 25

print(f"{name} scored {score} points!")
```

**Output:**

```text
Mira scored 25 points!
```

The `f` before the opening quotation mark tells Python to evaluate expressions inside curly braces (`{}`).

For now, remember this useful pattern:

```python
print(f"Hello, {name}!")
```

If `name` contains `"Mira"`, Python displays `Hello, Mira!`.

## 7. Debugging Detective 🕵️

Find the mistake in this program:

```python
favorite_color = "blue"
print(favourite_color)
```

Python reports a `NameError` because `favorite_color` and `favourite_color` are different names.

Python does not automatically know that you intended them to refer to the same value.

### Fix it

Make both spellings consistent:

```python
favorite_color = "blue"
print(favorite_color)
```

**Output:**

```text
blue
```

### Another common mistake

What is wrong here?

```python
2score = 10
print(2score)
```

The variable name starts with a digit, which is not allowed.

One correction is:

```python
score2 = 10
print(score2)
```

**Debugging habit:** When you see a `NameError`, check whether the variable was assigned a value and whether you spelled its name consistently.

## 8. Coding Lab: Update a Character's Status

Your fictional game character begins with 100 energy points and 0 collected stars.

Write a program that:

1. Creates variables for the character's name, energy, and stars.
2. Prints the character's starting status.
3. Reduces energy by 20.
4. Increases the number of stars by 3.
5. Prints the updated status.

### Starter code

```python
character_name = "Nova"
energy = 100
stars = 0

print("Starting status:")
print(f"Character: {character_name}")
print(f"Energy: {energy}")
print(f"Stars: {stars}")

# Update the character's status below


# Print the updated status below
```

Try to complete the program yourself before looking at the example solution.

<details>
<summary>Example solution</summary>

```python
character_name = "Nova"
energy = 100
stars = 0

print("Starting status:")
print(f"Character: {character_name}")
print(f"Energy: {energy}")
print(f"Stars: {stars}")

energy = energy - 20
stars = stars + 3

print("\nUpdated status:")
print(f"Character: {character_name}")
print(f"Energy: {energy}")
print(f"Stars: {stars}")
```

The updated status should show 80 energy points and 3 stars.

</details>

## 9. Boss Challenge: Build a Mini Profile 🏆

Create a small profile for a fictional person or character.

Your program must:

* Store a name, age, and favorite subject in variables.
* Store a score in another variable.
* Display all four values in a readable report.
* Increase the score by 10.
* Display the updated score.

**Stretch challenge:** Change the character's name and score, then run the program again. Can you update the information without rewriting your output messages?

## 10. Practice in VS Code

Your project already includes this practice file:

`lessons/00-zero-to-coder/lesson_03.py`

Open that file in VS Code and use it to experiment with the examples from this lesson.

Try the following:

1. Create three variables with different types of values.
2. Print their values.
3. Change one variable and print it again.
4. Calculate a new value using an existing variable.
5. Create a message using an f-string.
6. Intentionally misspell a variable name, observe the error, and fix it.

Save your file when you're done.

## 11. Retrieval Review 🧠

Answer these questions without looking back at the lesson.

**Question 1:** What does `=` do when used in a Python assignment?

**Question 2:** What does this program print?

```python
points = 10
points = points + 5
print(points)
```

**Question 3:** Are `score` and `Score` the same variable name?

**Question 4:** What is wrong with this code?

```python
student_name = "Ayan"
print(students_name)
```

**Question 5:** Why are meaningful variable names useful?

**Question 6:** What will this program print?

```python
name = "Mira"
score = 20
score = score + 5

print(f"{name} scored {score} points.")
```

### Answer key

1. It assigns a value to a variable name.
2. `15`.
3. No. Python variable names are case-sensitive.
4. The variable names do not match: `student_name` and `students_name`.
5. They make programs easier to read, understand, debug, and maintain.
6. `Mira scored 25 points.`

## 12. Completion Checklist ✅

Before moving on, make sure you can:

* [ ] Create variables and assign values.
* [ ] Explain what happens when a variable is reassigned.
* [ ] Use variables in calculations.
* [ ] Choose meaningful names that follow Python's naming rules.
* [ ] Display variable values using `print()`.
* [ ] Use an f-string to insert values into a message.
* [ ] Find and fix a variable-name error.

**You completed Lesson 3!** 🎉

You can now give information a name, update it, and use it to build programs that do more than print fixed messages.

**Next lesson:** Conditions — teaching Python to make decisions with `if`, `elif`, and `else`.
