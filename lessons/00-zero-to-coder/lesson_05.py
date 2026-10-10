
# Lesson 5: Loops — Teach Python to Repeat

print("=== Experiment 1: A for loop ===")

for number in range(5):
    print(number)

print("\n=== Experiment 2: Count backwards ===")

for number in range(5, 0, -1):
    print(number)

print("\n=== Experiment 3: Accumulate stars ===")

stars = 0

for level in range(1, 4):
    stars += 2
    print(f"Level {level}: {stars} stars")

print("\n=== Experiment 4: A while loop ===")

energy = 3

while energy > 0:
    print(f"Energy remaining: {energy}")
    energy -= 1

print("Out of energy!")

print("\n=== Experiment 5: Multiplication table ===")

number = 7

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

print("\n=== Experiment 6: Continue ===")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)