# Python Playground — Level 0 Checkpoint Test

**Version:** Draft 2
**Coverage:** Lessons 0–3
**Suggested time:** 25–35 minutes
**Total:** 30 points

## Purpose

This checkpoint checks whether you understand the foundations of Python: how programs work, how to display output, how values and types behave, and how to use variables.

This is a learning checkpoint, not a judgment of your ability.

## Instructions

1. Try every question independently before opening your lesson notes.
2. For prediction questions, write your predicted output before running the code.
3. For coding questions, write code that solves the stated problem.
4. Explain your reasoning wherever requested.
5. If you are unsure, make your best attempt. An honest attempt helps you identify what to practice next.

If you use a Python interpreter to check your predictions, do so only after recording them.

---

## Part A — Understand the concepts (6 points)

### 1. Input, processing, and output — 2 points

A program asks the user for two numbers, adds them, and displays their total.

Identify:

* **Input:** What information does the program receive?
* **Processing:** What does the program do with that information?
* **Output:** What does the program display?

**Scoring:** Award up to 2 points for correctly identifying all three stages and their roles.

### 2. Numbers and strings — 2 points

Explain the difference between the Python values `25` and `"25"`.

Your answer should identify their types and explain one way their behavior differs.

**Scoring:**

* 1 point for identifying the correct types.
* 1 point for explaining a meaningful difference in behavior.

### 3. Why use variables? — 2 points

In your own words, explain what a variable is useful for.

Give one simple example of a value you might store in a variable and explain why giving it a name is helpful.

**Scoring:**

* 1 point for explaining that a variable name refers to a value.
* 1 point for a relevant example or explanation of its usefulness.

---

## Part B — Predict the output (8 points)

Write the exact output in the correct order. Do not include the Python code itself in your answer.

### 4. Messages and calculations — 2 points

```python
print("Hello!")
print(4 + 3)
```

What will the program display?

**Scoring:** 1 point per correct output line.

### 5. Numbers versus text — 2 points

```python
print(6 + 2)
print("6" + "2")
```

What will the program display?

**Scoring:** 1 point per correct output line.

### 6. Updating a variable — 2 points

```python
score = 5
score = score + 4
print(score)
```

What will the program display? Briefly explain how the value changes.

**Scoring:** 1 point for the correct output and 1 point for a correct explanation.

### 7. Checking types — 2 points

```python
print(type(9 / 3))
print(type("9"))
```

What will the program display?

**Hint:** In Python 3, the `/` operator produces a `float`, even when the result is a whole number.

**Scoring:** 1 point for each correct output line.

---

## Part C — Find and fix errors (8 points)

For each question, write the corrected code. Explain the cause of the error or unexpected result where requested.

### 8. Fix a syntax error — 2 points

This code contains a syntax error:

```python
print("Learning Python!)
```

Rewrite the line so that it correctly displays:

`Learning Python!`

**Scoring:**

* 1 point for correcting the quotation marks.
* 1 point for providing a valid line that displays the required message.

### 9. Fix an unexpected result — 3 points

The programmer wants to calculate the total of twelve plus eight.

```python
print("12" + "8")
```

Rewrite the code so it displays the numerical result `20`.

Then explain why the original code produces a different result.

**Scoring:**

* 1 point for code that displays `20` as a numerical result.
* 2 points for explaining that the quoted values are strings and that `+` joins strings rather than adding their numerical values.

### 10. Correct a variable name — 3 points

Find and correct the error:

```python
student_name = "Mina"
print(studentname)
```

Write a corrected version that displays `Mina`, then explain what caused the problem.

**Scoring:**

* 2 points for a working correction.
* 1 point for explaining that the name used in `print()` does not match the assigned variable name.

---

## Part D — Write your own code (8 points)

Write Python code for each task. Your code should be readable and should run without errors.

### 11. Store and display information — 4 points

Write a short Python program that:

1. Stores a person's name in a variable called `name`.
2. Stores a whole-number age in a variable called `age`.
3. Prints both values.

Choose your own example name and age.

**Scoring:**

* 1 point for correctly creating `name`.
* 1 point for correctly creating `age` as an integer.
* 1 point for displaying the name.
* 1 point for displaying the age.

### 12. Add numbers and inspect the result — 4 points

Write a program that:

1. Stores two integers in separate variables.
2. Calculates and prints their sum.
3. Uses `type()` to print the type of the sum.

Choose your own integers.

**Scoring:**

* 1 point for storing the first integer.
* 1 point for storing the second integer.
* 1 point for correctly printing their sum.
* 1 point for printing the type of the sum.

---

## Self-review — Ungraded

After finishing, answer these questions honestly:

* Which question felt easiest?
* Which question was hardest?
* Which answer did you guess?
* What topic should you practice next?

Review your mistakes even if you achieved a high score. A correct answer is most valuable when you understand why it is correct.

## Score guide

* **27–30:** Strong grasp of these foundational concepts. Try extending your skills with new examples.
* **23–26:** Good progress. Review the questions you missed.
* **18–22:** You have a foundation to build on. Practice the weaker topics before moving forward.
* **Below 18:** Revisit Lessons 0–3, experiment with the examples, and try again.

Your score is feedback about what to learn next. It is not a measure of your potential.

**Answer key:** `level-0-checkpoint-answer-key.md`

Try the test before opening the answer key.
