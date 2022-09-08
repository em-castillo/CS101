first_age = int(input('What is  the age of the first rider? '))
first_height = int(input('What is the height of the first rider? '))
second_rider = input('Is there a second rider? (Yes/No) ')
if second_rider.lower() == 'Yes':
    second_age = int(input('What is the age of the second rider? '))
    second_height = int(input('What is the height of the second rider? '))

    if first_height < 36 or second_height < 36:
        print('Your are too short. Sorry, no ride for you.')

    else:
        if first_age >= 18 or second_age >= 18:
            print('Welcome! Enjoy the ride.')
        else:
            # print('You are not old enough to ride.')
            if first_age >= 12 and first_height >= 52 and second_age >= 12 and second_height >= 52:
                print('You can ride!')
            else:
                print('You can not ride.')

else:
    if first_age >= 18 and first_height >= 62:
        print('Can ride alone.')
    else:
        print('Can not ride alone.')
