from graphene import ObjectType, String, Int, List, Field
# from app.db.database import db
# from app.db.models import User, Author, Book


class UserObject(ObjectType):
    user_name = String()
    password = String()
    email = String()
    first_name = String()
    last_name = String()
    role = String()
    reviews = List(lambda: ReviewObject)

    # Field-level Resolver
    def resolve_reviews(root, info):
        return root.reviews


class AuthorObject(ObjectType):
    author_first_name = String()
    author_last_name = String()
    books = List(lambda: BookObject)

    # Field-level Resolver
    def resolve_books(root, info):
        # This is how you would do it without the back_populates relationship
        # books = db.session.query(Book).filter(Book.author_id == root.id).all()
        # db.session.close()
        # return books

        # This is how you would do it with the back_populates relationship specified in the Book model
        return root.books


class BookObject(ObjectType):
    book_title = String()
    page_count = Int()
    publish_date = String()
    price = Int()
    description = String()
    inventory_count = Int()
    isbn = String()
    author = Field(lambda: AuthorObject)
    book_reviews = List(lambda: ReviewObject)
    book_categories = List(lambda: BookCategoriesObject)

    # Field-level Resolver
    def resolve_author(root, info):
        # This is how you would do it without the back_populates relationship
        # author = db.session.query(Author).filter(Author.id == root.author_id).first()
        # db.session.close()
        # return author

        # This is how you would do it with the back_populates relationship specified in the Author model
        return root.author
    
    def resolve_book_reviews(root, info):
        return root.book_reviews

        # Field-level Resolver
    def resolve_book_categories(root, info):
        return root.book_categories
    
class ReviewObject(ObjectType):
    user = Field(lambda: UserObject)
    rating = Int()
    review = String()
    book = Field(lambda: BookObject)

    # Field-level Resolver
    def resolve_user(root, info):
        return root.user

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book


class CategoryObject(ObjectType):
    category_name = String()
    books = List(lambda: BookObject)

    # Field-level Resolver
    def resolve_books(root, info):
        return root.books

class BookCategoriesObject(ObjectType):
    book_id = Int()
    category_id = Int()
    book = Field(lambda: BookObject)
    category = Field(lambda: CategoryObject)

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book

    # Field-level Resolver
    def resolve_category(root, info):
        return root.category