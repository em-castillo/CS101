print()

print('Enter a list of numbers, type 0 when finished.')

numbers = []
new_number = '-1'
while new_number != 0:
    new_number = int(input('Enter number: '))

    if new_number != 0:
        numbers.append(new_number)

sum = 0

for new_number in numbers:
    sum += new_number

print(f'The sum is: {sum}')

count = len(numbers)
average = sum / count
print(f'The Average is : {average}')


largest_number = max(numbers)
print(f'The largest number is: {largest_number}')


smallest_number = 9999999999999
for new_number in numbers:
    if new_number > 0 and new_number < smallest_number:
        smallest_number = new_number

print(f'The smallest positive number is: {smallest_number}')

sorted_list = sorted(numbers)

print('The sorted list is:')
for new_number in sorted_list:
    print(new_number)
