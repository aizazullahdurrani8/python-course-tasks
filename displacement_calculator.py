# Input from user
u = float(input('Enter initial velocity: '))
v = float(input('Enter final velocity: '))
a = float(input('Enter acceleration: '))

# Calculate displacement using the formula: d = (v² - u²) / (2a)
d = (v**2 - u**2) / (2 * a)

# Display result
print("Displacement is", d)