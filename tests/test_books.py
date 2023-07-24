import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import Author, Book
from app.graphQL.mutations import AddAuthor, AddBook, UpdateBook, DeleteBook


def test_add_book_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Test data for a new author
        new_author_data = {
            "author_first_name": "Test",
            "author_last_name": "Author"
        }

        # Create a new instance of your AddAuthor mutation
        add_author_mutation = AddAuthor()
        # Call the mutation
        add_author_mutation.mutate(None, **new_author_data)

        # Check that an author was added to the session
        assert len(db.session.query(Author).all()) == 1
        added_author = db.session.query(Author).first()

        # Test data for a new book
        new_book_data = {
            "book_title": "Test Book",
            "page_count": 100,
            "publish_date": "2023-07-24",
            "price": 20,
            "description": "This is a test book",
            "inventory_count": 10,
            "isbn": "1234567890",
            "author_id": added_author.id
        }

        # Create a new instance of your AddBook mutation
        add_book_mutation = AddBook()
        # Call the mutation
        result = add_book_mutation.mutate(None, **new_book_data)

        # Check that a book was added to the session
        assert len(db.session.query(Book).all()) == 1

        # Check that the book data in the database matches the test data
        added_book = db.session.query(Book).first()
        for key in new_book_data:
            assert getattr(added_book, key) == new_book_data[key]

        # Check that the mutation's return value matches the added book
        assert result.book == added_book

        db.session.rollback()  # Roll back the session to clean up the test


def test_update_book_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Test data for a new author
        new_author_data = {
            "author_first_name": "Test",
            "author_last_name": "Author"
        }

        # Create a new instance of your AddAuthor mutation
        add_author_mutation = AddAuthor()
        # Call the mutation
        add_author_mutation.mutate(None, **new_author_data)

        # Test data for a new book
        new_book_data = {
            "book_title": "Test Book",
            "page_count": 100,
            "publish_date": "2023-07-24",
            "price": 20,
            "description": "This is a test book",
            "inventory_count": 10,
            "isbn": "1234567890",
            "author_id": db.session.query(Author).first().id
        }

        # Create a new instance of your AddBook mutation
        add_book_mutation = AddBook()
        # Call the mutation
        add_book_mutation.mutate(None, **new_book_data)

        # Check that a book was added to the session
        assert len(db.session.query(Book).all()) == 1
        added_book = db.session.query(Book).first()

        # Test data for updating the book
        update_book_data = {
            "book_id": added_book.id,
            "book_title": "Updated Book",
            "page_count": 200,
            "publish_date": "2024-07-24",
            "price": 30,
            "description": "This is an updated test book",
            "inventory_count": 20,
            "isbn": "0987654321"
        }

        # Create a new instance of your UpdateBook mutation
        update_book_mutation = UpdateBook()
        # Call the mutation
        result = update_book_mutation.mutate(None, **update_book_data)

        # Check that the book data in the database matches the updated data
        updated_book = db.session.query(Book).first()
        for key in update_book_data:
            if key != "book_id":  # skip comparing the book_id
                assert getattr(updated_book, key) == update_book_data[key]

        # Check that the mutation's return value matches the updated book
        assert result.book == updated_book

        db.session.rollback()  # Roll back the session to clean up the test


def test_delete_book_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Test data for a new author
        new_author_data = {
            "author_first_name": "Test",
            "author_last_name": "Author"
        }

        # Create a new instance of your AddAuthor mutation
        add_author_mutation = AddAuthor()
        # Call the mutation
        add_author_mutation.mutate(None, **new_author_data)

        # Test data for a new book
        new_book_data = {
            "book_title": "Test Book",
            "page_count": 100,
            "publish_date": "2023-07-24",
            "price": 20,
            "description": "This is a test book",
            "inventory_count": 10,
            "isbn": "1234567890",
            "author_id": db.session.query(Author).first().id
        }

        # Create a new instance of your AddBook mutation
        add_book_mutation = AddBook()
        # Call the mutation
        add_book_mutation.mutate(None, **new_book_data)

        # Check that a book was added to the session
        assert len(db.session.query(Book).all()) == 1

        # Get the book to be deleted
        book_to_delete = db.session.query(Book).first()

        # Test deleting the book
        delete_book_mutation = DeleteBook()
        result = delete_book_mutation.mutate(None, book_id=book_to_delete.id)

        # Check that the book was deleted from the session
        assert len(db.session.query(Book).all()) == 0

        # Check that the mutation's return value matches the deleted book
        assert result.book == book_to_delete

        db.session.rollback()  # Roll back the session to clean up the test
