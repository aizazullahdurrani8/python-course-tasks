# Input marks for three subjects
math = int(input('Enter Maths Marks: '))
phy = int(input('Enter Physics Marks: '))
chem = int(input('Enter Chemistry Marks: '))

# Check if marks in all subjects are at least 45
if math >= 45 and phy >= 45 and chem >= 45:
    print('Passed')
else:
    print('Failed')