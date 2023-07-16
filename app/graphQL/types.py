from graphene import ObjectType, String, Int, List, Field
from app.db.database import users_data, authors_data, books_data


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
        return [book for book in books_data if book["author_id"] == root['id']]


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
        return [author for author in authors_data if author["id"] == root["author_id"]][0]