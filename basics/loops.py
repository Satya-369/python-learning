# basics/loops.py

# For Loop - Iterating over a range
print("--- For Loop (range) ---")
for i in range(1, 5):
    print(f"Iteration {i}")

# For Loop - Iterating over a list
print("\n--- For Loop (list) ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While Loop with Break and Continue
print("\n--- While Loop ---")
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping 3 (continue)")
        continue
    print(f"Count: {count}")