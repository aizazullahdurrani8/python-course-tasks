# Input from user
no1 = int(input('Enter first number: '))
no2 = int(input('Enter second number: '))

# Calculate and display absolute difference
if no1 - no2 >= 0:
    print(no1 - no2)
else:
    print(no2 - no1)