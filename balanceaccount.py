bank_accounts = []
name = ''
balances = []
balance = ''

print('Enter the names and balances of bank accounts (type: quit when done) ')

while name != 'quit':
    name = input('What is the name of this account?  ')

    if name != 'quit':
        balance = float(input('What is the balance?  '))
        bank_accounts.append(name)
        balances.append(balance)
print()
print('Account Information:')

total = 0
for i in range(len(bank_accounts)):
    name = bank_accounts[i]
    balance = balances[i]
    print(f"{name} - ${balance}")
    total += balances[i]  # i represents the balance list additions


average = total / len(balances)
print()
print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')

highest_name = ''
highest_balance = 0
for j in range(len(bank_accounts)):
    highest_name = bank_accounts[j]
    highest_balance = balances[j]
highest_balance = max(balances)
print(f'Highest balance: {highest_name} - ${highest_balance:.2f}')


# stretch challenge
change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balances[index] = new_amount

    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(name)):
        print(f"{i}. {name[i]} - ${balances[i]:.2f}")
