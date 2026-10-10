# Lesson 8: Dictionaries — Organize Information with Keys and Values 🗂️

**Level:** 0 — Zero to Coder
**Prerequisites:** Lessons 1–7
**Estimated time:** 60–90 minutes
**Practice file:** `lessons/00-zero-to-coder/lesson_08.py`

---

## 1. What Is a Dictionary?

Imagine you want to store information about a student.

You could use separate variables:

```python
name = "Tasnimul"
age = 20
subject = "Python"
score = 95
```

But as your program grows, managing many separate variables becomes difficult.

A **dictionary** lets you group related information together using **key-value pairs**.

```python
student = {
    "name": "Tasnimul",
    "age": 20,
    "subject": "Python",
    "score": 95
}

print(student)
```

Output:

```text
{'name': 'Tasnimul', 'age': 20, 'subject': 'Python', 'score': 95}
```

A dictionary has two important parts:

* **Key:** The label used to identify information, such as `"name"`.
* **Value:** The information associated with that key, such as `"Tasnimul"`.

Think of a dictionary as a collection of labeled boxes. Each key tells you what kind of information a box contains.

### Dictionary syntax

```python
dictionary_name = {
    "key": value,
    "another_key": another_value
}
```

Notice the curly braces `{}` and the colon `:` between each key and value.

Keys are usually strings, although Python also supports certain other immutable types as keys.

---

## 2. Accessing Values

To retrieve a value, place its key inside square brackets.

```python
student = {
    "name": "Tasnimul",
    "subject": "Python",
    "score": 95
}

print(student["name"])
print(student["subject"])
print(student["score"])
```

Output:

```text
Tasnimul
Python
95
```

Unlike lists, which use numerical indexes, dictionaries use keys to find their values.

Compare:

```python
subjects = ["Python", "Physics"]
print(subjects[0])

student = {"name": "Tasnimul"}
print(student["name"])
```

Output:

```text
Python
Tasnimul
```

### What if a key doesn't exist?

```python
student = {"name": "Tasnimul"}

print(student["age"])
```

This raises a `KeyError` because `"age"` is not in the dictionary.

A safer approach is `.get()`.

```python
student = {"name": "Tasnimul"}

print(student.get("name"))
print(student.get("age"))
print(student.get("age", "Not provided"))
```

Output:

```text
Tasnimul
None
Not provided
```

**Remember:**

* `student["age"]` raises an error if the key is missing.
* `student.get("age")` returns `None` if the key is missing.
* `student.get("age", 20)` returns `20` as the fallback value if the key is missing.

Use `.get()` when a missing key is an expected possibility.

---

## 3. Adding New Information

You can add a new key-value pair by assigning a value to a new key.

```python
student = {
    "name": "Tasnimul",
    "subject": "Python"
}

student["age"] = 20
student["city"] = "Malda"

print(student)
```

Output:

```text
{'name': 'Tasnimul', 'subject': 'Python', 'age': 20, 'city': 'Malda'}
```

Python adds each new key to the dictionary.

You can also add several entries with `.update()`.

```python
student.update({
    "score": 95,
    "level": "Beginner"
})

print(student)
```

`.update()` adds new keys and changes existing keys when their names match.

---

## 4. Updating Existing Values

Assigning a value to an existing key replaces its previous value.

```python
student = {
    "name": "Tasnimul",
    "score": 75
}

student["score"] = 95

print(student)
```

Output:

```text
{'name': 'Tasnimul', 'score': 95}
```

You can also perform calculations:

```python
student["score"] = student["score"] + 3

print(student["score"])
```

Output:

```text
98
```

This is useful for updating scores, counters, settings, and other information.

---

## 5. Removing Information

Python offers several ways to remove dictionary entries.

### Using `pop()`

```python
student = {
    "name": "Tasnimul",
    "score": 95,
    "city": "Malda"
}

removed_city = student.pop("city")

print("Removed:", removed_city)
print(student)
```

Output:

```text
Removed: Malda
{'name': 'Tasnimul', 'score': 95}
```

`pop()` removes the key and returns its value.

### Using `del`

```python
student = {
    "name": "Tasnimul",
    "score": 95
}

del student["score"]

print(student)
```

Output:

```text
{'name': 'Tasnimul'}
```

### Using `clear()`

