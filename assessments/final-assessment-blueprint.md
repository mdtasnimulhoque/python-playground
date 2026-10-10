# Python Playground — Final Assessment Blueprint

**Status:** Design specification
**Audience:** Course maintainers and assessment developers
**Purpose:** Define a fair, reliable, accessible final assessment for the complete Python Playground course.

This document describes a future assessment system. It does not claim that the entire course, online exam engine, automated grader, or leaderboard already exists.

## 1. Assessment principles

The final assessment should measure whether learners can:

1. Explain core ideas in their own words.
2. Predict program behaviour and trace values step by step.
3. Read and interpret error messages.
4. Debug incorrect code and explain why a correction works.
5. Write programs independently from clear requirements.
6. Combine concepts in a practical task.
7. Test solutions and make sensible decisions about readability and correctness.

Avoid making speed the primary measure of skill. Learners who reason carefully should not be disadvantaged merely because they take longer.

**Curriculum rule:** Never require knowledge that has not been taught or clearly identified as optional extension material.

## 2. Exam format

* **Total:** 100 points
* **Suggested duration:** 90 minutes, subject to pilot testing
* **Attempts:** Unlimited practice attempts; a separately defined policy for official scored attempts
* **Recommended provisional passing score:** 70/100, plus a minimum practical-section score
* **Results:** Total score, percentage, section breakdown, feedback, and recommended review material

The duration, passing threshold, practical minimum, and official retake policy must be validated with learners before launch.

A learner should be able to understand the rules before starting an official attempt.

## 3. Sections and weighting

| Section                           |  Points | What it measures                                           |
| --------------------------------- | ------: | ---------------------------------------------------------- |
| A. Concepts and vocabulary        |      10 | Understanding fundamental ideas                            |
| B. Predict the output             |      15 | Tracing execution and values                               |
| C. Read and reason about code     |      15 | Understanding functions, data structures, and program flow |
| D. Debugging and errors           |      15 | Identifying causes and producing corrections               |
| E. Write code                     |      25 | Solving clearly specified programming tasks                |
| F. Testing and code quality       |      10 | Choosing useful tests and writing readable solutions       |
| G. Integrated practical challenge |      10 | Combining relevant skills in a small project               |
| **Total**                         | **100** |                                                            |

Sections should contain a balanced range of difficulties. A question must not depend on an obscure detail unless that detail is part of the published learning objectives.

## 4. Curriculum coverage

The final exam should be assembled only after the corresponding lessons and practice materials are published and reviewed.

### First Steps

Potential topics include:

* Running code, output, and comments
* Values, types, and variables
* Input, output, and conversion
* Arithmetic, comparisons, and Boolean logic
* Conditions and loops
* Strings and core collections
* Functions, parameters, return values, and scope
* Files, imports, exceptions, and debugging

### Builder Path

Potential topics include:

* Decomposition and pseudocode
* Comprehensions, mutability, and copying
* Searching, sorting, and basic complexity reasoning
* CSV, JSON, and text files
* Automated tests and debugging tools
* Classes, composition, and dataclasses
* Type hints, logging, configuration, and command-line arguments
* Git, documentation, and packaging basics

### Deep Dive

Potential topics include:

* Iterables, iterators, and generators
* Decorators, closures, and context managers
* Exceptions and Python's data model
* Async programming and concurrency concepts
* Profiling and performance
* Regular expressions and advanced typing
* Environments, reproducibility, and selected Python internals

### Creator Lab

Use a practical challenge aligned to the learner's chosen pathway, such as automation, APIs, data analysis, machine learning, or scientific computing.

Pathway-specific tasks should have clearly stated prerequisites and comparable assessment difficulty. A learner should not need specialist knowledge from another pathway to pass the general exam.

**Coverage safeguard:** If a topic has not been taught, remove the question, mark it as optional extension work, or publish the relevant material before the exam.

## 5. Question formats

Use a balanced mixture of:

* Multiple-choice questions
* Multiple-select questions where several answers may be correct
* Code-output prediction
* Short explanations in the learner's own words
* Debugging with corrected code
* Code-writing tasks evaluated against tests and a rubric
* Test-case selection and edge-case reasoning
* Practical tasks with explicit input, output, and behaviour requirements

Multiple-choice questions alone cannot demonstrate independent coding ability. Include substantial opportunities to write, test, and correct code.

Every question should have a unique identifier, topic tags, point value, expected answer or grading rubric, difficulty level, and a reviewed explanation.

## 6. Code execution and grading

For code-writing questions:

