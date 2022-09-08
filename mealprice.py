print("Please enter the following information.")
print()
child_meal = float(input("The price of a child's meal: $"))
adult_meal = float(input("The price of a adult's meal: $"))
child_drink = float(input("The price of a child's drink: $"))
adult_drink = float(input("The price of a adult's drink: $"))
number_children = int(input("The number of children: "))
number_adult = int(input("The number of adults: "))
tax_rate = float(input("The sales tax rate: "))
print()

total_children = (child_meal + child_drink) * number_children
total_adult = (adult_meal + adult_drink) * number_adult
subtotal = total_children + total_adult
print(f"Your subtotal is: ${subtotal:.2f}")
tax = subtotal * tax_rate / 100

print(f"Your sales tax is: ${tax: .2f}")
total = subtotal + tax

print(f"Your total is: ${total:.2f}")
print()

payment = float(input("What is the payment amount? $"))
change = payment - total
print(f"Your change is: ${change:.2f}")
print()
print(f"Thank you! Come back soon!")
