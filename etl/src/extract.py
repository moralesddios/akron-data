import pandas as pd

def extract(path_to_csv: str):
  """
  Extrae los datos del csv usando pandas
  :return: DataFrame
  """
  return pd.read_csv(path_to_csv)
