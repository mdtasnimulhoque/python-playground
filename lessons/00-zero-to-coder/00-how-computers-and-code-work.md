# Before You Code: How Computers and Programs Actually Work

**Python Playground · Level 0 · Lesson 0**

*No programming experience. No computer-science background. No prerequisites.*

**Estimated time:** 20–30 minutes
**Your mission:** Understand what a computer program is, how computers process instructions, and why programming languages exist.

---

## 1. Welcome. You belong here.

Maybe you've never written a line of code.

Maybe you have used a computer for years but never wondered how software works.

Maybe words such as *algorithm*, *memory*, *CPU*, and *programming language* seem confusing.

That's perfectly fine. You don't need to know any of them yet.

This course will explain each idea when you need it, give you examples to explore, and help you connect new concepts to things you already understand.

You are not expected to know everything immediately. You are here to learn.

**Let's begin with a question.**

When you open a calculator app, type `7 + 5`, and see `12`, how does the computer know what to do?

Does it understand mathematics the way a human does? Does somebody manually tell it the answer every time? Or is something else happening?

By the end of this lesson, you'll have a much clearer answer.

## 2. What is a computer?

A computer is an electronic machine that can process information by following instructions.

You probably already use computers in several forms:

* A laptop or desktop computer.
* A smartphone.
* A tablet.
* A smartwatch.
* Devices that control machines, vehicles, or household appliances.

These devices differ in size and capability, but they can all perform tasks by processing information.

Consider a simple calculator.

You provide two numbers and choose an operation. The calculator processes that information and displays a result.

This gives us our first important model:

**Input → Processing → Output**

Let's understand each part.

* **Input:** Information supplied to a system.
* **Processing:** Operations performed on that information.
* **Output:** The result produced by the system.

For a calculator:

| Stage      | Example             |
| ---------- | ------------------- |
| Input      | The numbers 7 and 5 |
| Processing | Addition            |
| Output     | The number 12       |

This pattern appears throughout computing.

When you search for a video, your search words are input. The software processes your request. The results shown on your screen are output.

When you edit a photograph, your adjustments are input. The application processes the image. The changed picture is output.

**Think about it:** Can you identify the input, processing, and output when you send someone a message?

*Remember:* Input–processing–output is a useful model, not a complete description of every computer system. Real systems can involve many stages, stored information, networks, and feedback.

## 3. Hardware and software: the physical machine and its instructions

A computer has physical components. These are called **hardware**.

Examples include:

* The keyboard.
* The screen.
* The processor.
* The memory chips.
* The storage drive.

You can physically touch hardware.

**Software** is different. It consists of programs and related information that tell a computer how to perform tasks.

Examples include:

* A calculator application.
* A web browser.
* A music player.
* A Python program you write yourself.

A useful analogy is a music player.

The physical device is hardware. The instructions and application that make it play music are software.

However, software isn't a physical object in the same sense as a keyboard. It is information represented and processed by the machine.

### Meet three important hardware concepts

**1. CPU — the central processing unit**

The CPU executes machine instructions and performs operations. It is often called the computer's processor.

**2. RAM — working memory**

RAM holds information and instructions that a computer is actively using. Its contents are generally temporary: they do not persist after power is removed.

**3. Storage**

Storage keeps information for later use. Your SSD or other storage device can hold documents, photographs, applications, and program files even when your computer is turned off.

An analogy can help:

Imagine working at a desk.

* The CPU is like a worker carrying out tasks.
* RAM is like the workspace holding the materials currently in use.
* Storage is like a cabinet holding things for later.

The analogy is imperfect, but it helps distinguish the roles.

### Check your understanding

Suppose you save a Python file, close your editor, and reopen it tomorrow.

Which component or concept is most relevant to keeping the file available?

A. RAM alone
B. Persistent storage
C. The keyboard

**Answer:** B. Persistent storage.

RAM helps the computer work with information, but persistent storage is what normally preserves your saved file.

## 4. What is a program?

A **program** is a set of instructions that a computer can execute to perform a task.

For example, imagine a program that calculates the total price of two items.

Its instructions might be:

1. Receive the first price.
2. Receive the second price.
3. Add the prices.
4. Display the total.

Notice something important: the computer doesn't need someone to explain the entire shopping experience. The program needs instructions precise enough to perform its assigned task.

Let's express the same idea without code:

> Take 8. Add 4. Show the result.

The expected result is 12.

That is the basic shape of a program: instructions that describe what should happen.

Programs can be tiny or enormous. A three-line script is a program. A web browser is also software built from many interacting parts.

## 5. What is an algorithm?

An **algorithm** is a defined sequence of steps for solving a problem or completing a task.

You already understand many algorithms without using that word.

Imagine making a cup of tea. Your process might be:

1. Heat water.
2. Prepare the cup.
3. Add tea.
4. Pour in the water.
5. Wait for the tea to steep.
6. Serve it.

That is an everyday example of an algorithm.

Now imagine explaining the same task to a machine. You would need to be much more precise about what the machine can do, what information it receives, and what happens when conditions change.

For example, what if there is no water? What if the water is not hot enough?

These questions lead to an important programming skill: thinking through the steps and possible situations before writing code.

An algorithm is the plan. A program is an implementation of instructions in a form the computer can execute.

They are related, but they are not the same thing.

### Mini-challenge: The morning routine

Write down five to eight steps for getting ready to leave home.

Then check your steps:

* Is the order sensible?
* Does each step describe a clear action?
* Is anything important missing?
* Would another person understand the instructions?

You have just practised the kind of structured thinking programmers use.

## 6. Why do programming languages exist?

