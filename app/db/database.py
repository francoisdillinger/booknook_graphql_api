from flask_sqlalchemy import SQLAlchemy
from app.utils.utils import add_initial_user_data, add_initial_author_data, add_initial_book_data, add_initial_review_data, prepare_database, add_initial_category_data, add_initial_book_categories_data
from app.db.models import Base, User, Author, Book, Review, Categories, BookCategories
from app.db.seed_data.users_data import users_data
from app.db.seed_data.authors_data import authors_data
from app.db.seed_data.books_data import books_data
from app.db.seed_data.book_reviews_data import reviews_data
from app.db.seed_data.category_data import category_data
from app.db.seed_data.book_category_data import book_category_data

db = SQLAlchemy()

def create_database(app):
    with app.app_context():
        db.init_app(app)
        prepare_database(Base, db)
        add_initial_user_data(User, db, users_data)
        add_initial_author_data(Author, db, authors_data)
        add_initial_book_data(Book, db, books_data)
        add_initial_review_data(Review, db, reviews_data)
        add_initial_category_data(Categories, db, category_data)
        add_initial_book_categories_data(BookCategories, db, book_category_data)    
