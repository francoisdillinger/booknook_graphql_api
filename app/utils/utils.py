import os
import jwt
# import uuid
from argon2 import PasswordHasher
from graphql import GraphQLError
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from app.db.models import User
from functools import wraps

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
TOKEN_EXPIRATION_TIME_IN_MINUTES = int(os.getenv('TOKEN_EXPIRATION_TIME_IN_MINUTES'))

# This function prepares the database by dropping all existing tables and creating new ones
# according to the schema defined in the models.
def prepare_database(base, database):
    base.metadata.drop_all(database.engine)
    base.metadata.create_all(database.engine)

# This function adds initial user data to the database. It loops over a list of dictionaries containing user data,
# creates User instances from that data, and adds them to the session. After each user is added, the session is committed.
def add_initial_user_data(User, db, users_data):
    print('Creating initial user data.')
    ph = PasswordHasher()
    for user in users_data:
        new_user = User(
            id=user['user_id'],
            user_name=user['user_name'],
            password=ph.hash(user['password']),
            email=user['email'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            role=user['role']
        )
        db.session.add(new_user)
        db.session.commit()

# This function does the same as the previous one, but for authors. It adds initial author data to the database.
def add_initial_author_data(Author, db, authors_data):
    print('Creating initial author data.')
    for author in authors_data:
        new_author = Author(
            id=author['id'],
            author_first_name=author['author_first_name'],
            author_last_name=author['author_last_name']
        )
        db.session.add(new_author)
        db.session.commit()

# This function does the same for books. It adds initial book data to the database.
def add_initial_book_data(Book, db, books_data):
    print('Creating initial book data.')
    for book in books_data:
        new_book = Book(
            id=book['book_id'],
            book_title=book['book_title'],
            page_count=book['page_count'],
            publish_date=book['publish_date'],
            price=book['price'],
            short_description=book['short_description'],
            long_description=book['long_description'],
            inventory_count=book['inventory_count'],
            isbn=book['isbn'],
            author_id=book['author_id']
        )
        db.session.add(new_book)
        db.session.commit()

# This function adds initial review data to the database.
def add_initial_review_data(Review, db, reviews_data):
    print('Creating initial review data.')
    for review in reviews_data:
        new_review = Review(
            id=review['id'],
            user_id=review['user_id'],
            book_id=review['book_id'],
            rating=review['book_rating'],
            review=review['book_review'],
            short_review=review['short_review'],
        )
        db.session.add(new_review)
        db.session.commit()

# This function adds initial category data to the database.
def add_initial_category_data(Category, db, categories_data):
    print('Creating initial category data.')
    for category in categories_data:
        new_category = Category(
            id=category['id'],
            category_name=category['category']
        )
        db.session.add(new_category)
        db.session.commit()

# This function adds initial book-category relation data to the database.
def add_initial_book_categories_data(BookCategories, db, book_categories_data):
    print('Creating initial book categories data.')
    for book_category in book_categories_data:
        new_book_category = BookCategories(
            id=book_category['id'],
            book_id=book_category['book_id'],
            category_id=book_category['category_id']
        )
        db.session.add(new_book_category)
        db.session.commit()

# This function adds initial cart data to the database.
def add_initial_cart_data(Cart, db, carts_data):
    print('Creating initial cart data.')
    for cart in carts_data:
        new_cart = Cart(
            id=cart['id'],
            user_id=cart['user_id'],
            book_id=cart['book_id'],
            quantity=cart['quantity']
        )
        db.session.add(new_cart)
        db.session.commit()


def add_initial_order_data(Order, db, orders_data):
    print('Creating initial order data.')
    for order in orders_data:
        new_order = Order(
            # id=order['order_id'],
            order_id=order['order_id'],
            user_id=order['user_id'],
            book_id=order['book_id'],
            quantity=order['quantity'],
            order_date=order['order_date'],
            order_amount = order['quantity'] * 4.95,
            order_status = "Processing",
        )
        db.session.add(new_order)
        db.session.commit()


def generate_token(email):
    expiration_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_TIME_IN_MINUTES)
    payload = {
        "sub": email,
        "exp": expiration_time
        }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def hash_password(password):
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(hashed_password, password):
    ph = PasswordHasher()

    try:
        ph.verify(hashed_password, password)
    except VerifyMismatchError:
        return GraphQLError('Invalid Email or password.')
    

def get_authenticated_user(context):
    from app.db.database import db
    auth_header = context.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            if datetime.now(timezone.utc) > datetime.fromtimestamp(payload['exp'], tz=timezone.utc):
                raise GraphQLError('Token has expired.')
            
            user = db.session.query(User).filter(User.email == payload['sub']).first()

            if not user:
                raise GraphQLError('Could not authenticate user.')
            
            return user
        except jwt.exceptions.InvalidSignatureError:
            raise GraphQLError('Invalid authentication token.')
    else:
        raise GraphQLError('No authentication token provided.')
    

def admin_user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        info = args[1]
        user = get_authenticated_user(info.context)

        if user.role != 'admin':
            raise GraphQLError('You do not have permission to perform this action.')
        return func(*args, **kwargs)
    return wrapper


def authenticated_user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        info = args[1]
        get_authenticated_user(info.context)

        return func(*args, **kwargs)
    return wrapper