1. Define the required behaviour and expected input/output clearly.
2. Test the reference solution against normal cases and relevant edge cases.
3. Use hidden tests only when they check published requirements fairly.
4. Apply execution time and resource limits to prevent infinite loops or excessive resource use.
5. Run untrusted learner code in an appropriately isolated environment; never execute arbitrary submissions directly on the main application server.
6. Return useful feedback without exposing private tests, server secrets, or the full hidden answer key.
7. Allow human review or an appeal process when an automated grader may have misclassified a valid solution.

Do not grade solely on exact text matching when multiple valid Python solutions exist. Where practical, assess program behaviour.

## 7. Code-writing rubric

Use a consistent rubric, adjusted to the task:

* **Correctness — 50%:** Meets the required behaviour for normal and relevant edge cases.
* **Reasoning — 20%:** Uses an appropriate approach and can explain key decisions.
* **Testing — 15%:** Tests representative cases, including a relevant edge case.
* **Readability — 10%:** Uses clear names and sensible structure.
* **Robustness — 5%:** Handles expected invalid input or errors when required.

For a task worth a different number of points, scale the rubric proportionally and define how partial credit works.

Do not penalize the same mistake repeatedly across several categories. Publish the rubric before the assessment.

## 8. Learner feedback

After submission, show:

* Score out of 100 and percentage
* Section-by-section results
* Explanations for objective questions
* Test feedback and rubric notes for coding questions
* Links to relevant lessons and exercises
* Suggested next steps based on demonstrated gaps

During an official attempt, withhold correct answers until submission. Practice quizzes can offer immediate explanations.

Feedback should explain what to improve, not merely state that an answer is wrong.

## 9. Fairness and integrity

* Make instructions accessible and controls keyboard-friendly.
* Do not require paid software or high-end hardware.
* Publish time limits and official attempt rules in advance.
* Offer unranked practice without leaderboard penalties.
* Use equivalent question variants with comparable difficulty.
* Avoid requiring unnecessary personal information.
* Provide a process for correcting technical failures and reviewing disputed scores.
* Define retakes, ties, score corrections, and suspicious activity before launch.

An online exam should not claim to prevent all cheating. Design for reliable assessment, clear expectations, and reasonable integrity protections.

## 10. Leaderboard design

Treat learning progress and final-exam achievement as different measures.

### Course learning leaderboard

Award points for defined activities such as lesson quizzes, completed exercises, and reviewed projects.

* Publish the points system.
* Cap repetitive activities so repeated easy attempts cannot dominate the rankings.
* Clearly distinguish completion, practice, and verified achievement.
* Avoid comparing learners using incomparable activities or unpublished scoring rules.

### Final assessment leaderboard

Rank learners using verified official scores.

* Make score the primary ranking factor.
* Define tie handling before launch.
* Use completion time only if a published policy explicitly permits it.
* Identify the assessment version so scores from materially different exams are not compared as though they were identical.
* Decide how retakes affect rankings and apply the same rules to everyone.

Suggested public fields: rank, chosen display name, score, assessment version, and achievement date.

Never publish email addresses or unnecessary personal information. Let learners understand what is public and provide a way to opt out of public display.

**Technical requirement:** A static GitHub Pages site alone cannot securely maintain a shared leaderboard. A future implementation will need authenticated score submission, persistent storage, server-side validation, and appropriate access controls. Never trust a score submitted only by a learner's browser.

## 11. Release checklist

Before launch:

* [ ] Every assessed topic has published teaching and practice material.
* [ ] Questions have been reviewed for correctness, ambiguity, and curriculum alignment.
* [ ] Point values and partial-credit rules are documented.
* [ ] Code-writing tasks have automated tests and readable rubrics.
* [ ] Execution limits and code isolation have been tested.
* [ ] Feedback and lesson-review links are available.
* [ ] The exam has been piloted with beginners and independent reviewers.
* [ ] Accessibility, mobile usability, and low-bandwidth behaviour have been checked.
* [ ] Retakes, ties, score corrections, and technical failures have defined policies.
* [ ] Score storage and server-side validation have been tested.
* [ ] Leaderboard privacy and public-display choices are clear.

## 12. Development sequence

1. Publish checkpoint quizzes alongside lessons.
2. Verify that quizzes match the actual lesson content.
3. Build a local, unranked practice assessment.
4. Test and refine the questions with learners.
5. Finish publishing and reviewing the course curriculum.
6. Assemble and pilot the complete final assessment.
7. Implement secure code execution and grading where needed.
8. Add authenticated score storage and the leaderboard as a separate feature.

**Current milestone:** The initial lesson quizzes and Level 0 checkpoint assessment are drafted. The complete final exam and online leaderboard remain future development tasks.
