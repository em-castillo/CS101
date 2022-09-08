action = [1, 2, 3, 4, 5]
products = []
total = 0
prices = []

print('Welcome to the Shopping Cart Program!')
print()


while products != 5:
    print()
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print()
    action = int(input('Please enter an action: '))

    if action > 5:
        print('Please enter a given number.')
        print()

# Add item
    if action == 1:
        item = str(input('What item would you like to add? '))
        value = float(input(f'What is the price of "{item}"? $'))
        print(f'"{item.capitalize()}" has been added to the cart.')
        products.append(item)
        prices.append(value)

# View cart
    elif action == 2:
        print('The contents of the shopping cart are: ')

        for i in range(len(products)):
            item = products[i]
            value = prices[i]
            i += 1
            print(f"{i}. {item.capitalize()} - ${value:.2f}")

# Remove item
    elif action == 3:
        index = int(input('Which item would you like to remove? '))
        index -= 1

        if index > len(products):
            print('Sorry, that is not a valid item number.')

        else:
            products.pop(index)
            prices.pop(index)
            print('Item removed.')

# Compute total
    elif action == 4:
        for i in range(len(products)):
            item = products[i]
            value = prices[i]
            total += prices[i]
        print()
        print(
            f'The total price of the items in the shopping cart is ${total:.2f}')

        for i in range(len(products)):
            item = products[i]
            i += 1
        print(f'Items sold: {i}')

# Quit
    elif action == 5:
        print('Thank you. Have a good day!')
        break
