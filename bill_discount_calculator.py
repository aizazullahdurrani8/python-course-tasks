# Input bill amount from user
amount = float(input('Enter Bill Amount: '))

# Calculate discount based on amount
if amount <= 1000:
    discount = amount * 10 / 100
elif amount > 1000 and amount <= 5000:
    discount = amount * 20 / 100
elif amount > 5000 and amount <= 10000:
    discount = amount * 30 / 100
else:
    discount = amount * 50 / 100

# Calculate amount to be paid
discamount = amount - discount

# Display payable amount
print('Pay', discamount)