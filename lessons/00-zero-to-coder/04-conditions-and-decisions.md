# Lesson 4: Teach Python to Make Decisions 🧠

**Time:** 25–35 minutes · **Prerequisites:** Lessons 1–3

## 🎯 Mission

By the end of this lesson, you will be able to:

* Explain what a condition is.
* Use `if` to run code only when a condition is true.
* Use `else` to handle an alternative.
* Use `elif` to check multiple possibilities.
* Compare values using comparison operators.
* Combine conditions using `and`, `or`, and `not`.
* Find and fix common conditional-statement errors.

## 1. The Hook: Programs Can Make Decisions

Imagine a game that gives you access to a new level only when your score reaches 100.

How could a program decide whether you can enter?

It needs to check a condition.

```python
score = 120

if score >= 100:
    print("Level unlocked!")
```

**Output:**

```text
Level unlocked!
```

The program checks whether `score >= 100` is true. Because the score is 120, Python executes the indented line.

Now change the score:

```python
score = 60

if score >= 100:
    print("Level unlocked!")
```

This time, nothing is printed because the condition is false.

**The key idea:** A condition allows a program to choose whether a particular block of code should run.

## 2. Understand `if`

The basic structure looks like this:

```python
if condition:
    # Code that runs when the condition is True
```

Let's examine the important parts:

* `if` introduces a conditional statement.
* `condition` is an expression that evaluates to `True` or `False`.
* `:` marks the beginning of the block.
* Indentation identifies the statements belonging to that block.

Python commonly uses four spaces for each indentation level.

For example:

```python
temperature = 32

if temperature > 30:
    print("It's a hot day!")
    print("Stay hydrated.")

print("Weather report complete.")
```

**Output:**

```text
It's a hot day!
Stay hydrated.
Weather report complete.
```

Both indented statements belong to the `if` block. The final statement is outside the block, so it runs regardless of the condition.

### Experiment

Change `temperature` to `25` and run the program again.

What do you notice?

**Expected result:** The two messages inside the `if` block disappear, but `Weather report complete.` still prints.

## 3. Comparison Operators: Ask Questions with Python

Conditions often use comparison operators.

| Operator | Meaning                  | Example            |
| -------- | ------------------------ | ------------------ |
| `==`     | Equal to                 | `5 == 5` → `True`  |
| `!=`     | Not equal to             | `5 != 3` → `True`  |
| `>`      | Greater than             | `8 > 4` → `True`   |
| `<`      | Less than                | `2 < 7` → `True`   |
| `>=`     | Greater than or equal to | `5 >= 5` → `True`  |
| `<=`     | Less than or equal to    | `3 <= 2` → `False` |

Try running this:

```python
print(10 > 5)
print(10 == 5)
print(10 != 5)
print(7 <= 7)
```

**Output:**

```text
True
False
True
True
```

Python uses Boolean values: `True` and `False`.

### Important: `=` and `==` are different

```python
score = 10
```

This assigns the value `10` to `score`.

```python
print(score == 10)
```

This checks whether `score` equals `10` and prints `True`.

Confusing assignment (`=`) with comparison (`==`) is a common beginner mistake.

## 4. Give Python an Alternative with `else`

What if the score is too low to unlock the level? We can provide an alternative.

```python
score = 60

if score >= 100:
    print("Level unlocked!")
else:
    print("Keep playing to unlock the level.")
```

**Output:**

```text
Keep playing to unlock the level.
```

Python evaluates the condition:

* If it is `True`, the `if` block runs.
* If it is `False`, the `else` block runs.

Only one of these two blocks executes.

### Your prediction

What will happen if you change `score` to `150`?

**Answer:** Python prints `Level unlocked!` and skips the `else` block.

## 5. Check Multiple Possibilities with `elif`

Suppose a game awards medals based on a player's score:

* 90 or above: Gold
* 70–89: Silver
* 50–69: Bronze
* Below 50: Keep practising

You could write:

```python
score = 76

if score >= 90:
    print("Gold medal!")
elif score >= 70:
    print("Silver medal!")
elif score >= 50:
    print("Bronze medal!")
else:
    print("Keep practising!")
```

**Output:**

```text
Silver medal!
```

`elif` means “else if.” Python checks the conditions in order and runs the first matching block. It skips the remaining branches once a matching condition is found.

### Why does the order matter?

Consider this incorrect version:

```python
score = 95

if score >= 50:
    print("Bronze medal!")
elif score >= 70:
    print("Silver medal!")
elif score >= 90:
    print("Gold medal!")
else:
    print("Keep practising!")
```

This prints `Bronze medal!`, even though the score is 95.

Why? Because `score >= 50` is already true. Python never reaches the later conditions.

**Rule:** When checking ranges like these, put the highest threshold first when using `>=`.

## 6. Combine Conditions with `and`, `or`, and `not`

Sometimes one condition isn't enough.

### `and`: Both conditions must be true

```python
age = 17
has_ticket = True

if age >= 13 and has_ticket:
    print("You may enter the game zone.")
```

Both conditions are true, so the message appears.

### `or`: At least one condition must be true

```python
has_student_id = False
has_library_card = True

if has_student_id or has_library_card:
    print("You have an accepted card.")
```

The message appears because at least one condition is true.

### `not`: Reverse a Boolean value

