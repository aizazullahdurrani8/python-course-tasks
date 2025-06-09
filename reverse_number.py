# Input number from user
n = int(input("Enter a Number: "))

rev = 0
temp = abs(n)  # Handle negative numbers

# Reverse the number
while temp > 0:
    r = temp % 10
    temp = temp // 10
    rev = rev * 10 + r

# Apply original sign
if n < 0:
    rev = -rev

print("Reversed Number:", rev)