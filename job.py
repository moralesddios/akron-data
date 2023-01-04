import logging

from data.extract import extract
from data.load import load
from data.transform import transform

root = logging.getLogger()
root.setLevel(logging.DEBUG)

#### ----- Extraer ----- ####
logging.debug('Running Data Extract...')
df = extract("puntos-de-acceso-wifi.csv")

#### ----- Transformar ----- ####
logging.debug('Running Data Transform...')
clean_df = transform(df)

#### ----- Cargar ----- ####
logging.debug('Running Data Load...')
load(clean_df, "access_points")

logging.info('Data succesfully loaded to PostgreSQL Database...')
