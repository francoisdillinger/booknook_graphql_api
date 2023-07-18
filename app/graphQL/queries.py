from graphene import ObjectType, List
from app.graphQL.types import UserObject, AuthorObject, BookObject
from app.db.database import db
from app.db.models import User, Author, Book


class Query(ObjectType):
    users = List(UserObject)
    authors = List(AuthorObject)
    books = List(BookObject)

    # Root-Level Resolvers
    def resolve_users(root, info):
        return db.session.query(User).all()
    
    def resolve_authors(root, info):
        return db.session.query(Author).all()
    
    def resolve_books(root, info):
        return db.session.query(Book).all()