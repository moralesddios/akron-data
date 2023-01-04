import logging

from src.extract import extract
from src.load import load
from src.transform import transform

root = logging.getLogger()
root.setLevel(logging.DEBUG)

#### ----- Extraer ----- ####
logging.debug('Running Data Extract...')
df = extract()

#### ----- Transformar ----- ####
logging.debug('Running Data Transform...')
clean_df = transform(df)

#### ----- Cargar ----- ####
logging.debug('Running Data Load...')
load(clean_df, "access_points")

logging.info('Data succesfully loaded to PostgreSQL Database...')
