# Input initial term, common difference, and number of terms
a = int(input('Enter initial term: '))
d = int(input('Enter common difference: '))
n = int(input('Enter number of terms: '))

# Generate and print arithmetic progression terms
for t in range(a, a + n * d, d):
    print(t)