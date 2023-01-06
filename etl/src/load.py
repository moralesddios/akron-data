from pandas import DataFrame
from sqlalchemy import Numeric

from .database import connection

def load(df: DataFrame, target: str):
  """
  Cargar los datos en una tabla de PostgreSQL
  :param df: DataFrame a cargar
  :param target: Nombre de la tabla de PostgreSQL
  :return: None
  """
  df.to_sql(
    target,
    con=connection(),
    if_exists='replace',
    index=False,
    dtype={
      "latitud": Numeric(precision=None),
      "longitud": Numeric(precision=None)
    }
  )
