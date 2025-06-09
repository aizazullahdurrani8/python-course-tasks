# Input number of terms from user
n = int(input("Enter the number of Fibonacci terms: "))

# Initialize first two terms
a, b = 0, 1
count = 0

# Generate Fibonacci sequence
while count < n:
    print(a)
    a, b = b, a + b
    count += 1