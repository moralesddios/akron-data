import os

from dotenv import load_dotenv

load_dotenv()

CSV_FILE_NAME = os.getenv('CSV_FILE_NAME')
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')