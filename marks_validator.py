# Input marks from user
marks = int(input('Enter Marks: '))

# Check if marks are within valid range
if marks >= 0 and marks <= 100:
    print('Valid')
else:
    print('Invalid')