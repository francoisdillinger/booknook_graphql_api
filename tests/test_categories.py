import pytest
from app.main import create_app
from app.db.database import db
from app.db.models import Categories
from app.graphQL.mutations import AddCategory, UpdateCategory


def test_add_category_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Test data for a new category
        test_category_data = {
            "category_name": "Test Category"
        }

        # Create a new instance of your mutation
        mutation = AddCategory()

        # Call the mutation
        result = mutation.mutate(None, **test_category_data)

        # Assert that a category was added to the session
        assert len(db.session.query(Categories).all()) == 1

        # Check that the category data in the database matches the test data
        added_category = db.session.query(Categories).first()
        for key in test_category_data:
            assert getattr(added_category, key) == test_category_data[key]

        # Check that the mutation's return value matches the added category
        assert result.category == added_category

        db.session.rollback()  # Roll back the session to clean up the test


def test_update_category_mutation():
    # Set up test Flask app and database session
    app = create_app()
    with app.app_context():
        db.create_all()  # make sure all tables are created

        # Test data for a new category
        test_category_data = {
            "category_name": "Test Category"
        }

        # Add a category to update
        new_category = Categories(**test_category_data)
        db.session.add(new_category)
        db.session.commit()
        db.session.refresh(new_category)

        # Update data for the category
        update_category_data = {
            "category_id": new_category.id,
            "category_name": "Updated Category"
        }

        # Create a new instance of your mutation
        mutation = UpdateCategory()

        # Call the mutation
        result = mutation.mutate(None, **update_category_data)

        # Check that the category data in the database matches the updated data
        updated_category = db.session.query(Categories).filter_by(id=new_category.id).first()
        for key in update_category_data:
            if key != "category_id":  # Skip the ID in this comparison
                assert getattr(updated_category, key) == update_category_data[key]

        # Check that the mutation's return value matches the updated category
        assert result.category == updated_category

        db.session.rollback()  # Roll back the session to clean up the test
