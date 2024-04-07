from sqlalchemy.orm import declarative_base
from sqlalchemy import UUID, Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM

Base = declarative_base()

order_status_enum = ENUM('Processing', 'Shipped', 'Delivered', name='order_status_enum', metadata=Base.metadata)

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_name = Column(String)
    # -----------------------------------------------------------------------------------------------------
    # Might want to change this to hashed_password
    # -----------------------------------------------------------------------------------------------------
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)

    # Relations
    reviews = relationship('Review', back_populates='user')
    cart = relationship('Cart', back_populates='user')
    orders = relationship('Order', back_populates='user')
    wish_list = relationship('WishList', back_populates='user')

class Author(Base):
    __tablename__ = 'authors'

    id = Column(UUID(as_uuid=True), primary_key=True)
    author_first_name = Column(String)
    author_last_name = Column(String)

    # Relations
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    book_title = Column(String)
    page_count = Column(Integer)
    publish_date = Column(String)
    price = Column(Numeric(10, 2))
    description = Column(String)
    inventory_count = Column(Integer)
    isbn = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey('authors.id'))
    
    # Relations
    author = relationship('Author', back_populates='books')
    book_reviews = relationship('Review', back_populates='book')
    book_categories = relationship('BookCategories', back_populates='book')
    cart_book = relationship('Cart', back_populates='book')
    book_orders = relationship('Order', back_populates='book')
    wish_list_book = relationship('WishList', back_populates='book')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    book_id = Column(UUID(as_uuid=True), ForeignKey('books.id'))
    rating = Column(Integer)
    review = Column(String)
    short_review = Column(String)
    
    # Relations
    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='book_reviews')

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(UUID(as_uuid=True), primary_key=True)
    category_name = Column(String)
    
    # Relations
    book_categories = relationship('BookCategories', back_populates='category')
    books = relationship('Book', secondary='book_categories')

class BookCategories(Base):
    __tablename__ = 'book_categories'

    id = Column(UUID(as_uuid=True), primary_key=True)
    book_id = Column(UUID(as_uuid=True), ForeignKey('books.id'))
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'))
    
    # Relations
    book = relationship('Book', back_populates='book_categories')
    category = relationship('Categories', back_populates='book_categories')

class Cart(Base):
    __tablename__ = 'cart'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    book_id = Column(UUID(as_uuid=True), ForeignKey('books.id'))
    quantity = Column(Integer)
    
    # Relations
    user = relationship('User', back_populates='cart')
    book = relationship('Book', back_populates='cart_book')

class Order(Base):
    __tablename__ = 'orders'

    # This also has an 'id' for uniqueness but 'order_id' is a shared id by items of same order
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(UUID(as_uuid=True))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    book_id = Column(UUID(as_uuid=True), ForeignKey('books.id'))
    quantity = Column(Integer)
    order_date = Column(String)
    order_amount = Column(Numeric(10, 2))
    order_status = Column(order_status_enum)
    
    # Relations
    user = relationship('User', back_populates='orders')
    book = relationship('Book', back_populates='book_orders')

class WishList(Base):
    __tablename__ = 'wish_list'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    book_id = Column(UUID(as_uuid=True), ForeignKey('books.id'))
    
    # Relations
    user = relationship('User', back_populates='wish_list')
    book = relationship('Book', back_populates='wish_list_book')
    # Remember to create relationships for user and book to wishlist