# Original list with duplicates
L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

# List to store unique elements
L2 = []

# Loop to remove duplicates
for x in L1:
    if x not in L2:
        L2.append(x)

# Display result
print(L2)