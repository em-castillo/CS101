def display_regular():
    print(user_message)


def display_uppercase():
    message = user_message.upper()
    print(message)


def display_lowercase():
    message = user_message.lower()
    print(message)


user_message = str(input('What is your message? '))

display_regular()
display_uppercase()
display_lowercase()
