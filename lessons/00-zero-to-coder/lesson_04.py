
# Lesson 4: Teach Python to Make Decisions

print("=== Experiment 1: if ===")

score = 85

if score >= 70:
    print("You passed!")

print("\n=== Experiment 2: if and else ===")

temperature = 25

if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not a hot day!")

print("\n=== Experiment 3: if, elif, and else ===")

score = 78

if score >= 90:
    print("Rank: Expert")
elif score >= 70:
    print("Rank: Skilled")
elif score >= 50:
    print("Rank: Beginner")
else:
    print("Rank: Keep practising")

print("\n=== Experiment 4: Combining conditions ===")

has_ticket = True
age = 17

if age >= 13 and has_ticket:
    print("You may enter the game zone.")
else:
    print("Entry not permitted.")

print("\n=== Experiment 5: Change the values ===")

score = 45

if score >= 90:
    print("Gold")
elif score >= 70:
    print("Silver")
elif score >= 50:
    print("Bronze")
else:
    print("Keep practising")