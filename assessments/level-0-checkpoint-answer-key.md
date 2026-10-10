# Python Playground — Level 0 Checkpoint Test: Answer Key

**Version:** Draft 2
**Coverage:** Lessons 0–3
**Total:** 30 points
**Audience:** Instructors, course maintainers, and grading systems

> **Keep this file private when publishing the course online.** Do not place the answer key in a publicly accessible learner-facing assessment page or reveal it before a learner submits the test.

Equivalent answers are acceptable when they demonstrate the required understanding. The examples below are sample answers, not the only acceptable wording or code.

---

## Part A — Understand the concepts (6 points)

### 1. Input, processing, and output — 2 points

**Expected answer:**

* **Input:** The two numbers supplied to the program.
* **Processing:** Adding the two numbers together.
* **Output:** Displaying the resulting sum.

**Marking guide:**

Award credit for correctly identifying the three stages and their roles. Accept equivalent wording. A response that merely lists the terms without explaining them should not receive full credit.

### 2. Numbers and strings — 2 points

**Expected answer:**

`25` is an integer (`int`). `"25"` is a string (`str`) containing text characters.

Although printing either value can display `25`, their types differ. For example, `25 + 1` produces `26`, while `"25" + "1"` produces `"251"`.

**Marking guide:**

* 1 point: Correctly identifies `25` as `int` and `"25"` as `str`.
* 1 point: Gives a valid explanation of how their behavior differs.

### 3. Why use variables? — 2 points

**Expected answer:**

A variable name is associated with a value. It lets a program refer to that value by name and use it in calculations or other operations.

For example:

```python
score = 10
print(score)
```

The program uses the name `score` to refer to the value `10`.

**Marking guide:**

* 1 point: Explains that a variable name refers to or is associated with a value.
* 1 point: Gives a relevant example or explains how naming a value makes a program easier to write or understand.

---

## Part B — Predict the output (8 points)

### 4. Messages and calculations — 2 points

**Expected output:**

```text
Hello!
7
```

**Marking guide:**

* 1 point: Correctly predicts `Hello!`.
* 1 point: Correctly predicts `7`.

### 5. Numbers versus text — 2 points

**Expected output:**

```text
8
62
```

**Explanation:**

`6 + 2` adds two integers, producing `8`. `"6" + "2"` joins two strings, producing `"62"`, which is displayed without quotation marks.

**Marking guide:**

* 1 point: Correctly predicts `8`.
* 1 point: Correctly predicts `62`.

### 6. Updating a variable — 2 points

**Expected output:**

```text
9
```

**Explanation:**

First, `score` is assigned the value `5`. Next, Python evaluates `score + 4`, which is `9`, and assigns that result back to `score`.

**Marking guide:**

* 1 point: Correct output.
* 1 point: Correctly explains the calculation and reassignment.

### 7. Checking types — 2 points

**Expected output:**

```text
<class 'float'>
<class 'str'>
```

**Explanation:**

In Python 3, `/` produces a floating-point result, even when dividing one number by another produces a whole number. The quoted value `"9"` is a string.

**Marking guide:**

* 1 point: Correctly identifies the first output as `<class 'float'>`.
* 1 point: Correctly identifies the second output as `<class 'str'>`.

---

## Part C — Find and fix errors (8 points)

### 8. Fix a syntax error — 2 points

**One valid answer:**

```python
print("Learning Python!")
```

The original line is missing a closing quotation mark for the string.

**Marking guide:**

* 1 point: Correctly fixes the quotation marks.
* 1 point: Provides a valid line that displays the requested message.

Accept other syntactically correct solutions that display exactly `Learning Python!`.

### 9. Fix an unexpected result — 3 points

**One valid answer:**

```python
print(12 + 8)
```

**Expected output:**

```text
20
```

**Explanation:**

In the original program, `"12"` and `"8"` are strings. The `+` operator concatenates them, producing the string `"128"`. Removing the quotation marks makes both values integers, so `+` performs numerical addition.

**Marking guide:**

* 1 point: Provides working code that displays the numerical result `20`.
* 1 point: Identifies the original values as strings.
* 1 point: Explains the difference between string concatenation and numerical addition.

### 10. Correct a variable name — 3 points

**One valid answer:**

```python
student_name = "Mina"
print(student_name)
```

**Expected output:**

```text
Mina
```

**Explanation:**

Python treats `studentname` and `student_name` as different names. The name used in `print()` must match the name that was assigned.

**Marking guide:**

* 2 points: Provides a working correction that displays `Mina`.
* 1 point: Explains that the two variable names do not match.

---

## Part D — Write your own code (8 points)

### 11. Store and display information — 4 points

**Sample solution:**

```python
name = "Alex"
age = 18

print(name)
print(age)
```

**Expected output:**

```text
Alex
18
```

Learners may use any name and any appropriate whole-number age.

**Marking guide:**

* 1 point: Assigns a string value to `name`.
* 1 point: Assigns an integer value to `age`.
* 1 point: Correctly displays `name`.
* 1 point: Correctly displays `age`.

Accept different valid approaches that satisfy the requirements. Award partial credit when the intended solution is clear but contains a minor syntax mistake.

### 12. Add numbers and inspect the result — 4 points

**Sample solution:**

```python
first_number = 12
second_number = 8

total = first_number + second_number

print(total)
print(type(total))
```

**Expected output:**

```text
20
<class 'int'>
```

Other integer values and sensible variable names are acceptable.

**Marking guide:**

* 1 point: Stores an integer in the first variable.
* 1 point: Stores an integer in the second variable.
* 1 point: Correctly calculates and displays their sum.
* 1 point: Uses `type()` to display the type of the sum.

Accept equivalent working code, including code that passes the addition directly to `print()` rather than using a separate `total` variable.

---

## General grading principles

1. **Reward understanding.** Accept equivalent explanations that demonstrate the intended concept.
2. **Award partial credit.** A minor syntax error should not automatically erase credit for an otherwise correct approach.
3. **Separate output from reasoning.** A correct predicted result does not automatically earn full explanation points.
4. **Do not penalize harmless style differences.** Different variable names, spacing, or valid coding approaches are acceptable unless the question specifies otherwise.
5. **Give useful feedback.** When a learner misses a question, identify the relevant concept and recommend the lesson to revisit.
6. **Allow practice and retries.** Learners should be able to learn from mistakes and try again in practice mode.

## Final score verification

| Section                     | Maximum points |
| --------------------------- | -------------: |
| Part A — Concepts           |              6 |
| Part B — Predict the output |              8 |
| Part C — Debugging          |              8 |
| Part D — Write code         |              8 |
| **Total**                   |         **30** |

The marking guide is designed to support consistent grading while allowing learners to express their understanding in different ways.
