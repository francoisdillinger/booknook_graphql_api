from graphene import Mutation, String, Int, Field, ObjectType
from app.db.database import db
from app.graphQL.types import UserObject, AuthorObject, BookObject
from app.db.models import User, Author, Book
from sqlalchemy.orm import joinedload


class AddAuthor(Mutation):
    class Arguments:
        author_first_name = String(required=True)
        author_last_name = String(required=True)
    
    author = Field(lambda: AuthorObject)

    def mutate(root, info, author_first_name, author_last_name):
        author = Author(
            author_first_name=author_first_name,
            author_last_name=author_last_name
        )
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)
        return AddAuthor(author=author)


class UpdateAuthor(Mutation):
    class Arguments:
        author_id = Int(required=True)
        author_first_name = String()
        author_last_name = String()
    
    author = Field(lambda: AuthorObject)

    def mutate(root, info, author_id, author_first_name=None, author_last_name=None):
        # This is how you would do it if the session is being closed prematurely. I removed explicit closing of 
        # the session in mutations because it was causing issues and flask_sqlalchemy handles it for us.
        # author = db.session.query(Author).options(joinedload(Author.books)).filter(Author.id == author_id).first()

        
        author = db.session.query(Author).filter(Author.id == author_id).first()

        if not author:
            raise Exception(f'Author with id {author_id} does not exist.')
        if author_first_name is not None:
            author.author_first_name = author_first_name
        if author_last_name is not None:
            author.author_last_name = author_last_name

        db.session.commit()
        db.session.refresh(author)
        return UpdateAuthor(author=author)

class Mutation(ObjectType):
    add_author = AddAuthor.Field()
    update_author = UpdateAuthor.Field()