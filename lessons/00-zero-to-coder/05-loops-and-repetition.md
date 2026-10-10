# Lesson 5: Loops — Teach Python to Repeat 🔁

**Time:** 25–35 minutes · **Prerequisites:** Lessons 1–4

## 🎯 Mission

By the end of this lesson, you will be able to:

* Explain why loops are useful.
* Use a `for` loop to repeat instructions.
* Use `range()` to control how many times a loop runs.
* Understand loop variables and indentation.
* Use a `while` loop to repeat code while a condition remains true.
* Recognize and avoid infinite loops.
* Use `break` and `continue` in simple examples.

## 1. The Hook: Stop Repeating Yourself

Imagine you want Python to greet five people.

You could write:

```python
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
```

It works, but what if you want to print the message 100 times? Writing the same instruction 100 times would be tedious.

A **loop** lets you repeat instructions automatically.

```python
for number in range(5):
    print("Hello!")
```

**Output:**

```text
Hello!
Hello!
Hello!
Hello!
Hello!
```

Five lines of output, with only two lines of code.

**The key idea:** A loop repeats a block of code according to a set of rules.

## 2. Understand Your First `for` Loop

Look at this example:

```python
for number in range(5):
    print(number)
```

**Output:**

```text
0
1
2
3
4
```

Let's break it down:

* `for` begins the loop.
* `number` is the loop variable. It receives a new value during each iteration.
* `range(5)` produces the sequence of integers from `0` up to, but not including, `5`.
* `:` marks the start of the loop's block.
* The indented `print(number)` runs once for each value.

An **iteration** means one execution of the loop's body.

Here, the loop runs five times, with `number` taking the values `0`, `1`, `2`, `3`, and `4`.

### Try this

Change `range(5)` to `range(3)`.

Before running the program, predict how many numbers Python will print.

**Answer:** Three numbers: `0`, `1`, and `2`.

## 3. Master `range()`

The `range()` function is useful when you want to repeat something a specific number of times.

### A. One argument: `range(stop)`

```python
for number in range(4):
    print(number)
```

Output: `0`, `1`, `2`, `3`.

The starting value is `0`, and the stop value is excluded.

### B. Two arguments: `range(start, stop)`

```python
for number in range(2, 7):
    print(number)
```

Output:

```text
2
3
4
5
6
```

Python starts at `2` and stops before `7`.

### C. Three arguments: `range(start, stop, step)`

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

The third argument is the step: Python increases the number by `2` each time.

You can also count backwards:

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

The negative step makes the sequence decrease.

### Prediction challenge

What will this print?

```python
for number in range(1, 8, 3):
    print(number)
```

**Answer:** `1`, `4`, and `7`.

## 4. The Loop Variable Changes

A loop variable receives a different value during each iteration.

```python
for number in range(1, 4):
    print("Current number:", number)
```

Output:

```text
Current number: 1
Current number: 2
Current number: 3
```

You can use the loop variable in calculations too:

```python
for number in range(1, 6):
    print(number * 2)
```

Output:

```text
2
4
6
8
10
```

Python multiplies each value by `2` before printing it.

### Important distinction

The variable `number` is not automatically a special Python keyword. It is a name chosen by the programmer.

You could write:

```python
for student in range(3):
    print(student)
```

The loop works the same way. Clear variable names help people understand what a loop is doing.

## 5. Indentation Controls What Repeats

In Python, indentation tells us which statements belong inside a loop.

```python
for number in range(3):
    print("Inside the loop")
    print("Number:", number)

print("Loop finished!")
```

Output:

```text
Inside the loop
Number: 0
Inside the loop
Number: 1
Inside the loop
Number: 2
Loop finished!
```

Both indented statements run during every iteration.

The final statement is not indented, so it runs once after the loop finishes.

**Rule:** Statements inside the loop's indented block repeat. Statements after the block run when the loop has finished, unless the program exits earlier.

## 6. Use Loops with Variables

Loops become more powerful when combined with variables.

Suppose you collect stars in a game.

```python
stars = 0

for level in range(1, 4):
    stars = stars + 2
    print("Level:", level)
    print("Total stars:", stars)
```

Output:

```text
Level: 1
Total stars: 2
Level: 2
Total stars: 4
Level: 3
Total stars: 6
```

The variable `stars` keeps its value between iterations. Each time the loop runs, Python adds another `2`.

This pattern is called **accumulation**: repeatedly updating a variable to build a total.

You can also use the shorter assignment operator `+=`:

```python
stars = 0

for level in range(3):
    stars += 2

print(stars)
```

Output:

```text
6
```

`stars += 2` is equivalent to `stars = stars + 2`.

## 7. Meet the `while` Loop

A `for` loop is useful when iterating over a sequence or repeating a known number of times. A `while` loop repeats as long as its condition is true.

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Output:

```text
1
2
3
```

How does it work?

1. Python checks whether `count <= 3`.
2. If true, it prints `count`.
3. It increases `count` by `1`.
4. Python checks the condition again.
5. When `count` becomes `4`, the condition is false, and the loop stops.

### Why must the variable change?

Look at this example:

```python
count = 1

while count <= 3:
    print(count)
```

The value of `count` never changes. The condition stays true forever, so the loop continues indefinitely.

This is an **infinite loop**.

