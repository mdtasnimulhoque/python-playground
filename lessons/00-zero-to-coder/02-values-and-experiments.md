# Lesson 2: Values and Experiments 🔬

**Python Playground · Level 0 · Lesson 2**

*Prerequisites: Lesson 0 — How Computers and Code Work; Lesson 1 — Make Python Speak*

**Estimated time:** 30–45 minutes

**Your mission:** Understand what values are, distinguish numbers from text, explore four basic Python data types, and learn how to investigate code through experiments.

---

## 1. Welcome to the Experiment Lab

Imagine you're building a simple student calculator.

It needs to work with information such as:

* A student's name.
* Their examination marks.
* Their average score.
* Whether they passed a particular test.

These pieces of information are not all the same kind of thing.

A name is text. A mark is a number. A pass-or-fail result can be represented by a true-or-false value.

Python needs to represent these differences so that it can work with information appropriately.

Today, you'll discover how.

### Your first prediction

Before learning anything new, look at this code:

```python
print("Python is fun!")
print(10 + 5)
```

**Predict:** What do you think Python will display?

Write down your answer before reading further.

Expected output:

```text
Python is fun!
15
```

The first instruction displays text. The second calculates a result and displays it.

You've already used Python to display information. Now it's time to understand the information itself.

---

## 2. What Is a Value?

A **value** is a piece of information that a program can work with.

Look at these examples:

```python
"Hello"
25
3.14
True
```

Each represents a value, but each has a different meaning.

* `"Hello"` represents text.
* `25` represents a whole number.
* `3.14` represents a number with a fractional part.
* `True` represents a truth value.

You have already encountered values in Lesson 1. Now we'll investigate them more carefully.

### Meet the difference between code and output

Consider this instruction:

```python
print("Hello")
```

You write the quotation marks in your code, but the output is:

```text
Hello
```

The quotation marks are not displayed. They help Python recognize the characters inside them as a string.

A **string** is a sequence of characters used to represent text.

### Experiment 1: Predict, run, explain

Look at the following code:

```python
print(25)
print("Hello")
print(3.14)
print(True)
```

Before running it, predict the output.

Expected output:

```text
25
Hello
3.14
True
```

Python can display values of different kinds. But how does it distinguish them?

That brings us to data types.

---

## 3. Meet Four Basic Data Types

A **data type** describes the kind of value something represents. It also influences which operations make sense for that value.

Python has many data types. Let's begin with four.

### Type 1: Integers (`int`)

An **integer** is a whole number without a fractional part.

Examples:

```python
7
0
-12
250
```

Python calls this type `int`.

Try:

```python
print(7)
print(7 + 3)
print(10 - 4)
print(6 * 2)
```

Expected output:

```text
7
10
6
12
```

The operators are:

* `+` means addition.
* `-` means subtraction.
* `*` means multiplication.

Python calculates the arithmetic expressions and displays their results.

**Your turn:** Change `7 + 3` to `20 + 5`. Predict the result before running the program.

### Type 2: Floating-Point Numbers (`float`)

A **floating-point number** represents a number that can have a fractional part.

Examples:

```python
3.14
2.5
-0.75
```

Python calls this type `float`.

Try:

```python
print(3.14)
print(2.5 + 1.5)
print(10 / 4)
```

Expected output:

```text
3.14
4.0
2.5
```

Notice that `2.5 + 1.5` produces `4.0`, not `4`.

The result is displayed as a floating-point number.

In Python, ordinary division using `/` produces a floating-point result, even when the answer is a whole number.

For example:

```python
print(10 / 2)
```

Output:

```text
5.0
```

#### A small computer surprise

Try:

```python
print(0.1 + 0.2)
```

You may see:

```text
0.30000000000000004
```

Why doesn't Python display exactly `0.3`?

Computers represent floating-point numbers using a binary system. Many decimal fractions cannot be represented exactly in that system, so tiny rounding differences can occur.

