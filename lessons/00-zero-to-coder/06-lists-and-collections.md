# Lesson 6: Lists — Store Many Values Together 📚

**Time:** 30–40 minutes · **Prerequisites:** Lessons 1–5

## 🎯 Mission

By the end of this lesson, you will be able to:

* Explain why lists are useful.
* Create lists containing multiple values.
* Access items using indexes.
* Update, add, and remove items.
* Use `len()` to count items.
* Loop through a list.
* Recognize common list errors.

## 1. The Hook: One Name, Many Values

Imagine you want to store your favourite subjects.

You could create separate variables:

```python
subject1 = "Python"
subject2 = "Mathematics"
subject3 = "Physics"
```

That works, but what if you have 50 subjects or 500 names?

Python provides a better solution: **lists**.

```python
subjects = ["Python", "Mathematics", "Physics"]

print(subjects)
```

**Output:**

```text
['Python', 'Mathematics', 'Physics']
```

A list stores multiple items in a single collection.

In this example:

* `subjects` is the variable name.
* Square brackets `[]` define the list.
* Commas separate the items.
* Each subject is a string.

Lists are useful for storing things such as student names, game scores, tasks, products, and much more.

## 2. Access Items with Indexes

Every item in a Python list has an index: its position number.

**Important:** Python indexes begin at `0`, not `1`.

```python
subjects = ["Python", "Mathematics", "Physics"]

print(subjects[0])
print(subjects[1])
print(subjects[2])
```

**Output:**

```text
Python
Mathematics
Physics
```

Here's how the indexes work:

| Index | Value           |
| ----: | --------------- |
|   `0` | `"Python"`      |
|   `1` | `"Mathematics"` |
|   `2` | `"Physics"`     |

The first item is at index `0`, the second at index `1`, and the third at index `2`.

### Try this

```python
colors = ["red", "green", "blue", "yellow"]

print(colors[0])
print(colors[3])
```

**Output:**

```text
red
yellow
```

### Access items from the end

Python also supports negative indexes.

```python
colors = ["red", "green", "blue", "yellow"]

print(colors[-1])
print(colors[-2])
```

**Output:**

```text
yellow
blue
```

* `-1` refers to the last item.
* `-2` refers to the second-to-last item.

This is especially useful when you don't know how long a list is.

## 3. Update an Item

Lists are mutable, which means you can change their contents after creating them.

```python
subjects = ["Python", "Mathematics", "Physics"]

subjects[1] = "Biology"

print(subjects)
```

**Output:**

```text
['Python', 'Biology', 'Physics']
```

The item at index `1` changed from `"Mathematics"` to `"Biology"`.

### Experiment

Change the first subject to `"Computer Science"` and print the list again.

Remember: the first item has index `0`.

## 4. Add Items to a List

Python provides several ways to add items.

### A. `append()` — Add one item at the end

```python
subjects = ["Python", "Mathematics"]

subjects.append("Physics")

print(subjects)
```

**Output:**

```text
['Python', 'Mathematics', 'Physics']
```

`append()` adds one item to the end of the list.

### B. `insert()` — Add an item at a specific position

```python
subjects = ["Python", "Physics"]

subjects.insert(1, "Mathematics")

print(subjects)
```

**Output:**

```text
['Python', 'Mathematics', 'Physics']
```

The first argument specifies the index where the new item should be inserted.

### C. `extend()` — Add multiple items

```python
subjects = ["Python", "Mathematics"]

subjects.extend(["Physics", "Biology"])

print(subjects)
```

**Output:**

```text
['Python', 'Mathematics', 'Physics', 'Biology']
```

Use `extend()` when you want to add the elements of another iterable to the end of a list.

## 5. Remove Items from a List

You can also remove items.

### A. `remove()` — Remove a matching value

```python
subjects = ["Python", "Mathematics", "Physics"]

subjects.remove("Mathematics")

print(subjects)
```

**Output:**

```text
['Python', 'Physics']
```

`remove()` removes the first matching value. If the value isn't present, Python raises a `ValueError`.

### B. `pop()` — Remove an item by index

```python
subjects = ["Python", "Mathematics", "Physics"]

removed_subject = subjects.pop(1)

print(removed_subject)
print(subjects)
```

**Output:**

```text
Mathematics
['Python', 'Physics']
```

`pop(1)` removes the item at index `1` and returns that item.

Calling `pop()` without an index removes and returns the last item.

### C. `del` — Delete an item by index

```python
subjects = ["Python", "Mathematics", "Physics"]

del subjects[0]

print(subjects)
```

**Output:**

```text
['Mathematics', 'Physics']
```

Use `del` when you want to delete an item by its position.

## 6. Count Items with `len()`

The built-in `len()` function tells you how many items are in a list.

```python
subjects = ["Python", "Mathematics", "Physics"]

print(len(subjects))
```

**Output:**

```text
3
```

Let's combine this with a list update:

```python
tasks = ["Study Python", "Practise maths"]

print("Tasks:", len(tasks))

tasks.append("Read a book")

print("Updated tasks:", len(tasks))
```

**Output:**

```text
Tasks: 2
Updated tasks: 3
```

`len()` counts the number of items, not the number of characters inside each item.

## 7. Loop Through a List

You already learned loops in Lesson 5. Now you can use them to process lists.

```python
subjects = ["Python", "Mathematics", "Physics"]

for subject in subjects:
    print(subject)
```

**Output:**

```text
Python
Mathematics
Physics
```

Python takes each item from the list, one at a time, and assigns it to `subject`.

### Display numbered items

You can use `enumerate()` to access both an item's index and its value.

