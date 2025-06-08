# Input username from user
username = input('Enter Username: ')

# Check if username is authorized
if username == 'john' or username == 'smith':
    print('Authorised')
else:
    print('Not Authorised')