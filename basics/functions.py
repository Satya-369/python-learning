# basics/functions.py

# Function Definition and Parameters
def greet(name, greeting="Hello"):
    """Returns a formatted greeting message."""
    return f"{greeting}, {name}!"

# Function with Multiple Return Values
def calculate_rectangle(width, height):
    """Calculates area and perimeter of a rectangle."""
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

# Executing functions
print(greet("Alice"))
print(greet("Bob", greeting="Welcome"))

rect_area, rect_perm = calculate_rectangle(5, 10)
print(f"Rectangle Area: {rect_area}, Perimeter: {rect_perm}")