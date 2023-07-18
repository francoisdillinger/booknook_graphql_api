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

    # Field-level Resolver
    def resolve_author(root, info):
        # This is how you would do it without the back_populates relationship
        # author = db.session.query(Author).filter(Author.id == root.author_id).first()
        # db.session.close()
        # return author

        # This is how you would do it with the back_populates relationship specified in the Author model
        return root.author