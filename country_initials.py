countries = {}

for i in range(4):
    name = input('Enter Country Name: ')
    initial = name[0].upper()

    if initial not in countries:
        countries[initial] = [name]
    else:
        countries[initial].append(name)

print(countries)