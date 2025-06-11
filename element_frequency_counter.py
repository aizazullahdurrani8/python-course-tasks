# List with repeated elements
L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']

# List to store tuples of (element, count)
result = []

# Count occurrences of each unique element
for x in L1:
    cnt = L1.count(x)
    if (x, cnt) not in result:
        result.append((x, cnt))

# Print first two elements with their counts
print(result[0:2])