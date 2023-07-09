from flask import Flask
from graphene import ObjectType, String, Schema, Int, List, Field
from flask_graphql import GraphQLView
from seed_data.users_data import users_data
from seed_data.authors_data import authors_data
from seed_data.books_data import books_data

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


class Query(ObjectType):
    users = List(UserObject)
    authors = List(AuthorObject)
    books = List(BookObject)

    # Root-Level Resolvers
    def resolve_users(root, info):
        print("Here I am!")
        print(f'Data: {users_data}')
        return users_data
    
    def resolve_authors(root, info):
        return authors_data
    
    def resolve_books(root, info):
        return books_data







schema = Schema(query=Query)

app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True  # Enable GraphiQL when app.debug is True. GraphiQL is an interactive in-browser GraphQL IDE.
    )
)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
