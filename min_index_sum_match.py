# Define the two food lists
L1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
L2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

# Initialize index values to a high number
index1 = 10
index2 = 10

# Loop through items in L1
for i in range(len(L1)):
    indx = L2.index(L1[i])  # Find index of same item in L2

    # Compare index sum with current minimum
    if i + indx < index1 + index2:
        index1 = i
        index2 = indx

# Output the result
print(L1[index1], index1 + index2)