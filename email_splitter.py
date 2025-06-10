# Input email ID from user
emailid = input('Enter email id: ')

# Find index of '@' symbol
atrate = emailid.find('@')

# Display position of '@' (optional)
print(atrate)

# Extract and display user ID and domain name
print('User ID:', emailid[:atrate])
print('Domain Name:', emailid[atrate + 1:])