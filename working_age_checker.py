# Input age from user
age = int(input('Enter Age: '))

# Check if age is within working range
if age >= 18 and age <= 60:
    print('Eligible')
else:
    print('Not Eligible')