# all books
max_chapters = 0
largest_book = ''

with open('books_and_chapters.txt') as scriptures:
    for line in scriptures:
        line = line.strip()
        parts = line.split(':')
        book = parts[0]
        chapter = int(parts[1])
        main_book = parts[2]

        print(f'Scripture: {main_book}, Book: {book}, Chapter: {chapter}')

        if chapter > max_chapters:
            max_chapters = chapter
            largest_book = book

print()
print(f'The book with the most chapters is : {largest_book}')
print(f'It has {max_chapters} chapters')
print()

# Book of mormon
max_chapters = 0
largest_book = ''

with open('books_and_chapters.txt') as scriptures:
    for line in scriptures:
        line = line.strip()
        parts = line.split(':')
        book = parts[0]
        chapter = int(parts[1])
        main_book = parts[2]

        if main_book == 'Book of Mormon':
            print(f'Scripture: {main_book}, Book: {book}, Chapter: {chapter}')

            if chapter > max_chapters:
                max_chapters = chapter
                largest_book = book

print()
print(f'The book with the most chapters is : {largest_book}')
print(f'It has {max_chapters} chapters')

# book chosen
max_chapters = 0
largest_book = ''

volume_choice = input(
    'Which volume of scripture would you like to learn about? ')


with open('books_and_chapters.txt') as scriptures:
    for line in scriptures:
        line = line.strip()
        parts = line.split(':')
        book = parts[0]
        chapter = int(parts[1])
        main_book = parts[2]

        if main_book == volume_choice:
            print(f'Scripture: {main_book}, Book: {book}, Chapter: {chapter}')

            if chapter > max_chapters:
                max_chapters = chapter
                largest_book = book

print()
print(
    f'The book in {volume_choice} with the most chapters is : {largest_book}')
print(f'It has {max_chapters} chapters')
