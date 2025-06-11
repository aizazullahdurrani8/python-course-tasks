# Define two 3x4 matrices
L1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
L2 = [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]]

# Resultant matrix initialization
L3 = []

# Loop through rows
for i in range(3):
    s = []
    # Loop through columns
    for j in range(4):
        r = L1[i][j] + L2[i][j]  # Add corresponding elements
        s.append(r)
    L3.append(s)

# Print the resulting matrix
print(L3)