import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import WishList, User, Author, Book
from app.graphQL.mutations import AddWishlist, DeleteWishlist

def test_add_wishlist_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user and book to the database
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
        

        # Create a new instance of your mutation
        mutation = AddWishlist()

        # Test data for a new wishlist
        test_wishlist_data = {
            "user_id": 1,
            "book_id": 1
        }

        # Call the mutation
        result = mutation.mutate(None, **test_wishlist_data)


        # Assert that a wishlist was added to the session
        assert len(db.session.query(WishList).all()) == 1

        # Check that the wishlist data in the database matches the test data
        added_wishlist = db.session.query(WishList).first()
        for key in test_wishlist_data:
            assert getattr(added_wishlist, key) == test_wishlist_data[key]

        # Check that the mutation's return value matches the added wishlist
        assert result.wishlist == added_wishlist

        db.session.rollback()  # Roll back the session to clean up the test

