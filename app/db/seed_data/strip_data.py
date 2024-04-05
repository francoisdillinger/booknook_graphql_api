import books_data

def strip_books_data(books_data):
    stripped_books_data = []
    for book in books_data:
        stripped_book = {
            'book_title': book['book_title'],
            # 'price': book['price'],
            # 'description': book['description'],
            'book_id': book['book_id']
        }
        stripped_books_data.append(stripped_book)
    return stripped_books_data

def write_stripped_books_data(stripped_books_data):
    with open("stripped_books.py", "w", encoding="utf-8") as file:
        file.write("stripped_books_data = [\n")
        for book in stripped_books_data:
            file.write("    " + str(book) + ",\n")
        file.write("]\n")


def main():
    stripped_books_data = strip_books_data(books_data.books_data)
    write_stripped_books_data(stripped_books_data)

if __name__ == "__main__":
    main()

