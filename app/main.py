import os
from dotenv import load_dotenv
from flask import Flask
from app.db.database import create_database


def create_app():
    load_dotenv()
    TESTING = os.getenv('TESTING') == 'True'

    if TESTING:
        DB_USER = os.getenv('TESTING_DB_USER')
        DB_PASS = os.getenv('TESTING_DB_PASS')
        DB_HOST = os.getenv('TESTING_DB_HOST')
        DB_NAME = os.getenv('TESTING_DB_NAME')
    else:
        DB_USER = os.getenv('DB_USER')
        DB_PASS = os.getenv('DB_PASS')
        DB_HOST = os.getenv('DB_HOST')
        DB_NAME = os.getenv('DB_NAME')

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_ECHO'] = True
    create_database(app)
    return app

# app.py
# requirements.txt
# .gitignore
#     app/
#         db/
#             seed_data/
#             __init__.py
#             database.py
#             models.py
#         graphQL/
#             __init__.py
#             mutations.py
#             queries.py
#             types.py     
#         utils/
#             __init__.py
#             utils.py
#         __init__.py
#         main.py
#     tests/
#         __init__.py
#         test_users.py