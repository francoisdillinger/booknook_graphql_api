import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import User, Author, Book, Cart
from app.graphQL.mutations import AddCart, UpdateCart, DeleteCart


def test_add_cart_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user, book, and cart to the database
        user = User(first_name="Test User First Name", last_name="Test User Last Name", email="test@test.com")
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        author = Author(author_first_name="Test Author First Name", author_last_name="Test Author Last Name")
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)

        book = Book(book_title="Test Book", page_count=100, publish_date="2023-07-24", price=10, description="Test", inventory_count=10, isbn="1234567890", author_id=author.id)
        db.session.add(book)
        db.session.commit()
        db.session.refresh(book)

        # Ensure that no cart records exist in the database yet
        assert len(db.session.query(Cart).all()) == 0

        # Test data for adding the cart
        test_cart_data = {
            "user_id": user.id,
            "book_id": book.id,
            "quantity": 1
        }

        # Create a new instance of your mutation
        mutation = AddCart()

        # Call the mutation
        result = mutation.mutate(None, **test_cart_data)

        # Assert that the cart record was added to the database
        assert len(db.session.query(Cart).all()) == 1

        # Check that the mutation's return value matches the added cart
        assert result.cart == db.session.query(Cart).first()

        db.session.rollback()  # Roll back the session to clean up the test


def test_update_cart_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user, book, and cart to the database
        user = User(first_name="Test User First Name", last_name="Test User Last Name", email="test@test.com")
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        author = Author(author_first_name="Test Author First Name", author_last_name="Test Author Last Name")
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)

        book = Book(book_title="Test Book", page_count=100, publish_date="2023-07-24", price=10, description="Test", inventory_count=10, isbn="1234567890", author_id=author.id)
        db.session.add(book)
        db.session.commit()
        db.session.refresh(book)

        cart = Cart(user_id=user.id, book_id=book.id, quantity=1)
        db.session.add(cart)
        db.session.commit()
        db.session.refresh(cart)

        # Ensure that the cart record exists in the database
        assert len(db.session.query(Cart).all()) == 1

        # Test data for updating the cart
        test_cart_data = {
            "cart_id": cart.id,
            "quantity": 2
        }

        # Create a new instance of your mutation
        mutation = UpdateCart()

        # Call the mutation
        result = mutation.mutate(None, **test_cart_data)

        # Assert that the cart record was updated in the database
        updated_cart = db.session.query(Cart).first()
        assert updated_cart.quantity == 2

        # Check that the mutation's return value matches the updated cart
        assert result.cart == updated_cart

        db.session.rollback()  # Roll back the session to clean up the test


def test_delete_cart_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user, book, and cart to the database
        user = User(first_name="Test User First Name", last_name="Test User Last Name", email="test@test.com")
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        author = Author(author_first_name="Test Author First Name", author_last_name="Test Author Last Name")
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)

        book = Book(book_title="Test Book", page_count=100, publish_date="2023-07-24", price=10, description="Test", inventory_count=10, isbn="1234567890", author_id=author.id)
        db.session.add(book)
        db.session.commit()
        db.session.refresh(book)

        cart = Cart(user_id=user.id, book_id=book.id, quantity=1)
        db.session.add(cart)
        db.session.commit()
        db.session.refresh(cart)

        # Ensure that a cart record exists in the database
        assert len(db.session.query(Cart).all()) == 1

        # Test data for deleting the cart
        test_cart_data = {
            "cart_id": cart.id
        }

        # Create a new instance of your mutation
        mutation = DeleteCart()

        # Call the mutation
        result = mutation.mutate(None, **test_cart_data)

        # Assert that no cart records are left in the session
        assert len(db.session.query(Cart).all()) == 0

        # Check that the mutation's return value matches the deleted cart
        assert result.cart == cart

        db.session.rollback()  # Roll back the session to clean up the test
