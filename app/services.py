from database import SessionLocal
from fastapi_pagination.ext.sqlalchemy import paginate

from app.models import PuntoAcceso

db = SessionLocal()


def listar():
  """ Obtener usuario por id """
  return paginate(db.query(PuntoAcceso))
