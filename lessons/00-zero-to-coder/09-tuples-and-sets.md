# Lesson 9: Tuples and Sets — Fixed Collections and Unique Values 🔗

**Level:** 0 — Zero to Coder
**Prerequisites:** Lessons 1–8
**Estimated time:** 60–90 minutes
**Practice file:** `lessons/00-zero-to-coder/lesson_09.py`

---

## 1. Why Do We Need More Collection Types?

So far, you've learned about lists and dictionaries.

A **list** stores an ordered collection of items:

```python
subjects = ["Python", "Physics", "Mathematics"]
```

A **dictionary** stores information using key-value pairs:

```python
student = {
    "name": "Tasnimul",
    "score": 95
}
```

Python also provides **tuples** and **sets**. Each collection type is useful for different situations.

* A tuple groups values in a particular order.
* A set stores unique values and supports mathematical set operations.

Let's explore both.

---

# Part A: Tuples

## 2. What Is a Tuple?

A **tuple** is an ordered collection of items. Tuples are immutable, meaning you cannot replace, add, or remove individual items after the tuple has been created.

```python
coordinates = (10, 20)

print(coordinates)
print(type(coordinates))
```

Output:

```text
(10, 20)
<class 'tuple'>
```

Tuples use parentheses `()` by convention.

You can store different types of values in one tuple:

```python
student = ("Tasnimul", 20, "Python", 95)

print(student)
```

Output:

```text
('Tasnimul', 20, 'Python', 95)
```

A tuple can contain strings, integers, floats, Booleans, and other objects.

---

## 3. Accessing Tuple Items

Like lists and strings, tuples use indexes that begin at `0`.

```python
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[0])
print(languages[1])
print(languages[-1])
```

Output:

```text
Python
Java
JavaScript
```

You can also use slicing.

```python
print(languages[0:2])
print(languages[1:])
print(languages[:3])
```

Output:

```text
('Python', 'Java')
('Java', 'C++', 'JavaScript')
('Python', 'Java', 'C++')
```

The starting index is included, while the ending index is excluded.

---

## 4. Why Are Tuples Immutable?

Consider this example:

```python
coordinates = (10, 20)

coordinates[0] = 50
```

Python raises a `TypeError` because tuple items cannot be reassigned.

When would this be useful?

Imagine storing a fixed coordinate, a date, or a record that should not accidentally have its individual fields replaced.

```python
location = (25.01, 88.14)

latitude = location[0]
longitude = location[1]

print("Latitude:", latitude)
print("Longitude:", longitude)
```

Tuples communicate that the collection is intended to stay fixed. They are not automatically better than lists in every situation; choose based on what your program needs.

**Important:** A tuple can contain a mutable object, such as a list. That object may still be changed, even though the tuple's references to its items cannot be reassigned.

---

## 5. The One-Item Tuple Surprise

Look carefully at these examples.

```python
single_value = (10,)
not_a_tuple = (10)

print(type(single_value))
print(type(not_a_tuple))
```

Output:

```text
<class 'tuple'>
<class 'int'>
```

The comma creates the one-item tuple. Parentheses alone do not.

You can also create a tuple without parentheses:

```python
coordinates = 10, 20

print(coordinates)
print(type(coordinates))
```

Output:

```text
(10, 20)
<class 'tuple'>
```

For clarity, using parentheses is often a good choice.

---

## 6. Useful Tuple Operations

### Count the items

```python
scores = (95, 88, 95, 76, 95)

print(len(scores))
```

Output:

```text
5
```

### Count how many times a value occurs

```python
print(scores.count(95))
```

Output:

```text
3
```

### Find the first index of a value

```python
print(scores.index(88))
```

Output:

```text
1
```

`.index()` raises a `ValueError` if the requested value isn't present.

### Check whether an item exists

```python
languages = ("Python", "Java", "C++")

print("Python" in languages)
print("Ruby" in languages)
```

Output:

```text
True
False
```

---

## 7. Tuple Unpacking

**Unpacking** lets you assign tuple items to separate variables.

```python
student = ("Tasnimul", 95, "Python")

name, score, subject = student

print(name)
print(score)
print(subject)
```

Output:

```text
Tasnimul
95
Python
```

The number of variables must normally match the number of items.

```python
coordinates = (10, 20)

x, y = coordinates

print("x:", x)
print("y:", y)
```

Output:

```text
x: 10
y: 20
```

You can use the same technique to swap two variables:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

Python evaluates the right-hand side and assigns the results to the variables on the left.

---

# Part B: Sets

