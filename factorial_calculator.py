# Input number from user
n = int(input("Enter a non-negative integer: "))

# Initialize factorial
factorial = 1

# Calculate factorial
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}")