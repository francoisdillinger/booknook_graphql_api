from graphene import Mutation, String, Int, List, Field
from graphql import GraphQLError
from app.db.models import User
from app.db.database import db
from random import choices
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
TOKEN_EXPIRATION_TIME_IN_MINUTES = int(os.getenv('TOKEN_EXPIRATION_TIME_IN_MINUTES'))


def generate_token(email):
    expiration_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_TIME_IN_MINUTES)
    payload = {
        "email": email,
        "exp": expiration_time
        }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

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