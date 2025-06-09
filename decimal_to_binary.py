# Input decimal number from user
dec = int(input("Enter a Decimal Number: "))

# Convert to binary using built-in function
binary = bin(dec)[2:]

# Display binary representation
print("Binary Equivalent:", binary)