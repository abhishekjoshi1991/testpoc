from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI_2
print(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI_2)
# db = SQLAlchemy()

def get_db_engine(uri=SQLALCHEMY_DATABASE_URI):
    return create_engine(uri)

def get_db_engine_2():
    return create_engine(SQLALCHEMY_DATABASE_URI_2)
