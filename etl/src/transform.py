from pandas import DataFrame

def transform(df: DataFrame) -> DataFrame:
  """ Transforma los datos """
  clean_df = df.fillna({'colonia': 'NA', 'alcaldia': 'NA'})
  return clean_df
