# Define two lists
L1 = [10, 15, 6, 9, 12, 8, 4]
L2 = [14, 6, 19, 4, 7, 10, 11]

# List to store common elements
L3 = []

# Find and store common elements
for x in L1:
    if x in L2:
        L3.append(x)

# Display the result
print(L3)