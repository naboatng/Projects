
# main.py

import geometry

# Calculate the area and circumference of a circle
radius = 5
area = geometry.circle_area(radius)
circumference = geometry.circle_circumference(radius)
print(f"Circle with radius {radius} has area: {area:.2f} and circumference: {circumference:.2f}")

# Calculate the area and perimeter of a rectangle
length = 6
width = 4
area = geometry.rectangle_area(length, width)
perimeter = geometry.rectangle_perimeter(length, width)
print(f"Rectangle with length {length} and width {width} has area: {area} and perimeter: {perimeter}")

# Calculate the area of a triangle
base = 8
height = 3
area = geometry.triangle_area(base, height)
print(f"Triangle with base {base} and height {height} has area: {area}")
