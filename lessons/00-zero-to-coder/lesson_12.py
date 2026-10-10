
# Lesson 12: Error Handling — Practice Experiments

print("=== Experiment 1: Handling invalid integer input ===")

try:
    number = int("hello")
except ValueError:
    print("ValueError handled: 'hello' is not an integer.")

print("The program continues after the error.")


print("\n=== Experiment 2: Handling division by zero ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError handled: cannot divide by zero.")


print("\n=== Experiment 3: Handling multiple exceptions ===")

test_values = ["25", "hello", "0"]

for value in test_values:
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        print(f"{value!r}: Please provide a valid integer.")
    except ZeroDivisionError:
        print(f"{value!r}: Division by zero is not allowed.")
    else:
        print(f"{value!r}: Result = {result}")


print("\n=== Experiment 4: Understanding else ===")

try:
    score = int("85")
except ValueError:
    print("The score was invalid.")
else:
    print("The conversion succeeded.")
    print("Score:", score)


print("\n=== Experiment 5: Understanding finally ===")

try:
    print("Starting the operation.")
    result = 20 / 4
    print("Result:", result)
except ZeroDivisionError:
    print("The calculation failed.")
finally:
    print("The operation has finished.")


print("\n=== Experiment 6: Raising a ValueError ===")


def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    return price * (1 - discount_percent / 100)


print("Discounted price:", calculate_discount(1000, 20))

try:
    calculate_discount(1000, 120)
except ValueError as error:
    print("Invalid discount handled:", error)


print("\n=== Experiment 7: Validating scores ===")


def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    return score


test_scores = [85, -5, 105]

for score in test_scores:
    try:
        valid_score = validate_score(score)
    except ValueError as error:
        print(f"{score}: {error}")
    else:
        print(f"{valid_score}: Valid score.")


print("\n=== Experiment 8: Handling a missing dictionary key ===")

student = {"name": "Tasnimul", "score": 92}

try:
    print("Grade:", student["grade"])
except KeyError:
    print("The requested grade does not exist.")


print("\n=== Experiment 9: Handling an invalid list index ===")

colors = ["red", "blue", "green"]

try:
    print(colors[10])
except IndexError:
    print("That list index does not exist.")


print("\n=== Experiment 10: A reusable safe division function ===")


def safe_divide(first_number, second_number):
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return None


print("20 / 4 =", safe_divide(20, 4))
print("20 / 0 =", safe_divide(20, 0))


print("\n=== Experiment 11: Handling user input safely ===")


def get_integer(text):
    try:
        return int(text)
    except ValueError:
        return None


user_inputs = ["42", "hello", "-7", "3.14"]

for user_input in user_inputs:
    result = get_integer(user_input)

    if result is None:
        print(f"{user_input!r}: Not a valid integer.")
    else:
        print(f"{user_input!r}: Converted to {result}.")


print("\n=== Experiment 12: A complete score analyzer ===")


def analyze_score(text):
    try:
        score = int(text)
    except ValueError:
        return "Error: Enter a whole number."

    if not 0 <= score <= 100:
        return "Error: Score must be between 0 and 100."

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 50:
        category = "Developing"
    else:
        category = "Needs more practice"

    return f"Score: {score} | Category: {category}"


score_inputs = ["95", "78", "hello", "-10", "105", "42"]

for score_input in score_inputs:
    print(f"{score_input!r} -> {analyze_score(score_input)}")


print("\nAll 12 experiments completed!")