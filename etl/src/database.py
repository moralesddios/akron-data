from sqlalchemy import create_engine

from .constants import SQLALCHEMY_DATABASE_URL

def connection():
  """ Retorna la conexión de postgresql """
  return create_engine(SQLALCHEMY_DATABASE_URL)
