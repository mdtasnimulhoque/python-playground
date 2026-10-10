
# Lesson 14: Object-Oriented Programming — Practice Experiments

print("=== Experiment 1: Creating a class and objects ===")


class Student:
    pass


student_one = Student()
student_two = Student()

print("Student one:", type(student_one).__name__)
print("Student two:", type(student_two).__name__)
print("Are they the same object?", student_one is student_two)


print("\n=== Experiment 2: Instance attributes ===")


class Learner:
    def __init__(self, name, score):
        self.name = name
        self.score = score


learner_one = Learner("Tasnimul", 92)
learner_two = Learner("Nora", 84)

print(learner_one.name, learner_one.score)
print(learner_two.name, learner_two.score)


print("\n=== Experiment 3: Instance methods ===")


class StudentProfile:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        return f"My name is {self.name}."

    def show_score(self):
        return f"My score is {self.score}."


profile = StudentProfile("Tasnimul", 92)

print(profile.introduce())
print(profile.show_score())


print("\n=== Experiment 4: Modifying object state ===")


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

print("After two increments:", counter.value)

counter.reset()
print("After reset:", counter.value)


print("\n=== Experiment 5: Class and instance attributes ===")


class CourseStudent:
    school = "Python Playground"

    def __init__(self, name):
        self.name = name


course_student_one = CourseStudent("Tasnimul")
course_student_two = CourseStudent("Nora")

print(course_student_one.school)
print(course_student_two.school)
print(course_student_one.name)
print(course_student_two.name)


print("\n=== Experiment 6: Properties and validation ===")


class ScoredStudent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("Score must be a number.")

        if not 0 <= value <= 100:
            raise ValueError("Score must be between 0 and 100.")

        self._score = value


scored_student = ScoredStudent("Tasnimul", 92)

print("Initial score:", scored_student.score)

scored_student.score = 96
print("Updated score:", scored_student.score)

try:
    scored_student.score = 150
except ValueError as error:
    print("Invalid score handled:", error)


print("\n=== Experiment 7: Inheritance ===")


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."


class InheritedStudent(Person):
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

    def show_score(self):
        return f"My score is {self.score}."


inherited_student = InheritedStudent("Tasnimul", 92)

print(inherited_student.introduce())
print(inherited_student.show_score())


print("\n=== Experiment 8: Method overriding ===")


class Animal:
    def describe(self):
        return "I am an animal."


class Cat(Animal):
    def describe(self):
        return "I am a cat."


animal = Animal()
cat = Cat()

print(animal.describe())
print(cat.describe())


print("\n=== Experiment 9: Polymorphism ===")


class Teacher:
    def introduce(self):
        return "I am a teacher."


class PolymorphicStudent:
    def introduce(self):
        return "I am a student."


people = [Teacher(), PolymorphicStudent(), Cat()]

for person in people:
    print(person.introduce() if hasattr(person, "introduce")
          else person.describe())


print("\n=== Experiment 10: Special method __str__ ===")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


book = Book("Learning Python", "Python Playground")

print(book)


print("\n=== Experiment 11: Composition with study sessions ===")


class StudySession:
    def __init__(self, subject, topic, minutes):
        if not isinstance(minutes, int) or isinstance(minutes, bool):
            raise ValueError("Minutes must be a whole number.")

        if minutes <= 0:
            raise ValueError("Minutes must be positive.")

        self.subject = subject
        self.topic = topic
        self.minutes = minutes


class StudyTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        if not isinstance(session, StudySession):
            raise TypeError("Expected a StudySession object.")

        self.sessions.append(session)

    def total_minutes(self):
        return sum(session.minutes for session in self.sessions)

    def minutes_for_subject(self, subject):
        return sum(
            session.minutes
            for session in self.sessions
            if session.subject.lower() == subject.lower()
        )

    def show_sessions(self):
        for session in self.sessions:
            print(
                f"{session.subject} — {session.topic}: "
                f"{session.minutes} minutes"
            )


tracker = StudyTracker()

tracker.add_session(StudySession("Python", "Classes", 45))
tracker.add_session(StudySession("Physics", "Motion", 60))
tracker.add_session(StudySession("Python", "Inheritance", 30))

tracker.show_sessions()

print("Total study time:", tracker.total_minutes(), "minutes")
print(
    "Python study time:",
    tracker.minutes_for_subject("Python"),
    "minutes"
)


print("\n=== Experiment 12: Handling invalid study sessions ===")

try:
    StudySession("Python", "Invalid duration", -10)
except ValueError as error:
    print("Invalid session handled:", error)


print("\n=== Experiment 13: Putting it all together ===")


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def show_roster(self):
        print("Course:", self.name)

        for student in self.students:
            print(f"- {student.name}: {student.score}/100")


python_course = Course("Python Fundamentals")

python_course.enroll(ScoredStudent("Tasnimul", 96))
python_course.enroll(ScoredStudent("Nora", 84))
python_course.enroll(ScoredStudent("Andria", 98))

python_course.show_roster()


print("\nAll 13 experiments completed!")