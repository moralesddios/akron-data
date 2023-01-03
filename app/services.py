from database import SessionLocal
from fastapi import status
from fastapi_pagination.ext.sqlalchemy import paginate

from app.exceptions import MessageException
from app.models import PuntoAcceso

db = SessionLocal()

class APServices():
  def list(self):
    """ Obtener una lista paginada de puntos de acceso """
    return paginate(db.query(PuntoAcceso))

  def get(self, id: str):
    """ Obtener un punto de acceso por id """
    ap = db.query(PuntoAcceso).get(id)
    if not ap:
      raise MessageException(status.HTTP_404_NOT_FOUND, "No encontrado")
    return ap
