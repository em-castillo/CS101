# friends = []
# name = None

# while name != "end":
#     name = input("Type the name of a friend: ")

#     if name != "end":
#         friends.append(name)

# print()
# print("Your friends are:")

# for friend in friends:
#     print(friend)


name = ''
friend_names = []

while name != 'end':
    name = str(input('Type the name of a friend: '))
    friend_names.append(name)
print()

if name == 'end':
    del friend_names[-1]  # del takes lasta element out
    print('Your friends are: ')

for name in friend_names:
    print(name)
