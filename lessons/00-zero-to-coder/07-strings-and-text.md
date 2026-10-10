# Lesson 7: Strings — Mastering Text in Python 📝

**Level:** 0 — Zero to Coder
**Prerequisites:** Lessons 1–6
**Estimated time:** 60–90 minutes
**Practice file:** `lessons/00-zero-to-coder/lesson_07.py`

---

## 1. What Is a String?

A **string** is a sequence of characters used to represent text.

Characters can include:

* Letters: `"Python"`
* Numbers stored as text: `"12345"`
* Spaces: `"Hello World"`
* Symbols: `"@#$%"`
* A combination: `"Tasnim is learning Python!"`

In Python, strings are written inside quotation marks.

```python
name = "Tasnim"
message = 'Hello, world!'
number_as_text = "123"
```

You can use either single or double quotation marks, but they must match.

```python
print("Hello")
print('Python')
```

### Text versus numbers

These two values are different:

```python
print(123 + 7)
print("123" + "7")
```

Output:

```text
130
1237
```

Why? Python adds numbers mathematically, but joins strings together. Joining strings is called **concatenation**.

**Remember:** `"123"` is text; `123` is an integer.

---

## 2. Combining Strings

You can combine strings using `+`.

```python
first_name = "Ada"
last_name = "Lovelace"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Ada Lovelace
```

Notice the `" "` between the names. Without it, the result would be `AdaLovelace`.

You can also repeat a string with `*`.

```python
print("Python! " * 3)
```

Output:

```text
Python! Python! Python!
```

---

## 3. Changing Capitalization

Python provides useful string methods.

```python
message = "python is interesting"

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())
```

Output:

```text
PYTHON IS INTERESTING
python is interesting
Python Is Interesting
Python is interesting
```

| Method          | What it does                                  |
| --------------- | --------------------------------------------- |
| `.upper()`      | Converts letters to uppercase                 |
| `.lower()`      | Converts letters to lowercase                 |
| `.title()`      | Capitalizes the beginning of each word        |
| `.capitalize()` | Capitalizes the first character of the string |

### Important discovery

String methods return a result. They do not automatically replace the original variable.

```python
name = "python"

name.upper()
print(name)
```

Output:

```text
python
```

To keep the changed version, assign it:

```python
name = name.upper()
print(name)
```

Output:

```text
PYTHON
```

---

## 4. Removing Unwanted Spaces

Sometimes text contains extra spaces at the beginning or end.

```python
username = "   Tasnim   "

print(username.strip())
print(username.lstrip())
print(username.rstrip())
```

* `.strip()` removes spaces from both ends.
* `.lstrip()` removes spaces from the left.
* `.rstrip()` removes spaces from the right.

This is useful when processing names or text entered by users.

```python
username = "   Tasnim   "
clean_username = username.strip()

print(f"Welcome, {clean_username}!")
```

Output:

```text
Welcome, Tasnim!
```

These methods do not remove spaces between words.

---

## 5. Finding the Length of Text

Use `len()` to count how many characters a string contains.

```python
word = "Python"

print(len(word))
```

Output:

```text
6
```

Spaces and punctuation count too.

```python
message = "Hello world!"

print(len(message))
```

Output:

```text
12
```

There are 11 letters and one space, plus the exclamation mark: 12 characters in total.

---

## 6. Accessing Individual Characters

Just like list items, string characters have indexes starting at `0`.

```python
language = "Python"

print(language[0])
print(language[1])
print(language[5])
print(language[-1])
```

Output:

```text
P
y
n
n
```

Positive indexes count from the beginning; negative indexes count from the end.

```text
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
Negative:-6 -5 -4 -3 -2 -1
```

### Getting part of a string: slicing

Use a colon to select a section.

```python
language = "Python"

print(language[0:3])
print(language[2:6])
print(language[:4])
print(language[3:])
```

Output:

```text
Pyt
thon
Pyth
hon
```

The starting index is included, but the ending index is excluded.

For example, `language[0:3]` takes indexes `0`, `1`, and `2`.

---

## 7. Searching Inside Text

Use `in` to check whether a string contains another string.

```python
message = "I am learning Python"

print("Python" in message)
print("Java" in message)
```

Output:

```text
True
False
```

You can also use `.find()`.

```python
message = "I love Python"

print(message.find("Python"))
print(message.find("Java"))
```

Output:

```text
7
-1
```

`.find()` returns the starting index of the first match. It returns `-1` when the text is not found.

**Be careful:** Searching is case-sensitive.

```python
print("python" in "I love Python")
```

Output:

```text
False
```

---

## 8. Replacing Text

Use `.replace(old, new)` to replace one piece of text with another.

```python
message = "I study mathematics"

updated_message = message.replace("mathematics", "computer science")

print(updated_message)
```

Output:

```text
I study computer science
```

The original string remains unchanged unless you assign the result back to a variable.

```python
message = message.replace("mathematics", "computer science")
```

You can also replace multiple occurrences:

```python
message = "red blue red blue"

print(message.replace("red", "green"))
```

Output:

```text
green blue green blue
```

---

## 9. Splitting and Joining Text

### Splitting

`.split()` divides a string into a list.

```python
subjects = "Python Mathematics Physics Chemistry"

subject_list = subjects.split()

print(subject_list)
```

Output:

```text
['Python', 'Mathematics', 'Physics', 'Chemistry']
```

You can split using a particular separator:

```python
colours = "red,green,blue"

print(colours.split(","))
```

Output:

```text
['red', 'green', 'blue']
```

### Joining

`.join()` combines strings from an iterable, such as a list.

```python
words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is powerful
```

Try changing `" "` to `"-"` or `", "` and observe what happens.

