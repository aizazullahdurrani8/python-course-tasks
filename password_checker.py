# Input password and confirmation
pass1 = input('Enter Password: ')
pass2 = input('Confirm Password: ')

# Check for exact match
if pass1 == pass2:
    print('Yes, they are matching')
else:
    # Check if only case is different
    if pass1.casefold() == pass2.casefold():
        print('Please check for the cases and try again')
    else:
        print('No, they are not matching. Try again')