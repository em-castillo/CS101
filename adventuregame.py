
print('Adventure Game')
print()
print('Read the promptings and write the capitalize word of your option.')
print()
choice1 = input(
    'Your mission is to find the blue gemstone. Do you want to start the adventure by HORSE or WAGON? ')
if choice1.lower() == 'horse':
    choice2 = input(
        'A wide river is on your way. Do you cross it on a BOAT or a farther BRIDGE? ')
    if choice2.lower() == 'boat':
        choice3 = input(
            'Your boat is sinking and the stream is leading to a waterfall. Do you WAIT to fall, JUMP off the boat, or SWIM to the other side? ')
        if choice3.lower() == 'wait':
            print('You survived the fall! But your mission failed.')
        elif choice3.lower() == 'jump':
            print('You found the blue gemstone under the water! Mission succeed!')
        elif choice3.lower() == 'swim':
            print('The stream took you down the waterfall. You did not survived.')
        else:
            print('Please enter one of the options given.')

    elif choice2.lower() == 'bridge':
        choice3 = input(
            'The bridge is too old and it broke while you were walking on it. Mission incompleted.')

    else:
        print('Please enter one of the options given.')

elif choice1.lower() == 'wagon':
    choice_2 = input(
        'The wagon left you next to a lake. Do you FISH or REFRESH? ')
    if choice_2.lower() == 'fish':
        choice_3 = input(
            "While eating the fish you caught you missed your mom's fried fish. Do you go HOME or you CONTINUE your mission? ")
        if choice_3.lower() == 'home':
            print('You are at home eating a delicious dinner with your family')
        elif choice_3.lower() == 'continue':
            choice_4 = input(
                'You camp during the night. Next morning you are ready to go but you are a little hungry. Do you SKIP breakfast or get some EGGS that you saw in the tree?')
            if choice_4.lower() == 'skip':
                print('You have low energy. you cannot continue your mission.')
            elif choice_4.lower() == 'eggs':
                print(
                    'You found two eggs and two blue gemstones! Mission completed! you can keep a gemstone.')
            else:
                print('Please enter one of the options given.')

        else:
            print('Please enter one of the options given.')

    elif choice_2.lower() == 'refresh':
        choice__3: input('While refreshing you see something shining in the shore. You found a red gemstone! It is not the blue one, so you can keep it.')

    else:
        print('Please enter one of the options given.')

else:
    print('Please enter one of the options given.')