```python
student = {"name": "Tasnimul", "score": 95}

student.clear()

print(student)
```

Output:

```text
{}
```

`clear()` removes every entry but leaves the dictionary itself available.

Be careful: `pop()` and `del` raise a `KeyError` if the specified key is absent, unless you handle that possibility. `pop()` can accept a default value to avoid this.

```python
student = {"name": "Tasnimul"}

removed = student.pop("city", "No city stored")

print(removed)
```

---

## 6. Finding Out What's Inside

Python provides several useful dictionary operations.

```python
student = {
    "name": "Tasnimul",
    "subject": "Python",
    "score": 95
}

print(len(student))
print(student.keys())
print(student.values())
print(student.items())
```

Output:

```text
3
dict_keys(['name', 'subject', 'score'])
dict_values(['Tasnimul', 'Python', 95])
dict_items([('name', 'Tasnimul'), ('subject', 'Python'), ('score', 95)])
```

| Operation          | Purpose                              |
| ------------------ | ------------------------------------ |
| `len(student)`     | Counts the number of key-value pairs |
| `student.keys()`   | Provides the dictionary's keys       |
| `student.values()` | Provides its values                  |
| `student.items()`  | Provides key-value pairs             |

These methods return dictionary view objects, which reflect the dictionary's current contents.

You can convert a view to a list if you need a list:

```python
keys = list(student.keys())
print(keys)
```

Output:

```text
['name', 'subject', 'score']
```

---

## 7. Looping Through a Dictionary

Loops let you process dictionary information automatically.

### Loop through keys

```python
student = {
    "name": "Tasnimul",
    "subject": "Python",
    "score": 95
}

for key in student:
    print(key)
```

Output:

```text
name
subject
score
```

By default, looping through a dictionary gives you its keys.

### Loop through values

```python
for value in student.values():
    print(value)
```

Output:

```text
Tasnimul
Python
95
```

### Loop through keys and values

The `.items()` method gives you both.

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Output:

```text
name: Tasnimul
subject: Python
score: 95
```

This pattern is particularly useful when displaying records or processing structured data.

---

## 8. Checking Whether a Key Exists

Use the `in` operator to check whether a dictionary contains a key.

```python
student = {
    "name": "Tasnimul",
    "score": 95
}

print("name" in student)
print("age" in student)
```

Output:

```text
True
False
```

Important: checking with `in` tests for keys, not values.

```python
student = {
    "name": "Tasnimul",
    "score": 95
}

print("name" in student)
print("Tasnimul" in student)
print("Tasnimul" in student.values())
```

Output:

```text
True
False
True
```

Use `.values()` when you want to check for a value.

---

## 9. Dictionaries Can Store Different Data Types

Dictionary values can contain strings, integers, floats, Booleans, lists, and even other dictionaries.

```python
student = {
    "name": "Tasnimul",
    "age": 20,
    "average_score": 91.5,
    "is_learning": True,
    "subjects": ["Python", "Physics", "Mathematics"]
}

print(student["name"])
print(student["average_score"])
print(student["subjects"])
print(student["subjects"][0])
```

Output:

```text
Tasnimul
91.5
['Python', 'Physics', 'Mathematics']
Python
```

Notice the last line: you can access a list stored inside a dictionary by first selecting the key and then using a list index.

---

## 10. Nested Dictionaries

A dictionary can contain another dictionary. This is called a **nested dictionary**.

```python
students = {
    "student_1": {
        "name": "Tasnimul",
        "score": 95
    },
    "student_2": {
        "name": "Amina",
        "score": 89
    }
}

print(students["student_1"]["name"])
print(students["student_2"]["score"])
```

Output:

```text
Tasnimul
89
```

This is useful when managing multiple records.

You can update nested information too:

```python
students["student_1"]["score"] = 98

print(students["student_1"]["score"])
```

Output:

```text
98
```

---

## 11. A Practical Example: Subject Score Tracker

Let's build a small score tracker.

```python
scores = {
    "Python": 95,
    "Mathematics": 88,
    "Physics": 91
}

print("Current scores:")

for subject, score in scores.items():
    print(f"{subject}: {score}")

scores["Mathematics"] = 92
scores["Computer Science"] = 97

print("\nUpdated scores:")

for subject, score in scores.items():
    print(f"{subject}: {score}")

print("\nNumber of subjects:", len(scores))
```

