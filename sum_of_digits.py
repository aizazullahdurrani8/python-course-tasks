# Input number from user
n = int(input('Enter a Number: '))

sum = 0
temp = abs(n)  # Handle negative numbers

# Calculate sum of digits
while temp > 0:
    r = temp % 10
    temp = temp // 10
    sum = sum + r

print('Sum of Digits is', sum)