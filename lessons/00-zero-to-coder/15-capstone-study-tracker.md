# Lesson 15 — Capstone Project: Python Playground Study Tracker

## Welcome to Your Final Project

Congratulations on reaching the capstone lesson!

Throughout this course, you've learned how to work with variables, conditions, loops, collections, functions, modules, exceptions, files, JSON, classes, and objects.

Now it's time to combine those skills into one useful application.

Your mission is to build a command-line **Study Tracker** that lets learners record their study sessions, review their progress, and keep their data saved between runs.

This is not just another collection of isolated experiments. It is a small but complete software project.

---

## 1. Project Goals

Build a Python application that allows a user to:

1. Add a study session.
2. View all recorded sessions.
3. Calculate total study time.
4. View study time grouped by subject.
5. Save records to a JSON file.
6. Load previously saved records when the application starts.
7. Handle invalid input without crashing.
8. Handle missing or damaged data files gracefully.
9. Organize the program using functions and classes.

## 2. Example User Experience

Your finished application might display a menu like this:

```text
=================================
     PYTHON PLAYGROUND
         STUDY TRACKER
=================================

1. Add a study session
2. View all sessions
3. View study summary
4. Save and exit

Choose an option:
```

A learner might add a session like this:

```text
Subject: Physics
Topic: Laws of Motion
Minutes studied: 45

Session added successfully!
```

The summary could look like this:

```text
========== STUDY SUMMARY ==========

Total sessions: 3
Total study time: 135 minutes

Time by subject:
Physics: 75 minutes
Python: 60 minutes

===================================
```

These are examples of the intended experience, not fixed output requirements. Your program should calculate the results from the records it actually contains.

## 3. Project Structure

Create the main Python file inside this lesson's folder:

```text
lessons/
└── 00-zero-to-coder/
    ├── 15-capstone-study-tracker.md
    ├── lesson_15.py
    └── lesson_15_data/
        └── study_sessions.json
```

Your program should create the `lesson_15_data` folder when necessary.

**Important:** Keep this project's data separate from the files generated in Lesson 13. Do not delete or overwrite your earlier lesson files.

## 4. Required Features

### Feature A — Add a Study Session

Each session must contain:

* Subject
* Topic
* Study duration in minutes

Requirements:

* Subject and topic cannot be empty.
* Study duration must be a positive whole number.
* Invalid entries should produce a helpful message.
* A rejected entry must not be added to the tracker.

### Feature B — View All Sessions

Display every recorded session in a readable format.

Each entry should show its subject, topic, and duration.

If no sessions exist, display a friendly message rather than an error.

### Feature C — Study Summary

Calculate and display:

* Total number of sessions
* Total study time in minutes
* Total study time in hours and minutes
* Study time grouped by subject

The summary must use the actual session records. Do not hard-code example totals.

### Feature D — Save Data

Save the session records to a JSON file.

Requirements:

* Use Python's `json` module.
* Use `pathlib` to manage file paths.
* Store the records in a structured format.
* Make sure the program reports saving errors clearly.

### Feature E — Load Data

When the program starts, attempt to load previously saved records.

Your application must handle:

* A data file that does not exist yet.
* An empty data file.
* Invalid JSON.
* Records containing missing or invalid fields.

A missing file should not prevent a first-time user from running the application. Invalid data should not crash the entire program.

### Feature F — Menu and Program Flow

Keep displaying the menu until the user chooses to exit.

Requirements:

* Handle unknown menu choices.
* Keep the program running after recoverable input errors.
* Save the records before exiting.
* Keep the menu logic easy to understand.

## 5. Required Programming Concepts

Your implementation must demonstrate the following:

* Variables and data types
* Conditions and loops
* Lists and dictionaries
* Functions with parameters and return values
* Classes and objects
* Exception handling
* JSON serialization and deserialization
* File and directory management with `pathlib`
* Input validation
* Separation of responsibilities between functions and classes

Use meaningful names and add comments where they help explain your reasoning.

## 6. Suggested Design

Start with a `StudySession` class to represent one session.

Each session should know its subject, topic, and duration.

Next, create a `StudyTracker` class to manage a collection of sessions.

The tracker should be responsible for adding sessions, listing them, calculating summaries, loading data, and saving data.

You may create additional helper functions if they make your code clearer.

Avoid putting the entire application into one enormous function.

## 7. Testing Checklist

Before declaring the project complete, verify each case:

* [ ] The application starts when no data file exists.
* [ ] A valid study session can be added.
* [ ] Empty subject and topic values are rejected.
* [ ] Zero, negative, and non-numeric durations are rejected.
* [ ] All saved sessions can be listed.
* [ ] The total study time is calculated correctly.
* [ ] Study time is grouped correctly by subject.
* [ ] Data is saved to JSON.
* [ ] Previously saved sessions appear after restarting the application.
* [ ] An invalid menu choice does not crash the program.
* [ ] Invalid JSON is handled gracefully.
* [ ] Invalid records are rejected or safely skipped.
* [ ] Exiting the application saves the records.

## 8. Stretch Challenges

Complete these only after all required features work:

1. Add a date and time to every session.
2. Let users search sessions by subject.
3. Allow users to delete a session.
4. Add a daily study-time summary.
5. Write automated tests for the tracker.
6. Improve the command-line interface with clearer formatting.

## 9. Definition of Done

Your capstone is complete when:

* All required features work.
* Valid data persists between application runs.
* Invalid input is handled safely.
* The code uses functions and classes appropriately.
* The testing checklist has been completed.
* The program runs without unhandled errors during normal use.

## Final Challenge

Build the application in small, testable stages. Run it frequently, inspect the output, and fix problems as you discover them.

You do not need to write perfect code on your first attempt. Real software development involves testing, debugging, and improving your work.

**The goal is not merely to finish the project. The goal is to understand why it works.**

Welcome to your first complete Python application!
