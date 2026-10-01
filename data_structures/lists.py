# data_structures/lists.py

# List Operations
numbers = [10, 20, 30, 40, 50]

# Accessing and Slicing
print(f"Original List: {numbers}")
print(f"First element: {numbers[0]}")
print(f"Slice (index 1 to 3): {numbers[1:4]}")

# Modifying Lists
numbers.append(60)         # Add to end
numbers.insert(2, 25)      # Insert at index 2
print(f"After append & insert: {numbers}")

removed_val = numbers.pop() # Remove last element
numbers.remove(25)         # Remove specific value
print(f"After pop ({removed_val}) & remove (25): {numbers}")

# Sorting
numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")