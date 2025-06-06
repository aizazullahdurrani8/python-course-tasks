# Function to calculate area of a rhombus
def area_of_rhombus(d1, d2):
    return (d1 * d2) / 2

# Input from user
d1 = float(input("Enter the length of diagonal 1: "))
d2 = float(input("Enter the length of diagonal 2: "))

# Calculate area
area = area_of_rhombus(d1, d2)

# Display result
print(f"The area of the rhombus is {area}")