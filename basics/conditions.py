# basics/conditions.py

# Control Flow with Conditional Statements
score = 85

print(f"Evaluating score: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# Logical Operators (and, or, not)
has_passed = score >= 70
has_honors = score >= 90

if has_passed and not has_honors:
    print("Status: Passed successfully!")