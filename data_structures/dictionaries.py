# data_structures/dictionaries.py

# Key-Value Pair Storage
student = {
    "name": "Alex",
    "age": 21,
    "courses": ["Math", "CS"]
}

print(f"Student dict: {student}")
print(f"Name: {student.get('name')}")

# Adding and updating keys
student["grade"] = "A"
student["age"] = 22

# Iterating over dictionary
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")