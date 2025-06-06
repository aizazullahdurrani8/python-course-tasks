# Function to calculate surface area of a cuboid
def surface_area_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

# Input from user
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

# Calculate surface area
area = surface_area_cuboid(length, width, height)

# Display result
print(f"The surface area of the cuboid is {area}")