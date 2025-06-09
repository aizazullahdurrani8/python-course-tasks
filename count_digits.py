# Input number from user
num = int(input("Enter a number: "))

# Initialize digit count
count = 0
temp = abs(num)  # Handle negative numbers

# Count digits
while temp != 0:
    temp //= 10
    count += 1

print("Number of digits:", count)