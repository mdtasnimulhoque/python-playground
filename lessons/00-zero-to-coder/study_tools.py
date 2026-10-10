
"""Reusable tools for student score analysis."""


def calculate_average(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def classify_score(score):
    if not 0 <= score <= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Developing"
    else:
        return "Needs more practice"


if __name__ == "__main__":
    sample_scores = [80, 90, 100]

    print("Testing study_tools")
    print("Average:", calculate_average(sample_scores))