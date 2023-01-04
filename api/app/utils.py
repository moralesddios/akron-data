from sqlalchemy.sql.functions import ReturnTypeFromArgs

class haversine(ReturnTypeFromArgs):
  inherit_cache = True