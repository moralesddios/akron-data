import os

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
PATH_TO_CSV = os.getenv('PATH_TO_CSV')