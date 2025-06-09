# Input how many numbers to compare
num_of_nos = int(input('Enter number of numbers: '))

count = 0

# Input the first number as initial maximum
max = int(input('Enter a number: '))

# Loop to find maximum
while count < num_of_nos - 1:
    n = int(input('Enter a number: '))
    if n > max:
        max = n
    count = count + 1

# Display the maximum number
print('Max number is', max)