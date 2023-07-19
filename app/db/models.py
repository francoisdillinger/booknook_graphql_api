from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_first_name = Column(String)
    author_last_name = Column(String)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_title = Column(String)
    page_count = Column(Integer)
    publish_date = Column(String)
    price = Column(Integer)
    description = Column(String)
    inventory_count = Column(Integer)
    isbn = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    # Relations
    author = relationship('Author', back_populates='books')
    book_categories = relationship('BookCategories', back_populates='book')

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String)
    
    # Relations
    book_categories = relationship('BookCategories', back_populates='category')
    books = relationship('Book', secondary='book_categories')

class BookCategories(Base):
    __tablename__ = 'book_categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    # Relations
    book = relationship('Book', back_populates='book_categories')
    category = relationship('Categories', back_populates='book_categories')
