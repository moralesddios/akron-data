
from database import SessionLocal

from app.models import PuntoAcceso

db = SessionLocal()


def listar():
  """ Obtener usuario por id """
  return db.query(PuntoAcceso).limit(10).all()
