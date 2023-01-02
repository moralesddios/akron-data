from pandas import DataFrame

from database import connection


def load(df: DataFrame, target: str):
  """ Carga el Dataframe en PostgreSQL """
  df.to_sql(target, con=connection, if_exists='replace', index=False)
  print("Data succesfully loaded to PostgreSQL Database")