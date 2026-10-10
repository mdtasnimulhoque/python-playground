# Lesson 1: Make Python Speak 🐍

**Python Playground · Level 0 · Lesson 1**

*No coding experience required. We'll explain every new idea.*

**Estimated time:** 25–40 minutes
**Your mission:** Write your first Python program, run it, predict its output, and explain what the code does.

---

## 1. Your First Conversation with a Computer

Welcome back!

In Lesson 0, you learned that a program is a set of instructions a computer can execute.

Today, you're going to write your first instructions in Python and watch them work.

Imagine you want your computer to display this message:

> Hello, future programmer!

How would you tell it to do that?

Python gives us a simple instruction:

```python
print("Hello, future programmer!")
```

That's a real Python program.

Let's understand how to run it, why it works, and how you can experiment with it yourself.

## 2. Meet Your First Python Instruction

Look carefully at this line:

```python
print("Hello, future programmer!")
```

It contains several pieces.

* `print` is the name of a built-in Python function.
* `(` and `)` are parentheses. They surround the information we're giving to the function.
* `"Hello, future programmer!"` is text surrounded by quotation marks.
* The quotation marks mark the beginning and end of the text. They are not included in the displayed message.

A **function** is a reusable piece of code that performs a particular task. You'll learn more about functions later.

For now, remember this:

**`print()` displays information when your Python program runs.**

Think of it as asking Python to show something on the screen.

### Predict Before You Run

What do you think this code displays?

```python
print("I am learning Python!")
```

A. `print("I am learning Python!")`

B. `I am learning Python!`

C. Nothing

Choose your answer before looking at the result.

**Expected output:**

```text
I am learning Python!
```

The correct answer is B. Python executes the instruction and displays the text inside the quotation marks, without the quotes themselves.

Predicting first helps you develop the ability to reason about code instead of merely copying it.

## 3. Set Up Your First Experiment in VS Code

You are using Visual Studio Code, so let's use it to run Python.

### Step 1 — Check Whether Python Is Installed

Python is the programming language. VS Code is the editor you use to write code. Having VS Code installed does not automatically guarantee that Python itself is installed.

If you haven't installed Python, visit the official Python website:

https://www.python.org/downloads/macos/

Download and install a current stable Python 3 release suitable for your Mac.

If you're unsure whether Python is already installed, open the VS Code terminal and try:

```bash
python3 --version
```

If Python is installed, you should see a version number. If the command fails, check your Python installation before continuing.

### Step 2 — Install the Python Extension

In VS Code:

1. Click the Extensions icon in the left sidebar.
2. Search for **Python**.
3. Choose the Python extension published by Microsoft.
4. Click **Install** if it isn't already installed.

The extension helps VS Code recognize Python files, select a Python interpreter, and run your programs.

### Step 3 — Open Your Practice File

Your Python Playground project already has a practice file:

`lessons/00-zero-to-coder/lesson_01.py`

In VS Code:

1. Find `lessons` in the Explorer sidebar.
2. Open the `00-zero-to-coder` folder.
3. Click `lesson_01.py`.
4. Replace the contents of that file with the example below.

```python
print("Hello, future programmer!")
```

Save the file by pressing **⌘ + S**.

**Why use this file?** Keeping your practice program in the existing course structure helps you find your work and avoids creating duplicate files.

Remember the distinction:

* `01-make-python-speak.md` contains the written lesson.
* `lesson_01.py` contains executable Python code.

### Step 4 — Run Your Program

With `lesson_01.py` open:

1. Look for the **Run Python File** play button near the upper-right corner of the editor.
2. Click it.
3. If VS Code asks you to select a Python interpreter, choose an installed Python 3 interpreter.
4. Look at the output in the integrated terminal panel at the bottom of VS Code.

You do not need to open the separate Terminal application on your Mac.

You should see:

```text
Hello, future programmer!
```

Congratulations! You've written and run your first Python program.

If the Run button is missing, the interpreter isn't available, or an error appears, don't panic. Check that the file is saved with the `.py` ending and that Python and the Microsoft Python extension are installed.

## 4. Give Python Three Instructions

One instruction is a program. Multiple instructions can work together to accomplish a task.

Replace the contents of your practice file with this:

```python
print("Hello, future programmer!")
print("I am learning to give computers instructions.")
print(2 + 3)
```

Save the file and run it again.

**Expected output:**

```text
Hello, future programmer!
I am learning to give computers instructions.
5
```

Three lines of code produced three lines of output.

Let's investigate why.

### Instruction 1

```python
print("Hello, future programmer!")
```

Python displays a message.

### Instruction 2

```python
print("I am learning to give computers instructions.")
```

Python displays another message.

### Instruction 3

```python
print(2 + 3)
```

Python calculates `2 + 3`, which equals `5`, and displays the result.

Notice that Python follows the instructions in order, from the first line to the next.

**Experiment:** Swap the first and second lines. Run the program again. What changes? What stays the same?

## 5. Text Versus Mathematics

This is one of your first important discoveries.

Compare these two instructions:

```python
print(10 + 10)
```

```python
print("10 + 10")
```

They look similar, but Python interprets them differently.

The first contains a mathematical expression. Python calculates the sum and displays `20`.

The second contains text. Python displays the characters `10 + 10` without calculating anything.

