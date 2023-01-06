from pandas import DataFrame

def transform(df: DataFrame) -> DataFrame:
  """
  Transformar los datos
  :param df: DataFrame a transformar
  :return: DataFrame transformado
  """
  clean_df = df.fillna({'colonia': 'NA', 'alcaldia': 'NA'})
  return clean_df
