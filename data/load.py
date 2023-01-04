from pandas import DataFrame
from sqlalchemy import Numeric

from database import connection


def load(df: DataFrame, target: str):
  """ Carga el Dataframe en PostgreSQL """
  df.to_sql(target, con=connection, if_exists='replace', index=False, dtype={"latitud": Numeric(precision=None), "longitud": Numeric(precision=None)})
  print("Data succesfully loaded to PostgreSQL Database")