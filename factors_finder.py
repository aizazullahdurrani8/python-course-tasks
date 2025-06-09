# Input number from user
num = int(input("Enter a number: "))

print(f"Factors of {num} are:")

# Loop to find factors
for i in range(1, num + 1):
    if num % i == 0:
        print(i)