Computers execute instructions represented in forms their hardware and software systems can process. At the lowest level, machine instructions are encoded as patterns of bits—binary digits, `0` and `1`.

Humans generally find raw machine instructions difficult to write and understand.

Programming languages give us a more practical way to express instructions.

Consider this Python statement:

```python
print("Hello, world!")
```

A person can read it and reasonably guess what it does: display a message.

Python is a programming language designed to let people express computational instructions using a readable syntax.

But writing Python code doesn't mean the CPU directly understands the English-like words in that statement.

Python's implementation processes the source code and executes the program through its runtime machinery. In the standard Python implementation, commonly called CPython, source code is compiled to Python bytecode, which is then executed by the Python virtual machine.

You don't need to memorize those technical details today. Just remember the distinction:

**You write Python instructions. Python's implementation processes them so the computer can carry out the requested work.**

We will explore how that process works in greater depth later.

### Your first tiny program

```python
print("Hello, world!")
```

Don't worry about memorizing the punctuation yet. For now, understand the purpose: this is a short instruction written in Python that displays a message.

You will learn what each part means in the next lesson.

## 7. What is coding?

**Coding** means writing instructions in a programming language.

**Programming** is broader. It includes understanding a problem, planning a solution, writing code, testing it, finding mistakes, improving the solution, and maintaining the program.

Imagine you want to build a program that helps students calculate their average marks.

You might need to:

1. Decide what information the program needs.
2. Determine how the average should be calculated.
3. Write the instructions.
4. Test the result with different numbers.
5. Fix mistakes.
6. Make the program easier to use.

Only part of that process is typing code.

This is why good programmers do more than memorize syntax. They learn how to reason about problems and check whether their solutions work.

## 8. Meet files, folders, and code editors

Before you start programming seriously, you need to understand three everyday tools.

**A file** stores information under a name. A photograph, a text document, and a Python program can all be stored as files.

**A folder** helps organize files and other folders.

**A code editor** is an application for writing and editing source code. Visual Studio Code, which you are using for this course, is one example.

A Python program is often saved in a file ending with `.py`.

For example:

`hello.py`

The `.py` ending tells people and software that the file contains Python source code. The filename alone does not execute the program.

Later, we'll learn how to run that file, understand the output, and interpret error messages.

You do not need to learn every computer tool at once. We will introduce each one when it becomes useful.

## 9. Your first mental model of programming

Let's bring the ideas together.

Imagine building a program that adds two numbers.

**Step 1 — Define the problem.**

We want to calculate the sum of two numbers.

**Step 2 — Plan the algorithm.**

1. Obtain two numbers.
2. Add them.
3. Display the result.

**Step 3 — Write the instructions in Python.**

```python
first_number = 7
second_number = 5

total = first_number + second_number

print(total)
```

Expected output:

```text
12
```

Don't worry if the equals signs, names, or parentheses are unfamiliar. We will explain them in later lessons.

For now, identify the big ideas:

* `first_number` and `second_number` give names to values.
* The `+` operator adds the numbers.
* `total` names the result.
* `print(total)` displays the result.

The important insight is that the program isn't magic. It follows instructions that you can inspect, reason about, and test.

## 10. Debugging: mistakes are part of the process

What happens if a program doesn't work as expected?

Programmers investigate. This process is called **debugging**.

Suppose the intended calculation is 7 + 5, but the program displays 75.

Perhaps the values were written as text:

```python
first_number = "7"
second_number = "5"

print(first_number + second_number)
```

In Python, the `+` operator joins these two strings, producing the text `75`. It does not perform numerical addition in this example.

The program followed the rules of the values it received. The programmer needs to understand those rules and choose the intended representation.

This is an important principle:

**When a program surprises you, examine the instructions and the information they use before assuming that the computer is behaving randomly.**

Errors are not proof that you cannot program. They are information you can use to investigate what happened.

## 11. Knowledge check

Try answering these questions without looking at the explanations above.

**Question 1.** What is the difference between hardware and software?

**Question 2.** In the calculator example, identify the input, processing, and output.

**Question 3.** What is an algorithm?

**Question 4.** How is an algorithm different from a program?

**Question 5.** Why do we use programming languages rather than writing every program directly as machine instructions?

**Question 6.** What is the purpose of debugging?

**Question 7.** A learner writes a program that produces an unexpected result. What should they do first?

### Answer key

1. Hardware refers to physical computer components; software consists of programs and related information used to perform tasks.
2. Input: the numbers and operation. Processing: the calculation. Output: the displayed result.
3. An algorithm is a defined sequence of steps for solving a problem or completing a task.
4. An algorithm describes the solution steps; a program implements instructions that a computer can execute.
5. Programming languages provide a more practical, readable way to express instructions.
6. Debugging is the process of investigating and correcting problems in a program.
7. Inspect the code, the information it uses, and the observed behaviour. Form a hypothesis, test it, and revise the solution.

If you struggled with a question, revisit the relevant section and explain the idea in your own words. Understanding matters more than finishing quickly.

## 12. Final mission: Explain a computer to a friend

Without copying the definitions above, try to explain these five ideas in simple language:

* Computer
* Hardware
* Software
* Algorithm
* Program

Then describe how a program could receive information, process it, and produce a result.

You can write your explanation, draw a diagram, or explain it aloud.

If you can explain these ideas clearly, you're ready to move forward.

## What comes next?

In **Lesson 1: Make Python Speak**, you'll run your first Python instructions and discover how to display text and calculate a result.

You now have the conceptual foundation to understand why you're doing it.

Welcome to Python Playground. Your journey starts here.
