# This function prepares the database by dropping all existing tables and creating new ones
# according to the schema defined in the models.
def prepare_database(base, database):
    base.metadata.drop_all(database.engine)
    base.metadata.create_all(database.engine)

# This function adds initial user data to the database. It loops over a list of dictionaries containing user data,
# creates User instances from that data, and adds them to the session. After each user is added, the session is committed.
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

# This function does the same as the previous one, but for authors. It adds initial author data to the database.
def add_initial_author_data(Author, db, authors_data):
    print('Creating initial author data.')
    for author in authors_data:
        new_author = Author(
            author_first_name=author['author_first_name'],
            author_last_name=author['author_last_name']
        )
        db.session.add(new_author)
        db.session.commit()

# This function does the same for books. It adds initial book data to the database.
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

# This function adds initial review data to the database.
def add_initial_review_data(Review, db, reviews_data):
    print('Creating initial review data.')
    for review in reviews_data:
        new_review = Review(
            user_id=review['user_id'],
            book_id=review['book_id'],
            rating=review['book_rating'],
            review=review['book_review']
        )
        db.session.add(new_review)
        db.session.commit()

# This function adds initial category data to the database.
def add_initial_category_data(Category, db, categories_data):
    print('Creating initial category data.')
    for category in categories_data:
        new_category = Category(
            category_name=category['category']
        )
        db.session.add(new_category)
        db.session.commit()

# This function adds initial book-category relation data to the database.
def add_initial_book_categories_data(BookCategories, db, book_categories_data):
    print('Creating initial book categories data.')
    for book_category in book_categories_data:
        new_book_category = BookCategories(
            book_id=book_category['book_id'],
            category_id=book_category['category_id']
        )
        db.session.add(new_book_category)
        db.session.commit()
