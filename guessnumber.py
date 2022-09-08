import random

magic_number = random.randint(1, 10)  # random number between 1 - 10
number = ""

while number != magic_number:

    number = int(input("What is your guess? "))
    if number > magic_number:
        print('Lower')
    elif number < magic_number:
        print('Higher')

    else:
        print('You guessed it!')
