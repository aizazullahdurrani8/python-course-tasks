class NegativeAgeException(Exception):
    pass

def stage(age):
    if age < 0:
        raise NegativeAgeException('Age should not be Negative')
    elif 0 <= age < 13:
        print('Kid')
    elif 13 <= age < 20:
        print('Teen')
    elif 20 <= age <= 50:
        print('Young')
    else:
        print('Old')

age = int(input('Enter Your Age: '))

try:
    stage(age)
except NegativeAgeException as e:
    print(e)