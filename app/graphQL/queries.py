from graphene import ObjectType, List
from app.graphQL.types import UserObject, AuthorObject, BookObject
from app.db.database import users_data, authors_data, books_data

class Query(ObjectType):
    users = List(UserObject)
    authors = List(AuthorObject)
    books = List(BookObject)

    # Root-Level Resolvers
    def resolve_users(root, info):
        # print("Here I am!")
        # print(f'Data: {users_data}')
        return users_data
    
    def resolve_authors(root, info):
        return authors_data
    
    def resolve_books(root, info):
        return books_data