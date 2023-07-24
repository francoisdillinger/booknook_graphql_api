import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import User
from app.graphQL.mutations import AddUser, UpdateUser, DeleteUser

def test_add_user_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Create a new instance of your mutation
        mutation = AddUser()

        # Test data for a new user
        test_user_data = {
            "user_name": "testuser",
            "password": "testpassword",
            "email": "testemail@test.com",
            "first_name": "Test",
            "last_name": "User",
            "role": "Test Role"
        }

        # Call the mutation
        result = mutation.mutate(None, **test_user_data)


        # Assert that a user was added to the session
        assert len(db.session.query(User).all()) == 1

        # Check that the user data in the database matches the test data
        added_user = db.session.query(User).first()
        for key in test_user_data:
            assert getattr(added_user, key) == test_user_data[key]

        # Check that the mutation's return value matches the added user
        assert result.user == added_user

        db.session.rollback()  # Roll back the session to clean up the test


def test_update_user_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Create a new instance of your AddUser mutation and add a user
        add_user_mutation = AddUser()
        test_user_data = {
            "user_name": "testuser",
            "password": "testpassword",
            "email": "testemail@test.com",
            "first_name": "Test",
            "last_name": "User",
            "role": "Test Role"
        }
        add_result = add_user_mutation.mutate(None, **test_user_data)
        added_user = add_result.user

        # Create a new instance of your UpdateUser mutation and update the user
        update_user_mutation = UpdateUser()
        test_updated_data = {
            "user_id": added_user.id,  # Use 'id' instead of 'user_id'
            "user_name": "updateduser",
            "password": "updatedpassword",
            "email": "updatedemail@test.com",
            "first_name": "Updated",
            "last_name": "User",
            "role": "Updated Role"
        }
        update_result = update_user_mutation.mutate(None, **test_updated_data)
        updated_user = update_result.user

        # Check that the user data in the database matches the updated data
        db_updated_user = db.session.query(User).filter(User.id == added_user.id).first()
        for key in test_updated_data:
            # Skip checking the user_id and password, as they should not be directly compared
            if key not in ["user_id", "password"]:
                assert getattr(db_updated_user, key) == test_updated_data[key]

        db.session.rollback()  # Roll back the session to clean up the test


def test_delete_user_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Create a new instance of your AddUser mutation and add a user
        add_user_mutation = AddUser()
        test_user_data = {
            "user_name": "testuser",
            "password": "testpassword",
            "email": "testemail@test.com",
            "first_name": "Test",
            "last_name": "User",
            "role": "Test Role"
        }
        add_result = add_user_mutation.mutate(None, **test_user_data)
        added_user = add_result.user

        # Assert that a user was added to the session
        assert len(db.session.query(User).all()) == 1

        # Create a new instance of your DeleteUser mutation and delete the user
        delete_user_mutation = DeleteUser()
        test_delete_data = {
            "user_id": added_user.id
        }
        delete_result = delete_user_mutation.mutate(None, **test_delete_data)

        # Assert that the returned user matches the user we deleted
        assert delete_result.user == added_user

        # Assert that no users remain in the database
        assert len(db.session.query(User).all()) == 0

        db.session.rollback()  # Roll back the session to clean up the test
