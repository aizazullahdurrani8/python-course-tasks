import math

# Input coefficients from user
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))

# Calculate discriminant
discriminant = b**2 - 4 * a * c

# Calculate roots
root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 * a)

# Display roots
print('Roots are', root1, root2)