```python
subjects = ["Python", "Mathematics", "Physics"]

for index, subject in enumerate(subjects):
    print(index, subject)
```

**Output:**

```text
0 Python
1 Mathematics
2 Physics
```

To start numbering from `1`, use `enumerate(subjects, start=1)`.

```python
for number, subject in enumerate(subjects, start=1):
    print(f"{number}. {subject}")
```

**Output:**

```text
1. Python
2. Mathematics
3. Physics
```

## 8. Lists Can Store Different Types

A Python list doesn't have to contain only strings.

```python
student = ["Mira", 17, 92.5, True]

print(student)
```

This list contains a string, an integer, a float, and a Boolean.

Python permits mixed types in a list. In real projects, lists often contain items of the same general kind, but mixed lists are useful in some situations.

You can also create an empty list:

```python
tasks = []

tasks.append("Learn Python")
tasks.append("Practise loops")

print(tasks)
```

**Output:**

```text
['Learn Python', 'Practise loops']
```

Starting with an empty list and adding items as you go is a common programming pattern.

## 9. Debugging Detective 🕵️

### Mistake 1: Using an index that doesn't exist

```python
subjects = ["Python", "Physics"]

print(subjects[2])
```

This raises an `IndexError` because the list has indexes `0` and `1`, but no index `2`.

**Fix:** Use a valid index, or check the list's length before accessing an item.

```python
subjects = ["Python", "Physics"]

print(subjects[1])
```

### Mistake 2: Using parentheses instead of square brackets

```python
subjects = ["Python", "Physics"]

print(subjects(0))
```

This attempts to call the list like a function and raises a `TypeError`.

**Fix:**

```python
print(subjects[0])
```

Use square brackets to access an item by index.

### Mistake 3: Trying to remove an item that isn't present

```python
subjects = ["Python", "Physics"]

subjects.remove("Biology")
```

This raises a `ValueError` because `"Biology"` is not in the list.

One safe approach is:

```python
if "Biology" in subjects:
    subjects.remove("Biology")
```

The `in` operator checks whether an item exists in a collection.

## 10. Coding Lab: Build a Subject Manager

Create a program that manages a list of subjects.

### Starter code

```python
subjects = ["Python", "Mathematics", "Physics"]

print("My subjects:")
# Print each subject on its own line.

# Add "Biology" to the list.

# Replace "Physics" with "Computer Science".

# Print the final list and its length.
```

Your program should:

1. Display the original subjects.
2. Add `"Biology"`.
3. Replace `"Physics"` with `"Computer Science"`.
4. Print the updated list.
5. Print the number of items in the list.

Try solving it before checking the example.

<details>
<summary>Example solution</summary>

```python
subjects = ["Python", "Mathematics", "Physics"]

print("My subjects:")

for subject in subjects:
    print(subject)

subjects.append("Biology")
subjects[2] = "Computer Science"

print("\nUpdated subjects:")

for subject in subjects:
    print(subject)

print("Total subjects:", len(subjects))
```

The final list contains four items:

`['Python', 'Mathematics', 'Computer Science', 'Biology']`

</details>

## 11. Boss Challenge: Build a Mini Task Manager 🏆

Create a simple task manager using a list.

Start with an empty list:

```python
tasks = []
```

Your program should:

1. Add three tasks using `append()`.
2. Print all tasks with numbers starting from `1`.
3. Remove one completed task.
4. Print the updated task list.
5. Display the total number of remaining tasks.

**Stretch challenge:** Ask the user to enter a new task using `input()` and append it to the list.

You don't need to build a full application yet. Focus on understanding how the list changes as your program runs.

## 12. Retrieval Review 🧠

Answer these questions without looking back at the lesson.

**Question 1:** What problem do lists solve?

**Question 2:** What does this program print?

```python
colors = ["red", "green", "blue"]
print(colors[1])
```

**Question 3:** What is the difference between `append()` and `extend()`?

**Question 4:** What does `len()` return when used with a list?

**Question 5:** What is the difference between `remove()` and `pop()`?

**Question 6:** Why does `subjects[3]` raise an `IndexError` for this list?

```python
subjects = ["Python", "Math", "Physics"]
```

**Question 7:** What does this program print?

```python
numbers = [2, 4, 6]
numbers.append(8)
print(len(numbers))
```

### Answer key

1. Lists store multiple items under one variable name.
2. `green`.
3. `append()` adds one item; `extend()` adds the elements of an iterable.
4. The number of items in the list.
5. `remove()` removes the first matching value; `pop()` removes and returns an item by index, or the last item when no index is provided.
6. The list has indexes `0`, `1`, and `2`, but no index `3`.
7. `4`.

## 13. Practice in VS Code

Your executable practice file for this lesson will be:

`lessons/00-zero-to-coder/lesson_06.py`

Create it in the same folder as your previous practice files.

Use it to practise:

* Creating a list.
* Accessing items by index.
* Updating an item.
* Adding and removing items.
* Using `len()`.
* Looping through a list.
* Building the subject manager.

Run the file and compare the output with your predictions.

## 14. Completion Checklist ✅

Before moving on, make sure you can:

* [ ] Create a list using square brackets.
* [ ] Explain why indexing starts at `0`.
* [ ] Access items using positive and negative indexes.
* [ ] Update an existing item.
* [ ] Add items with `append()`, `insert()`, and `extend()`.
* [ ] Remove items with `remove()`, `pop()`, and `del`.
* [ ] Count items with `len()`.
* [ ] Use a loop to process a list.
* [ ] Recognize and fix common list errors.

**Congratulations!** 🎉 You can now store, organize, and process multiple values in a single collection.

**Next lesson:** Strings — working with text, characters, formatting, and useful string operations.
