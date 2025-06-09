# Input the number of values to process
num_of_nos = int(input('Enter number of numbers: '))

Psum = 0
Nsum = 0
count = 0

# Loop to input and categorize numbers
while count < num_of_nos:
    n = int(input('Enter a number: '))
    if n > 0:
        Psum = Psum + n
    else:
        Nsum = Nsum + n
    count = count + 1

# Output the results
print('Positive Sum is', Psum)
print('Negative Sum is', Nsum)