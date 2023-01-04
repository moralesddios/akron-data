import pandas as pd

def extract(source: str):
  """ Extrae los datos usando pandas """
  return pd.read_csv(source)
