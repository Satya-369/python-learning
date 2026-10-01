# basics/variables.py

# Variable Assignments & Data Types
age = 25                   # Integer
height = 5.9               # Float
name = "Alice"             # String
is_student = True          # Boolean

# Outputting values and types
print(f"Name: {name} (Type: {type(name).__name__})")
print(f"Age: {age} (Type: {type(age).__name__})")
print(f"Height: {height} (Type: {type(height).__name__})")
print(f"Is Student: {is_student} (Type: {type(is_student).__name__})")

# Type Casting
age_str = str(age)
height_int = int(height)
print(f"\nConverted age to string: '{age_str}'")
print(f"Converted height to integer: {height_int}")