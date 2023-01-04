import pandas as pd

from .constants import PATH_TO_CSV

def extract():
  """ Extrae los datos usando pandas """
  return pd.read_csv(PATH_TO_CSV)
