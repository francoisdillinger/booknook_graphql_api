import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import User, Author, Book, Review
from app.graphQL.mutations import AddReview, UpdateReview, DeleteReview


def test_add_review_mutation():
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

        # Ensure that no reviews exist in the database before mutation
        assert len(db.session.query(Review).all()) == 0

        # Test data for adding a review
        test_review_data = {
            "user_id": user.id,
            "book_id": book.id,
            "rating": 5,
            "review": "This book is amazing!"
        }

        # Create a new instance of your mutation
        mutation = AddReview()

        # Call the mutation
        result = mutation.mutate(None, **test_review_data)

        # Assert that the review was added to the session
        assert len(db.session.query(Review).all()) == 1

        # Check that the review data in the database matches the test data
        added_review = db.session.query(Review).first()
        for key in test_review_data:
            assert getattr(added_review, key) == test_review_data[key]

        # Check that the mutation's return value matches the added review
        assert result.review == added_review

        db.session.rollback()  # Roll back the session to clean up the test


def test_update_review_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user, book, and review to the database
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

        review = Review(user_id=user.id, book_id=book.id, rating=4, review="This book is good.")
        db.session.add(review)
        db.session.commit()
        db.session.refresh(review)

        # Test data for updating the review
        test_review_data = {
            "id": review.id,
            "rating": 5,
            "review": "This book is excellent!"
        }

        # Create a new instance of your mutation
        mutation = UpdateReview()

        # Call the mutation
        result = mutation.mutate(None, **test_review_data)

        # Get the updated review from the database
        updated_review = db.session.query(Review).filter(Review.id == review.id).first()

        # Check that the review data in the database matches the updated data
        for key in test_review_data:
            assert getattr(updated_review, key) == test_review_data[key]

        # Check that the mutation's return value matches the updated review
        assert result.review == updated_review

        db.session.rollback()  # Roll back the session to clean up the test


def test_delete_review_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Add a user, book, and review to the database
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

        review = Review(user_id=user.id, book_id=book.id, rating=4, review="This book is good.")
        db.session.add(review)
        db.session.commit()
        db.session.refresh(review)

        # Ensure that a review record exists in the database
        assert len(db.session.query(Review).all()) == 1

        # Test data for deleting the review
        test_review_data = {
            "review_id": review.id
        }

        # Create a new instance of your mutation
        mutation = DeleteReview()

        # Call the mutation
        result = mutation.mutate(None, **test_review_data)

        # Assert that no review records are left in the session
        assert len(db.session.query(Review).all()) == 0

        # Check that the mutation's return value matches the deleted review
        assert result.review == review

        db.session.rollback()  # Roll back the session to clean up the test