## 8. What Is a Set?

A **set** is a collection of unique elements.

```python
subjects = {"Python", "Physics", "Mathematics"}

print(subjects)
print(type(subjects))
```

Output order may vary:

```text
{'Python', 'Physics', 'Mathematics'}
<class 'set'>
```

Sets are useful when you want to remove duplicates or determine which items two collections share.

Unlike lists and tuples, sets do not support accessing items by numerical index.

### Sets automatically remove duplicates

```python
scores = {95, 88, 95, 76, 88}

print(scores)
```

Output, in any order:

```text
{88, 95, 76}
```

Each value appears only once.

**Remember:** Sets are unordered collections. Don't rely on the order in which elements appear when printed.

---

## 9. Creating an Empty Set

This is a common beginner mistake:

```python
empty = {}
print(type(empty))
```

Output:

```text
<class 'dict'>
```

Empty curly braces create a dictionary, not a set.

To create an empty set, use:

```python
empty_set = set()

print(type(empty_set))
```

Output:

```text
<class 'set'>
```

---

## 10. Adding and Removing Set Items

### Adding an item

Use `.add()`.

```python
languages = {"Python", "Java"}

languages.add("C++")

print(languages)
```

The set now contains all three languages, though their printed order may vary.

Adding a value that already exists does not create a duplicate:

```python
languages.add("Python")

print(len(languages))
```

Output:

```text
3
```

### Adding several items

Use `.update()`.

```python
languages.update(["JavaScript", "Go", "Rust"])

print(len(languages))
```

The set now contains six unique languages.

### Removing an item

```python
languages.remove("Java")
```

`.remove()` raises a `KeyError` if the item is absent.

If you want to remove an item only when it exists, use `.discard()`:

```python
languages.discard("Ruby")
```

No error occurs if `"Ruby"` isn't present.

You can also use `.pop()` to remove and return an arbitrary set element. Because sets are unordered, you shouldn't predict which element will be removed.

---

## 11. Set Operations: Union

Imagine two groups of students:

```python
python_students = {"Amina", "Tasnimul", "Rahul"}
java_students = {"Rahul", "Sara", "Tasnimul"}
```

**Union** combines all unique elements from both sets.

Use the `|` operator or `.union()`.

```python
everyone = python_students | java_students

print(everyone)
```

The result contains:

```text
Amina, Tasnimul, Rahul, Sara
```

The displayed order can vary.

Union is useful when combining categories without duplicates.

---

## 12. Set Operations: Intersection

**Intersection** finds elements that appear in both sets.

Use the `&` operator or `.intersection()`.

```python
both = python_students & java_students

print(both)
```

Output, in any order:

```text
{'Tasnimul', 'Rahul'}
```

These students belong to both groups.

---

## 13. Set Operations: Difference

**Difference** finds items that belong to one set but not the other.

```python
only_python = python_students - java_students

print(only_python)
```

Output:

```text
{'Amina'}
```

The difference is directional:

```python
only_java = java_students - python_students

print(only_java)
```

Output:

```text
{'Sara'}
```

In general, `A - B` is not the same as `B - A`.

---

## 14. Set Operations: Symmetric Difference

**Symmetric difference** finds elements that belong to either set, but not both.

Use the `^` operator.

```python
different = python_students ^ java_students

print(different)
```

Output, in any order:

```text
{'Amina', 'Sara'}
```

These two students belong to only one of the groups.

### Summary of set operators

| Operator | Operation            | Meaning                           |
| -------- | -------------------- | --------------------------------- |
| `A \| B` | Union                | Items in A or B                   |
| `A & B`  | Intersection         | Items in both A and B             |
| `A - B`  | Difference           | Items in A but not B              |
| `A ^ B`  | Symmetric difference | Items in either set, but not both |

These operations are useful for comparing student groups, filtering categories, and analyzing collections of unique values.

---

## 15. Checking Set Relationships

You can check whether one set is contained within another.

```python
programming = {"Python", "Java", "C++"}
beginner = {"Python", "Java"}

print(beginner.issubset(programming))
print(programming.issuperset(beginner))
print(programming.isdisjoint({"Biology", "History"}))
```

Output:

```text
True
True
True
```

* `.issubset()` checks whether every item in one set appears in another.
* `.issuperset()` checks whether a set contains every item in another.
* `.isdisjoint()` checks whether two sets have no elements in common.

---

## 16. Converting Between Lists, Tuples, and Sets

You can convert one collection type into another.

```python
subjects = ["Python", "Physics", "Python", "Mathematics"]

unique_subjects = set(subjects)

print(unique_subjects)
```