```python
is_raining = False

if not is_raining:
    print("You can consider playing outside.")
```

Since `is_raining` is `False`, `not is_raining` is `True`.

Remember:

* `and`: all conditions must be true.
* `or`: at least one condition must be true.
* `not`: reverses a Boolean value.

## 7. A Practical Example: A Simple Study Planner

Let's create a program that suggests what to do based on the time available.

```python
study_minutes = 45

if study_minutes >= 120:
    print("You have time for a deep study session.")
elif study_minutes >= 60:
    print("Complete one focused study session.")
elif study_minutes >= 20:
    print("Review one concept and solve a few questions.")
else:
    print("Try a short revision session.")
```

**Output:**

```text
Review one concept and solve a few questions.
```

The program uses the value stored in `study_minutes` to choose an appropriate message.

Change the number to `150`, `75`, `30`, and `10`. Observe how the output changes.

This is the beginning of decision-making logic used in games, applications, and larger software systems.

## 8. Debugging Detective 🕵️

Find the problems in this code:

```python
score = 85

if score >= 70
print("You passed!")
```

There are two issues:

1. The condition is missing a colon (`:`).
2. The statement inside the `if` block needs indentation.

### Correct version

```python
score = 85

if score >= 70:
    print("You passed!")
```

**Output:**

```text
You passed!
```

### Another common mistake

```python
score = 85

if score = 70:
    print("You passed!")
```

This is invalid syntax because the condition uses `=` instead of `==`.

Correct it like this:

```python
if score == 70:
    print("Your score is exactly 70.")
```

Notice that `==` checks for equality. It does not assign a new value.

## 9. Coding Lab: Build a Score Classifier

Create a program that classifies a fictional player's score:

* 90 or above: Expert
* 70–89: Skilled
* 50–69: Beginner
* Below 50: Keep practising

### Starter code

```python
player_name = "Nova"
score = 78

print(f"Player: {player_name}")
print(f"Score: {score}")

# Write your conditional statements below.
```

**Your mission:**

1. Use `if`, `elif`, and `else`.
2. Print exactly one classification.
3. Test your program with scores of `95`, `78`, `55`, and `25`.

Try to solve it before checking the example.

<details>
<summary>Example solution</summary>

```python
player_name = "Nova"
score = 78

print(f"Player: {player_name}")
print(f"Score: {score}")

if score >= 90:
    print("Rank: Expert")
elif score >= 70:
    print("Rank: Skilled")
elif score >= 50:
    print("Rank: Beginner")
else:
    print("Rank: Keep practising")
```

For a score of `78`, the program prints `Rank: Skilled`.

</details>

## 10. Boss Challenge: Build a Login Decision Simulator 🏆

Create a fictional login simulator with these variables:

```python
username = "nova"
password_correct = True
account_active = True
```

Your program should:

1. Print a welcome message if the username is `"nova"`, the password is correct, and the account is active.
2. Print an account-disabled message if the account is inactive.
3. Print a login-failed message in other cases.

**Stretch challenge:** Test at least four different combinations of values.

Use only fictional data. This is a programming exercise, not a real authentication system.

## 11. Retrieval Review 🧠

Answer these questions before looking at the answer key.

**Question 1:** What does an `if` statement do?

**Question 2:** What is the difference between `=` and `==`?

**Question 3:** What will this program print?

```python
number = 12

if number > 10:
    print("A")
else:
    print("B")
```

**Question 4:** When does Python execute an `else` block?

**Question 5:** What is the purpose of `elif`?

**Question 6:** What does `and` require when combining two conditions?

**Question 7:** Find the mistake:

```python
temperature = 35

if temperature > 30:
print("Hot")
```

### Answer key

1. It executes a block of code when its condition is true.
2. `=` assigns a value; `==` compares two values for equality.
3. `A`.
4. When the preceding `if` and `elif` conditions are all false.
5. It checks another condition when earlier conditions were false.
6. Both conditions must be true.
7. The `print()` statement must be indented under the `if` statement.

## 12. Practice in VS Code

You will create a separate executable file for this lesson:

`lessons/00-zero-to-coder/lesson_04.py`

After saving this Markdown lesson, create `lesson_04.py` in the same folder as `lesson_01.py`, `lesson_02.py`, and `lesson_03.py`.

Use it to practise:

1. An `if` statement.
2. An `if` and `else` pair.
3. An `if`, `elif`, and `else` chain.
4. Comparison operators.
5. A combination of `and`, `or`, and `not`.
6. The score-classifier challenge.

Run your file and check that the output matches your predictions.

## 13. Completion Checklist ✅

Before moving on, make sure you can:

* [ ] Explain what a condition is.
* [ ] Write an `if` statement with correct indentation.
* [ ] Use `else` to handle an alternative.
* [ ] Use `elif` to check multiple possibilities.
* [ ] Use comparison operators correctly.
* [ ] Explain the difference between `=` and `==`.
* [ ] Combine conditions using `and`, `or`, and `not`.
* [ ] Debug missing colons, incorrect indentation, and invalid comparisons.

**Congratulations!** 🎉 You have taught Python to make decisions.

Your programs can now respond differently depending on their inputs and values.

**Next lesson:** Loops — teaching Python to repeat tasks using `for` and `while`.
