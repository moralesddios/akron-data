from sqlalchemy import create_engine

from .constants import SQLALCHEMY_DATABASE_URL

def connection():
  return create_engine(SQLALCHEMY_DATABASE_URL)
