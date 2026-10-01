# data_structures/tuples.py

# Tuples are immutable ordered collections
coordinates = (10.0, 20.0, 30.0)

print(f"Tuple: {coordinates}")
print(f"X coordinate: {coordinates[0]}")

# Tuple Unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# Immutability Demonstration
try:
    coordinates[0] = 15.0
except TypeError as e:
    print(f"Caught expected error: {e}")