You don't need to master the mathematics yet. Just remember that calculations involving decimal numbers can sometimes produce surprising results.

### Type 3: Strings (`str`)

A **string** is a sequence of characters used to represent text.

Examples:

```python
"Python"
"Hello, world!"
"123"
""
```

Python calls this type `str`.

The final example, `""`, is an **empty string**: text containing zero characters.

Strings can contain letters, spaces, punctuation, and digits. Digits inside a string do not automatically make it a number.

Try:

```python
print("Python")
print("123")
print("Hello" + " world")
```

Expected output:

```text
Python
123
Hello world
```

The `+` operator joins the two strings in the final example.

This operation is called **concatenation**.

Notice the space before `world` in `" world"`. Without it, Python would join the words as `Helloworld`.

### Type 4: Booleans (`bool`)

A **Boolean** represents one of two truth values.

In Python, they are written exactly like this:

```python
True
False
```

Python calls this type `bool`.

Try:

```python
print(True)
print(False)
print(5 > 3)
print(5 < 3)
```

Expected output:

```text
True
False
True
False
```

The expressions `5 > 3` and `5 < 3` compare numbers.

* `>` means greater than.
* `<` means less than.

Python evaluates each comparison and produces a Boolean result.

Because 5 is greater than 3, the expression `5 > 3` evaluates to `True`.

Booleans become especially useful when programs need to make decisions. We'll explore that in a later lesson.

### Quick comparison

| Data type      | Python name | Example   | Meaning                                |
| -------------- | ----------- | --------- | -------------------------------------- |
| Integer        | `int`       | `25`      | Whole number                           |
| Floating-point | `float`     | `3.14`    | Number that can have a fractional part |
| String         | `str`       | `"Hello"` | Text                                   |
| Boolean        | `bool`      | `True`    | Truth value                            |

Don't try to memorize this table mechanically. Focus on understanding what each value represents.

---

## 4. The Quotation-Mark Experiment

This is one of the most important experiments in your early Python journey.

Study these instructions:

```python
print(25)
print("25")
print(25 + 5)
print("25" + "5")
```

Before running them, predict the output of each line.

Expected output:

```text
25
25
30
255
```

Why do the last two lines behave differently?

### Experiment A: Numbers

```python
print(25 + 5)
```

Python treats both values as integers.

The `+` operator performs addition:

$$
25 + 5 = 30
$$

The output is:

```text
30
```

### Experiment B: Strings

```python
print("25" + "5")
```

Python treats both values as strings.

The `+` operator joins their text:

```text
255
```

Python isn't calculating twenty-five plus five here. It's putting the characters together.

### Why the first two lines look identical

Compare:

```python
print(25)
print("25")
```

Both display:

```text
25
25
```

However, the values are different:

* `25` is an integer.
* `"25"` is a string.

The quotation marks help Python recognize the second value as text. The marks themselves aren't shown by `print()`.

**Important lesson:** Two values can look identical in the output but represent different kinds of information.

That difference affects what Python can do with them.

### Your experiment

Predict the output before running this code:

```python
print(8 + 2)
print("8" + "2")
print(8 * 2)
print("8" * 2)
```

Expected output:

```text
10
82
16
88
```

Why does `"8" * 2` produce `88`?

Python allows a string to be repeated using multiplication by an integer. It repeats the text twice rather than performing numerical multiplication.

This is another example of how an operation's behavior can depend on the type of value involved.

---

## 5. Let Python Tell You a Value's Type

Instead of guessing a value's type, you can ask Python.

Meet the built-in function `type()`.

For now, think of `type()` as a tool that tells you what kind of value Python is working with.

Try this:

```python
print(type(25))
print(type(3.14))
print(type("Hello"))
print(type(True))
```

Expected output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

The output contains some extra punctuation. For now, focus on the names:

* `int`: integer.
* `float`: floating-point number.
* `str`: string.
* `bool`: Boolean.

