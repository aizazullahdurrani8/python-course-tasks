# Original 3x4 matrix
L1 = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4]]

# Initialize empty list for transpose (4x3 matrix)
L2 = []

# Loop through columns of original matrix
for i in range(4):
    s = []
    # Loop through rows of original matrix
    for j in range(3):
        s.append(L1[j][i])  # Append element from L1[j][i]
    L2.append(s)

# Print the transposed matrix
print(L2)