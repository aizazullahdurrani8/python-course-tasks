# Define two lists
L1 = [3, 5, 12, 6, 4]
L2 = [12, 4, 5, 3, 15, 11, 6]

# Find the length of the longer list
largest = len(L1) if len(L1) > len(L2) else len(L2)

# Display result
print(largest)