The program stores scores, updates one value, adds a new subject, and displays the results.

### Your experiment

Change the scores, add two subjects, and remove one subject. Predict the output before you run the program.

---

## 12. Common Mistakes and Debugging

### Mistake 1: Forgetting quotation marks around string keys

Incorrect:

```python
student = {"name": "Tasnimul"}
print(student[name])
```

Python interprets `name` as a variable, which may cause a `NameError`.

Correct:

```python
print(student["name"])
```

### Mistake 2: Accessing a missing key

Incorrect when the key might be absent:

```python
print(student["age"])
```

Safer:

```python
print(student.get("age", "Age not available"))
```

### Mistake 3: Using a list as a key

Incorrect:

```python
data = {["a", "b"]: 10}
```

Lists are mutable and cannot be dictionary keys.

Correct:

```python
data = {("a", "b"): 10}
```

Tuples can be dictionary keys when all their elements are hashable.

### Mistake 4: Confusing keys and values

```python
student = {"name": "Tasnimul"}

print("Tasnimul" in student)
```

This returns `False` because `"Tasnimul"` is a value, not a key.

Correct:

```python
print("Tasnimul" in student.values())
```

### Mistake 5: Repeating a key

```python
student = {
    "score": 80,
    "score": 95
}

print(student["score"])
```

Output:

```text
95
```

Dictionary keys must be unique. If you repeat a key in a dictionary literal, the later value replaces the earlier one.

---

## 13. Coding Lab: Personal Profile Manager 🧑‍💻

Build a program that stores your profile in a dictionary.

Include these fields:

* Name
* Location
* Favourite subject
* Hobby
* Current programming language
* Learning goal

Your program should:

1. Create the dictionary.
2. Print the profile one field at a time.
3. Add a new field called `"current_project"`.
4. Update your learning goal.
5. Check whether `"hobby"` exists.
6. Display the total number of fields.
7. Loop through every key-value pair and display it neatly.

**Bonus:** Ask the user for a new learning goal using `input()` and update the dictionary with their answer.

---

## 14. Boss Challenge: Mini Student Database 🏆

Create a dictionary containing at least three students. Each student should have a name and a score.

Example structure:

```python
students = {
    "student_1": {"name": "Tasnimul", "score": 95},
    "student_2": {"name": "Amina", "score": 89},
    "student_3": {"name": "Rahul", "score": 92}
}
```

Your program should:

* Display every student's name and score.
* Calculate the average score.
* Identify the student with the highest score.
* Add a new student.
* Update one student's score.
* Check whether a particular student ID exists.

**Hint:** Start with a loop. You can calculate a total by adding each score to a variable initialized to `0`. Divide the total by the number of students to find the average.

Try to solve this independently before looking for help.

---

## 15. Retrieval Practice: Test Yourself

Answer these questions without looking back.

1. What is a dictionary?
2. What is the difference between a key and a value?
3. How do you access the value associated with `"name"`?
4. What happens when you access a missing key using square brackets?
5. What does `.get()` do?
6. How do you add a new key-value pair?
7. What is the difference between `pop()` and `clear()`?
8. How do `.keys()`, `.values()`, and `.items()` differ?
9. What does `in` check when used directly with a dictionary?
10. What is a nested dictionary?
11. Why can't a list be used as a dictionary key?
12. What happens when the same key appears twice in a dictionary literal?

---

## 16. Completion Checklist

Before moving to Lesson 9, make sure you can:

* [ ] Explain key-value pairs.
* [ ] Create a dictionary.
* [ ] Retrieve values using keys.
* [ ] Handle missing keys with `.get()`.
* [ ] Add and update entries.
* [ ] Remove entries safely.
* [ ] Use `len()`, `.keys()`, `.values()`, and `.items()`.
* [ ] Loop through dictionaries.
* [ ] Check whether keys and values exist.
* [ ] Work with lists inside dictionaries.
* [ ] Read and update nested dictionaries.
* [ ] Build the Personal Profile Manager.
* [ ] Attempt the Mini Student Database challenge.

**Next lesson:** Tuples and Sets — Understand Ordered Records and Unique Values.

Keep experimenting: predict the output, run the program, compare the result, and explain why it happened.
