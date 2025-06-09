# Input number from user
n = int(input('Enter a Number: '))
m = n  # Store original number

rev = 0

# Reverse the number
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

# Check if original and reversed numbers are the same
if m == rev:
    print('Number is a Palindrome')
else:
    print('Number is not a Palindrome')