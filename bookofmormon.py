with open('books.txt') as book_file:
    for line in book_file:
        clean_line = line.strip() #delete line spaces
        print(clean_line)
