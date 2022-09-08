integer1 = int(input('What is the first number? '))
integer2 = int(input('What is the second number? '))

if integer1 > integer2:
    print('The first number is greater.')
else:
    print('The first number is not greater.')

if integer1 == integer2:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')

if integer1 < integer2:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

print()
animal = input('What is your favorite animal? ')

if animal.lower() == 'cat':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')