The set contains only the unique subjects.

Convert it back to a list:

```python
subjects_again = list(unique_subjects)

print(subjects_again)
```

The list's order may differ from the original because a set doesn't preserve the original sequence.

If you need to remove duplicates while keeping their original order, a different approach is:

```python
subjects = ["Python", "Physics", "Python", "Mathematics"]

unique_subjects = list(dict.fromkeys(subjects))

print(unique_subjects)
```

Output:

```text
['Python', 'Physics', 'Mathematics']
```

This technique works because dictionaries preserve insertion order and retain only one entry per key.

---

## 17. Tuples, Sets, Lists, and Dictionaries Compared

| Feature             | List                 | Tuple                       | Set                          | Dictionary           |
| ------------------- | -------------------- | --------------------------- | ---------------------------- | -------------------- |
| Syntax              | `[]`                 | `()`                        | `{}`                         | `{"key": value}`     |
| Ordered             | Yes                  | Yes                         | No guaranteed order          | Yes, insertion order |
| Duplicates          | Allowed              | Allowed                     | Not allowed                  | Keys must be unique  |
| Access              | Index                | Index                       | No index                     | Key                  |
| Add or remove items | Yes                  | No direct item modification | Yes                          | Yes                  |
| Best for            | Changeable sequences | Fixed sequences             | Unique items and comparisons | Labeled information  |

These are general rules. Python also has more advanced features, but this table is a useful starting point.

---

## 18. Coding Lab: Course Enrollment Analyzer 🎓

Imagine three courses:

```python
python_students = {"Amina", "Tasnimul", "Rahul", "Sara"}
ai_students = {"Tasnimul", "Rahul", "Imran"}
web_students = {"Sara", "Rahul", "Nadia"}
```

Build a program that:

1. Displays all unique students enrolled in Python or AI.
2. Finds students enrolled in both Python and AI.
3. Finds students enrolled in Python but not AI.
4. Finds students enrolled in exactly one of Python and AI.
5. Checks whether every AI student is also enrolled in Python.
6. Counts how many unique students are enrolled in any of the three courses.

**Hints:**

* Union: `python_students | ai_students`
* Intersection: `python_students & ai_students`
* Difference: `python_students - ai_students`
* Symmetric difference: `python_students ^ ai_students`
* Combine all three groups using another union operation.
* Use `len()` to count the resulting set.

Predict the output before running your solution.

---

## 19. Boss Challenge: Study Group Planner 🏆

Create a study group planner that manages three collections:

* Students learning Python.
* Students learning AI.
* Students learning web development.

Your program should:

* Store each group in a set.
* Add a new student to a group.
* Remove a student safely.
* Identify students enrolled in all three groups.
* Find students enrolled in at least one group.
* Identify students enrolled in exactly one group.
* Ask the user to enter a student's name and check whether that student belongs to a particular group.

**Bonus:** Store a fixed coordinate pair as a tuple. Unpack it into separate variables and print them with descriptive labels.

Try to solve the challenge without copying the earlier examples line by line.

---

## 20. Retrieval Practice

Answer these questions without looking at the explanations.

1. What is a tuple?
2. Why can't you replace an individual tuple item?
3. Why does `(10,)` create a tuple but `(10)` create an integer?
4. What is tuple unpacking?
5. What is a set?
6. Why does `{}` create a dictionary rather than an empty set?
7. What happens when you add a duplicate value to a set?
8. What is the difference between `.remove()` and `.discard()`?
9. What do union and intersection mean?
10. What is the difference between `A - B` and `B - A`?
11. What does symmetric difference return?
12. Why shouldn't you depend on the printed order of set elements?
13. Which collection should you choose to store labeled student information?

---

## 21. Completion Checklist

Before moving to Lesson 10, confirm that you can:

* [ ] Create and access tuples.
* [ ] Explain tuple immutability.
* [ ] Create a one-item tuple correctly.
* [ ] Use tuple unpacking.
* [ ] Create empty and non-empty sets.
* [ ] Add and remove set elements.
* [ ] Explain why sets eliminate duplicates.
* [ ] Perform union, intersection, difference, and symmetric difference.
* [ ] Check subset, superset, and disjoint relationships.
* [ ] Convert between collection types.
* [ ] Choose between lists, tuples, sets, and dictionaries.
* [ ] Complete the Course Enrollment Analyzer.

**Next lesson:** Functions — Turn Reusable Instructions into Building Blocks.

Keep experimenting: predict the result, run your code, and explain why the result happened.
