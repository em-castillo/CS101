people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 9999  # small
youngest_person = ''

oldest = -1  # largest
oldest_person = ''

for person in people:
    person = person.split(' ')

    age = int(person[1])  # ages
    name = person[0]  # names

    if age < youngest:
        youngest = age
        youngest_person = name

    if age > oldest:
        oldest = age
        oldest_person = name

print(f'{youngest} {youngest_person}')
print(f'{oldest} {oldest_person}')
