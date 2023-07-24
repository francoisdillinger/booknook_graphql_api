import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import User, Author, Book, Order
from app.graphQL.mutations import AddOrder

def test_add_order_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user, book, and order to the database
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

        # Ensure that no orders exist in the database before mutation
        assert len(db.session.query(Order).all()) == 0

        # Test data for adding an order
        test_order_data = {
            "order_id": "test_order_id",
            "user_id": user.id,
            "book_id": book.id,
            "quantity": 2,
            "order_date": "2023-07-24"
        }

        # Create a new instance of your mutation
        mutation = AddOrder()

        # Call the mutation
        result = mutation.mutate(None, **test_order_data)

        # Assert that the order was added to the session
        assert len(db.session.query(Order).all()) == 1

        # Check that the order data in the database matches the test data
        added_order = db.session.query(Order).first()
        for key in test_order_data:
            assert getattr(added_order, key) == test_order_data[key]

        # Check that the mutation's return value matches the added order
        assert result.order == added_order

        db.session.rollback()  # Roll back the session to clean up the test
