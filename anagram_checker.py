# Input two strings
s1 = input('Enter a String: ')
s2 = input('Enter second String: ')

# Check if lengths are different
if len(s1) != len(s2):
    print('Not Anagram')
else:
    # Check each character
    for x in s1:
        if x not in s2:
            print('Not Anagram')
            break
    else:
        print('Anagram')