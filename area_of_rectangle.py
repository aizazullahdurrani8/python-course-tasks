# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area
area = area_of_rectangle(length, width)

# Display result
print(f"The area of the rectangle is {area}")