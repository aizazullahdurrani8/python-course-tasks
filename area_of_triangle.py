# Function to calculate area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Input from user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate area
area = area_of_triangle(base, height)

# Display result
print(f"The area of the triangle is {area}")