**Remember:** The string before `.join()` is the separator.

---

## 10. Checking What a String Contains

Python provides methods for checking the contents of text.

```python
print("python".startswith("py"))
print("report.pdf".endswith(".pdf"))
print("12345".isdigit())
print("hello".isalpha())
print("hello123".isalnum())
```

Output:

```text
True
True
True
True
True
```

| Method          | Checks whether                         |
| --------------- | -------------------------------------- |
| `.startswith()` | Text begins with a particular sequence |
| `.endswith()`   | Text ends with a particular sequence   |
| `.isdigit()`    | All characters are digits              |
| `.isalpha()`    | All characters are letters             |
| `.isalnum()`    | All characters are letters or digits   |

These methods return Boolean values: `True` or `False`.

---

## 11. Formatting Text with f-Strings

You first met f-strings in Lesson 3. They are especially useful for building messages.

```python
name = "Tasnim"
subject = "Python"
hours = 3

message = f"{name} studied {subject} for {hours} hours."

print(message)
```

Output:

```text
Tasnim studied Python for 3 hours.
```

You can also place expressions inside an f-string.

```python
a = 10
b = 20

print(f"The sum is {a + b}.")
print(f"The product is {a * b}.")
```

Output:

```text
The sum is 30.
The product is 200.
```

The `f` before the quotation mark tells Python to evaluate expressions inside `{}`.

---

## 12. Strings Are Immutable

This is one of Python's most important string concepts.

**Immutable** means that a string cannot be changed character by character after it has been created.

This will cause an error:

```python
word = "Python"
word[0] = "J"
```

Instead, create a new string:

```python
word = "Python"
word = "J" + word[1:]

print(word)
```

Output:

```text
Jython
```

You didn't modify the original string's first character. You constructed a new string and assigned it to `word`.

This differs from lists, whose individual items you can update.

---

## 13. Common Mistakes and Debugging

### Mistake 1: Mixing strings and integers

```python
age = 19
print("Age: " + age)
```

This raises a `TypeError` because Python cannot concatenate a string and an integer directly.

Correct approaches:

```python
print("Age:", age)
print("Age: " + str(age))
print(f"Age: {age}")
```

### Mistake 2: Calling a method without parentheses

```python
message = "hello"
print(message.upper)
```

This displays a method reference rather than the uppercase text.

Correct:

```python
print(message.upper())
```

### Mistake 3: Wrong capitalization

```python
message = "Hello"
print(message.find("hello"))
```

Output:

```text
-1
```

The search is case-sensitive. Use the matching capitalization or normalize both strings first.

### Mistake 4: Index out of range

```python
word = "Python"
print(word[10])
```

This raises an `IndexError` because index `10` does not exist.

### Mistake 5: Forgetting that methods return new strings

```python
message = "hello"
message.upper()
print(message)
```

Output:

```text
hello
```

Correct:

```python
message = message.upper()
```

---

## 14. Your Coding Lab: Text Analyzer 🔬

Build a program that analyzes a sentence.

Your program should:

1. Ask the user to enter a sentence.
2. Remove unnecessary spaces from the beginning and end.
3. Print the sentence in uppercase and lowercase.
4. Display the number of characters.
5. Display the number of words.
6. Check whether the word `"python"` appears, ignoring capitalization.
7. Replace `"python"` with `"Python"` in a case-insensitive way if you can figure out how to do it.

**Hints:**

* Use `input()` to receive text.
* Use `.strip()` to clean the input.
* Use `.upper()` and `.lower()`.
* Use `len()` to count characters.
* Use `.split()` to create a list of words.
* Use `in` to check for a substring.

For the optional case-insensitive replacement challenge, first convert the sentence to lowercase to understand how to find a match. Then investigate how to preserve the original text when replacing different capitalization patterns.

---

## 15. Boss Challenge: A Personal Introduction Generator 🏆

Create a program that asks the user for:

* Their name
* Their favourite subject
* A hobby
* A goal they want to achieve

Then print a polished introduction using f-strings.

**Requirements:**

* Remove accidental spaces from the answers.
* Capitalize the name appropriately.
* Display the introduction in a readable paragraph.
* Print the character count and word count of the final introduction.
* Check whether the introduction contains the word `"Python"` without being affected by capitalization.

Try adding a feature that converts a comma-separated list of hobbies into a neatly formatted list.

---

## 16. Retrieval Practice: Test Yourself

Answer these without looking at the explanations above.

1. What is a string?
2. What is the difference between `"5" + "2"` and `5 + 2`?
3. What does `.strip()` do?
4. What does `len("Hello!")` return?
5. What does `"Python"[1:4]` return?
6. What does `.find()` return when a match cannot be found?
7. How does `.split()` differ from `.join()`?
8. Why does `word[0] = "J"` fail for a string?
9. What does an f-string allow you to do?
10. Why does `"Python" in "I love python"` return `False`?

---

## 17. Completion Checklist

Before moving to Lesson 8, confirm that you can:

* [ ] Explain what strings are.
* [ ] Combine and repeat strings.
* [ ] Use `.upper()`, `.lower()`, `.title()`, and `.capitalize()`.
* [ ] Clean text using `.strip()`.
* [ ] Count and access characters.
* [ ] Extract substrings using slicing.
* [ ] Search and replace text.
* [ ] Split and join strings.
* [ ] Use string-checking methods.
* [ ] Format messages with f-strings.
* [ ] Explain string immutability.
* [ ] Complete the Text Analyzer lab.

**Next lesson:** Dictionaries — Store Information Using Keys and Values.

Keep experimenting. The fastest way to master strings is to change the examples, predict the output, run the code, and explain why the result happened.