| Code               | What Python does                  | Output    |
| ------------------ | --------------------------------- | --------- |
| `print(10)`        | Displays a number                 | `10`      |
| `print(10 + 10)`   | Calculates a sum                  | `20`      |
| `print("10")`      | Displays text                     | `10`      |
| `print("10 + 10")` | Displays text without calculating | `10 + 10` |

The outputs in the first and third rows look identical, but the underlying values are different: one is a number, and the other is text.

In Python, text is commonly represented using a **string**. A string is a sequence of characters.

Strings can contain letters, spaces, punctuation, and even digits.

Try running all four examples:

```python
print("Python is a language")
print(10)
print(10 + 10)
print("10 + 10")
```

**Your mission:** Before running the code, write down what you think each line will display. Then run it and compare.

If you predict something incorrectly, investigate why. That's how programmers build reliable mental models.

## 6. What Happens When You Make a Mistake?

Programmers make mistakes. Learning to investigate them is part of programming.

Consider this code:

```python
print("Hello, Python!)
```

Can you spot the problem?

The text starts with a quotation mark, but it doesn't have a matching closing quotation mark.

Try running it in your practice file.

Python will report an error instead of displaying the intended message.

Now fix the code:

```python
print("Hello, Python!")
```

Run it again. It should work.

### Debugging Detective 🔎

Debugging means investigating why a program isn't working as intended and correcting the problem.

When you encounter an error:

1. Read the error message.
2. Look at the indicated line of code.
3. Check the punctuation and spelling.
4. Form a guess about what went wrong.
5. Change something and run the program again.

You won't always understand an error message immediately. That's normal. With practice, you'll learn to recognize common problems.

**Remember:** An error is information about what happened, not a judgment of your ability.

## 7. Your First Coding Laboratory

Now it's your turn to experiment.

Open `lessons/00-zero-to-coder/lesson_01.py` and write this program:

```python
print("My name is Alex.")
print("I am learning Python.")
print(8 + 4)
print(15 - 6)
print(3 * 4)
print(20 / 5)
```

Save and run it.

**Expected output:**

```text
My name is Alex.
I am learning Python.
12
9
12
4.0
```

The final result is `4.0`, rather than `4`, because Python's `/` operator performs division that produces a floating-point result.

A **floating-point number** is a representation used for numbers that can include a fractional part.

You don't need to memorize every detail today. Just notice that different operators perform different calculations.

Try these operators yourself:

* `+` adds.
* `-` subtracts.
* `*` multiplies.
* `/` divides.

### Experiment: Change the Program

Make at least three changes:

1. Replace the name Alex with a name of your choice.
2. Change `8 + 4` to a calculation of your choice.
3. Add another `print()` instruction.

Before running the program, predict the new output.

Then run it and check your prediction.

## 8. Boss Challenge: Build a Tiny Introduction

Now create a program of your own.

Your program must:

1. Display a greeting.
2. Display something you are curious about.
3. Calculate and display the result of a mathematical expression.
4. Display one more message of your choice.

For example, your program might look like this:

```python
print("Hello, world!")
print("I am curious about space.")
print(25 + 17)
print("This is my first program!")
```

**Expected output:**

```text
Hello, world!
I am curious about space.
42
This is my first program!
```

Don't simply copy the example. Personalize it.

### Extra Challenge

Make Python display a question and then an answer on the next line.

Hint: You can use two separate `print()` instructions.

For example, one instruction could display a question about a calculation, and the next could display its answer.

## 9. Quick Retrieval Check

Close or minimize the lesson and answer these questions from memory.

**Question 1:** What does `print()` do?

**Question 2:** What is a string?

**Question 3:** What is the difference between `print(2 + 3)` and `print("2 + 3")`?

**Question 4:** What happens when Python executes multiple `print()` instructions in sequence?

**Question 5:** What should you do when a program produces an unexpected error?

**Question 6:** Why is predicting the output before running code useful?

### Answer Key

1. It displays information.
2. A string is a sequence of characters used to represent text.
3. The first calculates the sum and displays `5`. The second displays the text `2 + 3`.
4. Python executes the instructions in order, so each `print()` displays its result in sequence.
5. Read the error, inspect the code, identify a possible cause, make a correction, and test again.
6. Prediction helps you reason about code and compare your understanding with what actually happens.

If you missed a question, return to the relevant example and explain the idea in your own words.

## 10. Completion Check

Before moving on, confirm that you can:

* [ ] Create and save a `.py` file.
* [ ] Run Python code using VS Code.
* [ ] Explain what `print()` does.
* [ ] Predict the output of a short program.
* [ ] Distinguish text from a mathematical expression.
* [ ] Identify and fix a missing quotation mark.
* [ ] Write a short program of your own.

You don't have to memorize everything. You do need to be able to experiment and explain the main ideas.

If running Python didn't work on your computer, you can still study the examples, but return to the setup steps before continuing with the hands-on exercises.

## What Comes Next?

In **Lesson 2: Values and Experiments**, you'll explore the different kinds of information Python can work with, investigate how Python interprets values, and learn to test your predictions systematically.

For now, take a moment to appreciate what you've done.

You didn't just read about programming. You wrote instructions, ran a program, observed its behaviour, and began learning how to investigate mistakes.

That's the beginning of programming.

**Welcome to Python Playground. Keep experimenting!**