If you accidentally run an infinite loop in VS Code, stop the program using the terminal's interrupt shortcut, usually **Control + C**.

Before using a `while` loop, ask yourself:

* What condition keeps the loop running?
* What changes during each iteration?
* How will the condition eventually become false?

## 8. Choose Between `for` and `while`

Use a `for` loop when you want to iterate through a sequence or repeat a known number of times.

```python
for number in range(5):
    print(number)
```

Use a `while` loop when repetition depends on a condition.

```python
energy = 3

while energy > 0:
    print("Energy remaining:", energy)
    energy -= 1

print("Out of energy!")
```

Output:

```text
Energy remaining: 3
Energy remaining: 2
Energy remaining: 1
Out of energy!
```

Both loops are useful. The best choice depends on the problem you're solving.

## 9. Control a Loop with `break` and `continue`

Sometimes you need to change the normal flow of a loop.

### `break`: Stop the loop immediately

```python
for number in range(1, 6):
    if number == 4:
        break
    print(number)
```

Output:

```text
1
2
3
```

When `number` reaches `4`, `break` ends the loop immediately.

### `continue`: Skip the current iteration

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

When `number` is `3`, Python skips the remaining statements in that iteration and moves to the next one.

Remember:

* `break` ends the loop.
* `continue` skips the rest of the current iteration.

## 10. Debugging Detective 🕵️

Find the mistake in this program:

```python
for number in range(3):
print(number)
```

The `print()` statement is not indented. Python needs it inside the loop's block.

### Correct version

```python
for number in range(3):
    print(number)
```

Output:

```text
0
1
2
```

### Another challenge: Why doesn't this loop stop?

```python
count = 1

while count <= 5:
    print(count)
    count = count - 1
```

The variable decreases rather than increases. Starting at `1`, it becomes `0`, `-1`, `-2`, and so on. Every value remains less than or equal to `5`, so the condition never becomes false.

One correction is:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

**Debugging habit:** Check that the loop variable moves toward a state where the loop condition becomes false.

## 11. Coding Lab: Build a Multiplication Table

Create a program that prints the multiplication table for a number.

### Starter code

```python
number = 7

print(f"Multiplication table for {number}")

# Use a for loop to print the table from 1 to 10.
```

Your program should produce results such as:

```text
Multiplication table for 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

Try writing the loop yourself.

<details>
<summary>Example solution</summary>

```python
number = 7

print(f"Multiplication table for {number}")

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
```

`range(1, 11)` includes the numbers `1` through `10` because the stop value `11` is excluded.

</details>

## 12. Boss Challenge: Build a Countdown and Score Tracker 🏆

Create a small program that:

1. Prints a countdown from `5` to `1`.
2. Prints `"Launch!"` after the countdown.
3. Starts a score at `0`.
4. Adds `10` points during each of five rounds.
5. Prints the score after every round.
6. Prints the final score.

**Stretch challenges:**

* Let the user choose the starting number for the countdown.
* Use a `while` loop for the countdown.
* Skip one round using `continue`.
* Stop early using `break` when a chosen condition is met.

Try the basic challenge before attempting the stretch tasks.

## 13. Retrieval Review 🧠

Answer these questions without looking back at the lesson.

**Question 1:** Why are loops useful?

**Question 2:** What does this program print?

```python
for number in range(3):
    print(number)
```

**Question 3:** Why does `range(2, 6)` stop at `5` rather than `6`?

**Question 4:** What is the difference between a `for` loop and a `while` loop?

**Question 5:** What can cause an infinite loop?

**Question 6:** What is the difference between `break` and `continue`?

**Question 7:** Find the mistake:

```python
count = 1

while count <= 3:
    print(count)
```

### Answer key

1. Loops repeat instructions without requiring the programmer to write them repeatedly.
2. `0`, `1`, and `2`, each on a new line.
3. The stop value in `range()` is excluded.
4. A `for` loop iterates through a sequence or iterable; a `while` loop repeats while its condition is true.
5. A loop can continue indefinitely if its stopping condition never becomes false or if its logic never reaches a stopping point.
6. `break` ends the loop; `continue` skips the rest of the current iteration.
7. `count` never changes, so the condition stays true. Add `count = count + 1` inside the loop.

## 14. Practice in VS Code

Your practice file for this lesson will be:

`lessons/00-zero-to-coder/lesson_05.py`

Create this file inside the same folder as your previous practice files.

Use it to practise:

* A basic `for` loop.
* Different forms of `range()`.
* A loop that updates a variable.
* A `while` loop with a clear stopping condition.
* `break` and `continue`.
* The multiplication-table challenge.

Run the program and compare the actual output with your predictions.

## 15. Completion Checklist ✅

Before moving on, make sure you can:

* [ ] Explain what a loop does.
* [ ] Write a `for` loop using `range()`.
* [ ] Explain why the stop value in `range()` is excluded.
* [ ] Understand loop variables and indentation.
* [ ] Update a variable during a loop.
* [ ] Write a `while` loop with a stopping condition.
* [ ] Recognize the risk of an infinite loop.
* [ ] Use `break` and `continue`.
* [ ] Build a multiplication table using a loop.

**Congratulations!** 🎉 You've learned how to make Python repeat tasks efficiently.

You can now combine variables, conditions, and loops to build more useful programs.

**Next lesson:** Collections — storing and working with multiple values using lists.
