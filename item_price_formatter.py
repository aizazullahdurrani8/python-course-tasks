# Input item name and price
item = input('Enter The Item: ')
price = input('Enter price: ')

# Calculate total length of item and price
total_len = len(item) + len(price)

# Create spacing using dots
dots = '.' * (25 - total_len)

# Display formatted output
print(item + dots + price)