The expression `type(25)` asks Python for the type of the value `25`. Wrapping it in `print()` displays the answer.

Now investigate these:

```python
print(type("25"))
print(type(25 + 5))
print(type("25" + "5"))
```

Expected output:

```text
<class 'str'>
<class 'int'>
<class 'str'>
```

Why?

* `"25"` is a string.
* `25 + 5` evaluates to the integer `30`.
* `"25" + "5"` evaluates to the string `"255"`.

The type depends on the value Python is working with—not just what the value looks like on your screen.

### Experiment: Investigate before guessing

Try:

```python
print(type(10 / 2))
print(type(10 // 2))
print(type(10 == 2))
```

Expected output:

```text
<class 'float'>
<class 'int'>
<class 'bool'>
```

Here's what happened:

* `/` performs ordinary division and returns a floating-point result.
* `//` performs floor division. For these positive integers, the result is the whole number `5`.
* `==` checks whether two values are equal and produces a Boolean result.

Be careful: `=` and `==` have different purposes. You'll learn more about that distinction in upcoming lessons.

---

## 6. A Common Beginner Mistake

Consider this code:

```python
age = "18"
print(age + 2)
```

What do you think will happen?

You might expect Python to display `20`.

But if you run it, Python raises a `TypeError` because it cannot use `+` to add a string and an integer in this example.

Why?

* `"18"` is a string.
* `2` is an integer.
* Python doesn't automatically convert the string `"18"` into a number for this addition.

A `TypeError` means an operation was used with a type of value that doesn't support that operation in the way requested.

### How can we fix it?

If `age` is supposed to represent a number, write:

```python
age = 18
print(age + 2)
```

Expected output:

```text
20
```

We'll explore the meaning of `age = 18` and how names such as `age` work in Lesson 3.

For now, remember:

**If two values look similar, don't assume they have the same type. Check how Python represents them.**

### Debugging habit

When an error occurs:

1. Read the error message.
2. Find the line of code where the problem occurs.
3. Inspect the values and their types.
4. Form a possible explanation.
5. Change the code and run it again.

Errors aren't evidence that you can't program. They're information that can help you understand what happened.

---

## 7. Build Your Experiment Notebook

Now it's time to leave the reading and work directly with Python.

### Step 1: Open your practice file

Your project already includes this file:

`lessons/00-zero-to-coder/lesson_02.py`

In VS Code:

1. Find `lessons` in the Explorer sidebar.
2. Open `00-zero-to-coder`.
3. Click `lesson_02.py`.
4. Replace its contents with the experiment below.

Keep this Python file separate from the Markdown lesson you're reading.

### Step 2: Enter the experiment

Type or paste this code into `lesson_02.py`:

```python
print(type(42))
print(type(4.2))
print(type("42"))
print(type(False))

print(8 + 2)
print("8" + "2")
```

Save the file using **⌘ + S**, then run it in VS Code.

### Step 3: Check your output

You should see:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
10
82
```

If your output differs, don't panic. Check that the code matches the example, save your file, and run it again.

### Step 4: Experiment independently

Now change the values.

For example:

```python
print(type(100))
print(type(100.0))
print(type("100"))
```

Predict the output first.

Expected output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
```

The visible number is similar in each case, but the types differ.

Next, try:

```python
print("Hello" + " Python")
print(10 + 5)
print("10" + "5")
```

Expected output:

```text
Hello Python
15
105
```

### The Experiment Rule

For every experiment:

1. **Predict:** What do you think will happen?
2. **Run:** Execute the code.
3. **Compare:** Was your prediction correct?
4. **Explain:** Why did Python produce that result?
5. **Modify:** Change one thing and test again.

Being wrong in a prediction isn't failure. It's an opportunity to discover how Python works.

Change one thing at a time so you can understand which change caused which result.

---

## 8. The Debugging Challenge

A learner wants to calculate the total of two numbers.

