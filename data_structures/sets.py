# data_structures/sets.py

# Sets store unique, unordered elements
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Set Operations
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")

# Adding and Removing
set_a.add(10)
set_a.discard(1)  # Discard removes without throwing error if absent
print(f"Modified Set A: {set_a}")