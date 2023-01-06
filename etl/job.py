import os
import logging

from src.constants import CSV_FILE_NAME
from src.extract import extract
from src.load import load
from src.haversine import create_haversine
from src.transform import transform

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Obtener la ruta del archivo csv con los datos
base_dir = os.path.dirname(__file__)
path_to_csv = os.path.join(base_dir, CSV_FILE_NAME)

#### ----- Extraer ----- ####
logging.debug('Running Data Extract...')
df = extract(path_to_csv)

#### ----- Transformar ----- ####
logging.debug('Running Data Transform...')
clean_df = transform(df)

#### ----- Cargar ----- ####
logging.debug('Running Data Load...')
load(clean_df, "access_points")

# Crear el procedimiento almacenado para el calculo aproximado de la distancia entre dos puntos
create_haversine()

logging.info('Data succesfully loaded to PostgreSQL Database...')
