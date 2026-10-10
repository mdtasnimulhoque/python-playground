# Lesson 14: Object-Oriented Programming (OOP)

## 1. What Is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a way of organising programs using **objects** that combine data and behaviour.

Imagine a student record. It has data such as a name and score, and behaviours such as calculating an average or displaying a report.

OOP lets us represent these concepts in Python.

You have already used objects without necessarily thinking about them:

```python
name = "Tasnimul"
print(name.upper())
```

The string `"Tasnimul"` is an object, and `upper()` is one of its methods.

## 2. Classes and Objects

A **class** is a blueprint. An **object** is an individual instance created from that blueprint.

```python
class Student:
    pass


student_one = Student()
student_two = Student()

print(type(student_one))
print(type(student_two))
```

Both objects belong to the `Student` class, but they are separate instances.

The `pass` keyword is a placeholder that allows an otherwise empty class body.

## 3. Attributes: Giving Objects Data

Attributes store information associated with an object.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


student_one = Student("Tasnimul", 92)
student_two = Student("Nora", 84)

print(student_one.name)
print(student_one.score)
print(student_two.name)
print(student_two.score)
```

Here:

* `__init__()` initialises a new object.
* `self` refers to the current instance.
* `self.name` stores that instance's name.
* `self.score` stores that instance's score.

When you create a student, Python passes the new instance to `__init__()` as `self`.

## 4. Methods: Giving Objects Behaviour

A method is a function defined inside a class.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"My name is {self.name}.")

    def show_score(self):
        print(f"My score is {self.score}.")


student = Student("Tasnimul", 92)

student.introduce()
student.show_score()
```

Methods can read or modify an object's attributes.

## 5. Instance Methods and `self`

An instance method operates on a particular object.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


counter = Counter()
counter.increment()
counter.increment()

print(counter.value)

counter.reset()
print(counter.value)
```

Each `Counter` object has its own `value`. Changing one counter does not automatically change another.

## 6. The Difference Between Class and Instance Attributes

A class attribute is shared through the class, while an instance attribute belongs to an individual object.

```python
class Student:
    school = "Python Playground"

    def __init__(self, name):
        self.name = name


student_one = Student("Tasnimul")
student_two = Student("Nora")

print(student_one.school)
print(student_two.school)

print(student_one.name)
print(student_two.name)
```

Use class attributes for information that should normally be shared. Use instance attributes for data that varies between objects.

Be careful when using mutable class attributes such as lists: all instances may refer to the same list.

## 7. Encapsulation and Properties

Encapsulation means organising data and the operations that work on it behind a clear interface.

Python uses conventions and language features to help with this. A leading underscore, such as `_score`, indicates that an attribute is intended for internal use.

A property lets you expose a value through attribute-style access while validating changes.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Score must be between 0 and 100.")

        self._score = value


student = Student("Tasnimul", 92)

print(student.score)

student.score = 95
print(student.score)
```

If you try to assign `student.score = 150`, the setter raises a `ValueError`.

A single leading underscore is a convention, not strict access protection. Python's properties are useful for controlled access and validation.

## 8. Inheritance

Inheritance lets a new class reuse or extend another class's behaviour.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

    def show_score(self):
        print(f"My score is {self.score}.")


student = Student("Tasnimul", 92)

student.introduce()
student.show_score()
```

Here:

* `Person` is the parent class.
* `Student` is the child class.
* `super().__init__(name)` calls the parent's initialisation method.
* `Student` inherits the `introduce()` method.

Inheritance is helpful when a class genuinely represents a specialised version of another class.

## 9. Method Overriding

A child class can provide its own implementation of a method inherited from its parent.

```python
class Person:
    def describe(self):
        print("I am a person.")


class Student(Person):
    def describe(self):
        print("I am a student.")


person = Person()
student = Student()

person.describe()
student.describe()
```

Both classes have a `describe()` method, but the behaviour depends on the object's class.

## 10. Polymorphism

Polymorphism allows different objects to respond to the same method call in their own ways.

```python
class Student:
    def introduce(self):
        return "I am a student."


class Teacher:
    def introduce(self):
        return "I am a teacher."


people = [Student(), Teacher()]

for person in people:
    print(person.introduce())
```

The loop does not need to know the exact class of every object. It only needs each object to provide the method it calls.

## 11. Special Methods

Python supports special methods that define how objects interact with built-in operations.

For example, `__str__()` defines a human-readable string representation.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}/100"


student = Student("Tasnimul", 92)

print(student)
```

Other special methods include `__len__()` and `__eq__()`. They should be implemented when their behaviour makes sense for your class.

## 12. Composition: Objects Containing Other Objects

Composition means building a larger object using other objects.

```python
class StudySession:
    def __init__(self, subject, topic, minutes):
        self.subject = subject
        self.topic = topic
        self.minutes = minutes


class StudyTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def total_minutes(self):
        return sum(session.minutes for session in self.sessions)


tracker = StudyTracker()

tracker.add_session(StudySession("Python", "Classes", 45))
tracker.add_session(StudySession("Physics", "Motion", 60))

print("Total study time:", tracker.total_minutes())
```

The tracker contains a list of `StudySession` objects. This is a useful way to model real-world systems.

## 13. When Should You Use OOP?

OOP is useful when a program has related entities with data and behaviour, such as:

* Students and courses
* Bank accounts
* Game characters
* Study sessions and trackers
* Medical records and analysis workflows

Not every problem needs a class. For small calculations or simple scripts, ordinary functions and data structures may be clearer.

Choose the simplest design that solves the problem well.

## 14. Common Mistakes to Avoid

1. Forgetting `self` in an instance method.
2. Confusing a class with an instance.
3. Forgetting to initialise required attributes.
4. Using class attributes for data that should be unique to each object.
5. Using inheritance when composition would be more appropriate.
6. Modifying internal data without validating important rules.
7. Creating classes for problems that simple functions could solve.

## 15. Practice Checklist

By the end of this lesson, you should be able to:

* [ ] Explain the difference between a class and an object.
* [ ] Create objects using `__init__()`.
* [ ] Use instance attributes and methods.
* [ ] Distinguish class attributes from instance attributes.
* [ ] Validate values using properties.
* [ ] Use inheritance and `super()`.
* [ ] Explain method overriding and polymorphism.
* [ ] Implement a simple special method such as `__str__()`.
* [ ] Use composition to combine objects.
* [ ] Decide when OOP is useful.

## 16. Challenge: Build a Study Tracker With Classes

Create a `StudySession` class with attributes for subject, topic, and study duration.

Then create a `StudyTracker` class that can:

1. Add study sessions.
2. List all saved sessions.
3. Calculate the total study time.
4. Calculate the total time spent on a particular subject.
5. Reject invalid study durations.

For an extra challenge, save the records to JSON and load them again when the program starts.

**Next lesson:** Lesson 15 — Capstone Project: Build a Complete Python Application.
