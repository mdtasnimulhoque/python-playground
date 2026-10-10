# Lesson 13: Files and Data — Make Information Last

## 1. Why Do Programs Need Files?

So far, most of our Python examples have stored information in variables.

```python
student_name = "Tasnimul"
score = 92

print(student_name, score)
```

When a program finishes, its ordinary variables disappear. If we want to preserve information between runs, we can save it in a file.

Files allow programs to store notes, settings, reports, student records, and other information.

## 2. Understanding File Modes

Python's built-in `open()` function opens a file.

| Mode  | Meaning                                         |
| ----- | ----------------------------------------------- |
| `"r"` | Read an existing file                           |
| `"w"` | Write to a file, replacing existing contents    |
| `"a"` | Append to the end of a file                     |
| `"x"` | Create a new file, failing if it already exists |

Be careful with `"w"`: opening an existing file in this mode replaces its previous contents.

## 3. Writing a Text File

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("I am learning Python.\n")
    file.write("Files help programs remember information.\n")
```

Here:

* `open()` opens the file.
* `"w"` selects write mode.
* `encoding="utf-8"` supports a wide range of characters.
* `with` automatically closes the file when the block finishes.
* `\n` creates a new line.

The file is created relative to the program's current working directory unless you supply another path.

## 4. Reading a Text File

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
```

The `read()` method returns the file's contents as a string.

Other useful methods include:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    print(first_line)
```

You can also process a file one line at a time:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

`rstrip()` removes trailing whitespace, including the newline at the end of a line.

## 5. Appending Without Replacing Existing Content

Append mode adds information to the end of a file.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Today I learned about file handling.\n")
```

Run this code multiple times and the message will be appended multiple times.

Use `"a"` when you want to preserve existing content.

## 6. Handling Missing Files

Opening a file in read mode raises `FileNotFoundError` if the file does not exist.

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print("The requested file does not exist.")
```

For larger projects, consider using `pathlib` to check paths and organise file operations.

## 7. Understanding File Paths With `pathlib`

```python
from pathlib import Path

file_path = Path("notes.txt")

print("File name:", file_path.name)
print("File extension:", file_path.suffix)
print("Exists:", file_path.exists())
```

A relative path is interpreted from the current working directory. If a program needs a path relative to its own location, `Path(__file__).resolve().parent` can help.

```python
from pathlib import Path

script_folder = Path(__file__).resolve().parent
notes_path = script_folder / "notes.txt"

print(notes_path)
```

This is particularly useful when running scripts from different directories.

## 8. What Is JSON?

JSON stands for JavaScript Object Notation. It is a widely used text format for storing structured data.

Example:

```json
{
  "name": "Tasnimul",
  "score": 92,
  "subjects": ["Python", "Physics", "Mathematics"]
}
```

JSON can represent objects, arrays, strings, numbers, booleans, and null values.

Python's built-in `json` module converts between Python data and JSON.

## 9. Saving Data as JSON

```python
import json

student = {
    "name": "Tasnimul",
    "score": 92,
    "subjects": ["Python", "Physics", "Mathematics"]
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)
```

`json.dump()` writes a Python object into a file in JSON format. The `indent=4` argument makes the file easier to read.

## 10. Loading JSON Data

```python
import json

with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student["name"])
print(student["score"])
print(student["subjects"])
```

`json.load()` reads JSON from a file and converts it into corresponding Python data structures.

You can also use `json.dumps()` and `json.loads()` to convert between JSON strings and Python objects without working directly with files.

## 11. Handling Invalid JSON

A JSON file may contain malformed data. Python raises `json.JSONDecodeError` when it cannot parse the contents.

```python
import json

try:
    student = json.loads('{"name": "Tasnimul",}')
except json.JSONDecodeError:
    print("The JSON data is invalid.")
```

Notice the extra comma after `"Tasnimul"`. It makes this JSON invalid.

## 12. Saving Multiple Student Records

A list of dictionaries is useful for storing multiple records.

```python
import json

students = [
    {"name": "Tasnimul", "score": 92},
    {"name": "Nora", "score": 84},
    {"name": "Andria", "score": 96}
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

for student in loaded_students:
    print(student["name"], student["score"])
```

This approach can form the foundation of a student management application.

## 13. Practical Project: A Study Tracker

Imagine creating a program that records what you study each day.

Each record might contain:

* The subject you studied
* The topic you completed
* The number of minutes you studied

Example data:

```python
study_session = {
    "subject": "Python",
    "topic": "File handling",
    "minutes": 45
}
```

You could save multiple sessions in a JSON file and load them the next time you run the program.

This is an introduction to persistent data. Later, you can extend the project with dates, summaries, input validation, and reports.

## 14. Common Mistakes to Avoid

1. Opening a file in `"w"` mode when you intended to append.
2. Trying to read a file that does not exist.
3. Forgetting to use `with` for file operations.
4. Assuming a relative path always points to the script's folder.
5. Attempting to parse invalid JSON.
6. Saving values without considering the correct data format.
7. Assuming files are saved in the same place on every computer.

## 15. Practice Checklist

By the end of this lesson, you should be able to:

* [ ] Create and write a text file.
* [ ] Read all the contents of a file.
* [ ] Read a file line by line.
* [ ] Append text without replacing existing contents.
* [ ] Explain the difference between `"r"`, `"w"`, `"a"`, and `"x"`.
* [ ] Handle `FileNotFoundError`.
* [ ] Use `pathlib` to work with file paths.
* [ ] Save and load Python data using JSON.
* [ ] Handle invalid JSON.
* [ ] Build a simple persistent study tracker.

## 16. Challenge

Build a small study-record program that:

1. Creates a list of study sessions.
2. Saves them to `study_sessions.json`.
3. Loads the saved sessions.
4. Prints each subject, topic, and duration.
5. Handles a missing JSON file gracefully.

**Next lesson:** Lesson 14 — Object-Oriented Programming (OOP).