They write:

```python
print("12" + "8")
```

The program displays:

```text
128
```

The learner expected `20`.

### Your mission

Before looking at the solution:

1. Explain why the program displays `128`.
2. Rewrite the instruction so that Python calculates `20`.
3. Use `type()` to verify the types of the two values in your corrected expression.

### Solution

```python
print(12 + 8)
print(type(12))
print(type(8))
```

Expected output:

```text
20
<class 'int'>
<class 'int'>
```

The original program joined two strings. The corrected program adds two integers.

This wasn't a random computer mistake. Python followed the rules for the values it received.

**Programmer's lesson:** Understanding the input values often helps you understand the output.

---

## 9. Boss Challenge: Build a Tiny Information Display

Now combine what you've learned.

Write a program that displays:

1. A name of your choice as text.
2. A whole number of your choice.
3. A decimal number.
4. A Boolean value.
5. The type of each value.

For example:

```python
print("Alex")
print(18)
print(3.5)
print(True)

print(type("Alex"))
print(type(18))
print(type(3.5))
print(type(True))
```

Expected output:

```text
Alex
18
3.5
True
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Before running your program, predict what it will display.

Then run it and compare your prediction with the actual output.

You can use different values. The goal is to understand the differences, not copy the example exactly.

### Extra challenge

Can you display a number as text and then display it as a number?

Try:

```python
print("18")
print(18)

print(type("18"))
print(type(18))
```

Explain why the displayed characters look similar while the types differ.

---

## 10. Quick Retrieval Check

Answer these questions without looking back at the lesson.

**Question 1:** What is a value?

**Question 2:** What is the difference between `25` and `"25"`?

**Question 3:** What is the difference between `int` and `float`?

**Question 4:** What does `type()` tell you?

**Question 5:** Why does `"8" + "2"` produce `82` rather than `10`?

**Question 6:** What are the two Boolean values in Python?

**Question 7:** Why does `10 / 2` produce `5.0` rather than `5`?

**Question 8:** What is a `TypeError`?

**Question 9:** What should you do when a program produces an unexpected result?

### Answer Key

1. A piece of information a program can work with.
2. `25` is an integer; `"25"` is a string.
3. An integer is a whole number without a fractional part; a floating-point number can represent a fractional part.
4. It tells you the type of a value.
5. Both values are strings, so `+` joins their text rather than adding the numbers.
6. `True` and `False`.
7. Python's ordinary division operator `/` returns a floating-point result.
8. An error that occurs when an operation is used with a type of value that doesn't support that operation in the requested way.
9. Inspect the code and the values involved, form a hypothesis, test it, and learn from the result.

If you get something wrong, revisit the relevant example and try explaining it in your own words.

---

## 11. Completion Checklist

Before moving on, make sure you can:

* [ ] Explain what a value is.
* [ ] Recognize integers, floating-point numbers, strings, and Booleans.
* [ ] Explain why `25` and `"25"` are different.
* [ ] Predict the results of basic arithmetic and string concatenation.
* [ ] Explain why `"8" * 2` produces `88`.
* [ ] Use `type()` to investigate a value.
* [ ] Explain why ordinary division produces a floating-point result.
* [ ] Explain and fix the string-versus-number mistake.
* [ ] Read a simple error and investigate its cause.
* [ ] Write a small program that explores different data types.

You don't need to memorize every example. Focus on understanding what Python is doing and being able to investigate it yourself.

If one item is difficult, repeat the relevant experiment before moving on.

---

## What Comes Next?

In **Lesson 3: Variables Are Labels**, you'll learn how to give values meaningful names, reuse information, and understand how a program can remember and update values while it runs.

You'll build on today's knowledge to write programs that work with information more flexibly.

You're not just learning Python syntax. You're learning how to think, test, investigate, and reason like a programmer.

**Keep experimenting. Every question you investigate is another step toward understanding how code works.**
