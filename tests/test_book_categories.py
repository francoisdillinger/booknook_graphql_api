import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import Author, Book, Categories, BookCategories
from app.graphQL.mutations import AddBookCategory, DeleteBookCategories


def test_delete_book_categories_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add an author to the database
        author = Author(author_first_name="Test Author First Name", author_last_name="Test Author Last Name")
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)

        # Add a book, category and book_category to the database
        book = Book(book_title="Test Book", page_count=100, publish_date="2023-07-24", price=10, description="Test", inventory_count=10, isbn="1234567890", author_id=1)
        db.session.add(book)
        db.session.commit()
        db.session.refresh(book)

        category = Categories(category_name="Test Category")
        db.session.add(category)
        db.session.commit()
        db.session.refresh(category)

        book_category = BookCategories(book_id=book.id, category_id=category.id)
        db.session.add(book_category)
        db.session.commit()
        db.session.refresh(book_category)

        # Ensure that a book_category record exists in the database
        assert len(db.session.query(BookCategories).all()) == 1

        # Test data for deleting the book_category
        test_book_category_data = {
            "book_id": book.id
        }

        # Create a new instance of your mutation
        mutation = DeleteBookCategories()

        # Call the mutation
        result = mutation.mutate(None, **test_book_category_data)

        # Assert that no book_category records are left in the session
        assert len(db.session.query(BookCategories).all()) == 0

        # Check that the mutation's return value matches the deleted book_category
        assert result.book_category == book_category

        db.session.rollback()  # Roll back the session to clean up the test



def test_delete_book_categories_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add an author to the database
        author = Author(author_first_name="Test Author First Name", author_last_name="Test Author Last Name")
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)

        # Add a book, category and book_category to the database
        book = Book(book_title="Test Book", page_count=100, publish_date="2023-07-24", price=10, description="Test", inventory_count=10, isbn="1234567890", author_id=1)
        db.session.add(book)
        db.session.commit()
        db.session.refresh(book)

        category = Categories(category_name="Test Category")
        db.session.add(category)
        db.session.commit()
        db.session.refresh(category)

        book_category = BookCategories(book_id=book.id, category_id=category.id)
        db.session.add(book_category)
        db.session.commit()
        db.session.refresh(book_category)

        # Ensure that a book_category record exists in the database
        assert len(db.session.query(BookCategories).all()) == 1

        # Test data for deleting the book_category
        test_book_category_data = {
            "book_id": book.id
        }

        # Create a new instance of your mutation
        mutation = DeleteBookCategories()

        # Call the mutation
        result = mutation.mutate(None, **test_book_category_data)

        # Assert that no book_category records are left in the session
        assert len(db.session.query(BookCategories).all()) == 0

        # Check that the mutation's return value matches the deleted book_category
        assert result.book_category == book_category

        db.session.rollback()  # Roll back the session to clean up the test
