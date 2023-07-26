from graphene import Mutation, String, Int, List, Field
from graphql import GraphQLError
from app.db.models import User
from app.db.database import db
from random import choices

class LoginUser(Mutation):
    class Arguments:
        email = String(required=True)
        password = String(required=True)
    
    token = String()

    def mutate(root, info, email, password):
        user = db.session.query(User).filter_by(email=email).first()

        if not user or user.password != password:
            raise GraphQLError('Invalid Email')
        
        token = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
        
        return LoginUser(token=token)