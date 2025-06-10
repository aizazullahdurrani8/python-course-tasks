# Input full card number
cardno = input('Enter Card No: ')

# Extract last 4 digits
lastDigits = cardno[15:]

# Create masked portion
four = '*' * 4 + ' '
dispno = four * 3 + lastDigits

# Display masked card number
print(dispno)