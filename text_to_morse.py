# Morse code representations for letters a-j
codes = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

# Input text to convert
text = 'deface'

# Initialize empty Morse code string
morse_str = ''

# Convert each character to Morse code
for x in text:
    morse_str += codes[ord(x) - 97] + " "

# Display Morse code
print(morse_str)