
def prepare_database(base, database):
    base.metadata.drop_all(database.engine)
    base.metadata.create_all(database.engine)


def add_initial_user_data(User, db, users_data):
    print('Creating initial user data.')
    for user in users_data:
        new_user = User(
            user_name=user['user_name'],
            password=user['password'],
            email=user['email'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            role=user['role']
        )
        db.session.add(new_user)
        db.session.commit()

def add_initial_author_data(Author, db, authors_data):
    print('Creating initial author data.')
    for author in authors_data:
        new_author = Author(
            author_first_name=author['author_first_name'],
            author_last_name=author['author_last_name']
        )
        db.session.add(new_author)
        db.session.commit()

def add_initial_book_data(Book, db, books_data):
    print('Creating initial book data.')
    for book in books_data:
        new_book = Book(
            book_title=book['book_title'],
            page_count=book['page_count'],
            publish_date=book['publish_date'],
            price=book['price'],
            description=book['description'],
            inventory_count=book['inventory_count'],
            isbn=book['isbn'],
            author_id=book['author_id']
        )
        db.session.add(new_book)
        db.session.commit()