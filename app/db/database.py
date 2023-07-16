from flask_sqlalchemy import SQLAlchemy
from app.utils.utils import add_initial_user_data, add_initial_author_data, add_initial_book_data, prepare_database
from app.db.models import Base, User, Author, Book
from app.db.seed_data.users_data import users_data
from app.db.seed_data.authors_data import authors_data
from app.db.seed_data.books_data import books_data

db = SQLAlchemy()

def create_database(app):
    with app.app_context():
        db.init_app(app)
        prepare_database(Base, db)
        add_initial_user_data(User, db, users_data)
        add_initial_author_data(Author, db, authors_data)
        add_initial_book_data(Book, db, books_data)
