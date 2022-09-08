items = ''
shopping_list = []

print('Please enter the items of the shopping list (type: quit to finish): ')

while items != 'quit':
    items = str(input('Item: '))

    if items != 'quit':
        shopping_list.append(items)

# if this section would have been in the while loop,
#     if items == 'quit', quit is displayed. This way is not.
print()
print('The shopping list is:')
for items in shopping_list:
    print(items)


print()
print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    items = shopping_list[i]
    print(f'{i}. {items}')

print()
index = int(input('Which item would you like to change? '))
new_item = str(input('What is the new item? '))

# gets the item at the index the user typed and replace it
shopping_list[index] = new_item

print()
print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    items = shopping_list[i]
    print(f'{i}. {items}')
