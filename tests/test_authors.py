import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import Author
from app.graphQL.mutations import AddAuthor, UpdateAuthor, DeleteAuthor

def test_add_author_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Create a new instance of your mutation
        mutation = AddAuthor()

        # Test data for a new author
        test_author_data = {
            "author_first_name": "Test",
            "author_last_name": "Author"
        }

        # Call the mutation
        result = mutation.mutate(None, **test_author_data)

        # Assert that an author was added to the session
        assert len(db.session.query(Author).all()) == 1

        # Check that the author data in the database matches the test data
        added_author = db.session.query(Author).first()
        for key in test_author_data:
            assert getattr(added_author, key) == test_author_data[key]

        # Check that the mutation's return value matches the added author
        assert result.author == added_author

        db.session.rollback()  # Roll back the session to clean up the test


def test_update_author_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Test data for a new author
        new_author_data = {
            "author_first_name": "Original",
            "author_last_name": "Author"
        }

        # Create a new instance of your AddAuthor mutation
        add_mutation = AddAuthor()
        # Call the mutation
        add_mutation.mutate(None, **new_author_data)
        added_author = db.session.query(Author).first()

        # Test data for update
        test_update_data = {
            "author_id": added_author.id,
            "author_first_name": "Updated",
            "author_last_name": "Author"
        }

        # Create a new instance of your UpdateAuthor mutation
        update_mutation = UpdateAuthor()
        # Call the mutation
        update_result = update_mutation.mutate(None, **test_update_data)

        # Check that the author data in the database matches the updated data
        updated_author = db.session.query(Author).first()
        for key in test_update_data:
            if key != "author_id":  # We don't want to compare the id
                assert getattr(updated_author, key) == test_update_data[key]

        # Check that the mutation's return value matches the updated author
        assert update_result.author == updated_author

        db.session.rollback()  # Roll back the session to clean up the test


def test_delete_author_mutation():
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
        add_mutation = AddAuthor()
        # Call the mutation
        add_mutation.mutate(None, **new_author_data)

        # Check that an author was added to the session
        assert len(db.session.query(Author).all()) == 1
        added_author = db.session.query(Author).first()

        # Test data for deletion
        test_delete_data = {
            "author_id": added_author.id
        }

        # Create a new instance of your DeleteAuthor mutation
        delete_mutation = DeleteAuthor()
        # Call the mutation
        delete_result = delete_mutation.mutate(None, **test_delete_data)

        # Check that no author remains in the session
        assert len(db.session.query(Author).all()) == 0

        # Check that the mutation's return value matches the deleted author
        assert delete_result.author.id == added_author.id

        db.session.rollback()  # Roll back the session to clean up the test
