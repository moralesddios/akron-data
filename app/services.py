from database import SessionLocal
from fastapi import status
from fastapi_pagination.ext.sqlalchemy import paginate

from app.exceptions import MessageException
from app.models import PuntoAcceso
from app.utils import haversine

db = SessionLocal()

class APServices():
  def list(self, colonia: str):
    """ Obtener una lista paginada de puntos de acceso """
    query = db.query(PuntoAcceso)
    if colonia:
      query = query.filter_by(colonia=colonia)
      return paginate(query)
    return paginate(query)

  def get(self, id: str):
    """ Obtener un punto de acceso por id """
    ap = db.query(PuntoAcceso).get(id)
    if not ap:
      raise MessageException(status.HTTP_404_NOT_FOUND, "No encontrado")
    return ap
  
  def nearby(self, lat, long):
    """ Obtener una lista paginada y ordenada por proximidad a una coordenada dada """
    distancia = haversine(lat, long, PuntoAcceso.latitud, PuntoAcceso.longitud)
    query = db.query(
      PuntoAcceso.id,
      PuntoAcceso.programa,
      PuntoAcceso.fecha_instalacion,
      PuntoAcceso.latitud,
      PuntoAcceso.longitud,
      PuntoAcceso.colonia,
      PuntoAcceso.alcaldia,
      distancia.label('distancia')
    ).order_by(distancia)

    return paginate(query)
