"""Python Playground — Lesson 15: Study Tracker Capstone."""

from pathlib import Path
import json


# Keep this project's data separate from Lesson 13.
SCRIPT_FOLDER = Path(__file__).resolve().parent
DATA_FOLDER = SCRIPT_FOLDER / "lesson_15_data"
DATA_FILE = DATA_FOLDER / "study_sessions.json"


class StudySession:
    """Represent one study session."""

    def __init__(self, subject, topic, minutes):
        subject = subject.strip()
        topic = topic.strip()

        if not subject:
            raise ValueError("Subject cannot be empty.")

        if not topic:
            raise ValueError("Topic cannot be empty.")

        if isinstance(minutes, bool) or not isinstance(minutes, int):
            raise ValueError("Minutes must be a whole number.")

        if minutes <= 0:
            raise ValueError("Minutes must be greater than zero.")

        self.subject = subject
        self.topic = topic
        self.minutes = minutes

    def to_dict(self):
        """Convert this session into a dictionary for JSON."""
        return {
            "subject": self.subject,
            "topic": self.topic,
            "minutes": self.minutes,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a session from a dictionary."""
        if not isinstance(data, dict):
            raise ValueError("A session must be a dictionary.")

        return cls(
            subject=data["subject"],
            topic=data["topic"],
            minutes=data["minutes"],
        )

    def __str__(self):
        return (
            f"{self.subject} — {self.topic} "
            f"({self.minutes} minutes)"
        )


class StudyTracker:
    """Manage study sessions and their summaries."""

    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        """Add a valid StudySession object."""
        if not isinstance(session, StudySession):
            raise TypeError("Expected a StudySession object.")

        self.sessions.append(session)

    def list_sessions(self):
        """Return all recorded sessions."""
        return self.sessions.copy()

    def total_minutes(self):
        """Calculate total study time in minutes."""
        return sum(session.minutes for session in self.sessions)

    def subject_totals(self):
        """Calculate study time grouped by subject."""
        totals = {}

        for session in self.sessions:
            totals[session.subject] = (
                totals.get(session.subject, 0) + session.minutes
            )

        return totals


def run_foundation_test():
    """Test the basic session and tracker features."""
    tracker = StudyTracker()

    tracker.add_session(StudySession("Physics", "Laws of Motion", 45))
    tracker.add_session(StudySession("Python", "Classes", 60))
    tracker.add_session(StudySession("Physics", "Work and Energy", 30))

    print("=" * 40)
    print("PYTHON PLAYGROUND — STUDY TRACKER")
    print("=" * 40)

    print("\nRecorded sessions:")

    for number, session in enumerate(tracker.list_sessions(), start=1):
        print(f"{number}. {session}")

    print("\nStudy summary:")
    print("Total sessions:", len(tracker.list_sessions()))
    print("Total minutes:", tracker.total_minutes())

    hours, minutes = divmod(tracker.total_minutes(), 60)
    print(f"Total time: {hours} hours and {minutes} minutes")

    print("\nTime by subject:")

    for subject, total in tracker.subject_totals().items():
        print(f"{subject}: {total} minutes")

    print("\nFoundation test completed successfully!")


if __name__ == "__main__":
    run_foundation_test()