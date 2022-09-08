number = int(
    input('How many columns and rows do you want in your multiplication table? '))
size = number + 1

for row in range(1, size):  # number + 1 instead of size
    for column in range(1, size):
        table = row * column
        print(f'{table:3}', end=' ')
    print()  # finish line
