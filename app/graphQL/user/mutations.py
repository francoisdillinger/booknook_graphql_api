from graphene import Mutation, String, Int, List, Field
from graphql import GraphQLError
from app.db.models import User
from app.db.database import db
from app.utils.utils import generate_token, ph, VerifyMismatchError

class LoginUser(Mutation):
    class Arguments:
        email = String(required=True)
        password = String(required=True)
    
    token = String()

    def mutate(root, info, email, password):
        user = db.session.query(User).filter_by(email=email).first()

        if not user:
            raise GraphQLError('Invalid Email or password.')
        
        try:
            ph.verify(user.password, password)
        except VerifyMismatchError:
            raise GraphQLError('Invalid Email or password.')
        
        # token = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
        token = generate_token(email)
        
        return LoginUser(token=token)