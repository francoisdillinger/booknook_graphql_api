import os
from dotenv import load_dotenv
from flask import Flask
from app.db.database import create_database


def create_app():
    load_dotenv()
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_ECHO'] = True
    create_database(app)
    return app
