from fastapi import status
from fastapi_pagination.ext.sqlalchemy import paginate

from app.database import SessionLocal
from app.exceptions import MessageException
from app.models import PuntoAcceso
from app.utils import haversine

db = SessionLocal()

class APServices():
  def list(self, colonia: str):
    """
    Obtener una lista paginada de puntos de acceso
    :param colonia: colonia
    :return: lista paginada de puntos de acceso
    """
    query = db.query(PuntoAcceso)
    if colonia:
      query = query.filter_by(colonia=colonia)
      return paginate(query)
    return paginate(query)

  def get(self, id: str):
    """
    Obtener un punto de acceso por id
    :param id: punto de acceso id
    :return: punto de acceso
    """
    ap = db.query(PuntoAcceso).get(id)
    if not ap:
      raise MessageException(status.HTTP_404_NOT_FOUND, "No encontrado")
    return ap
  
  def nearby(self, lat, lon):
    """
    Obtener una lista paginada y ordenada por proximidad a una coordenada dada
    :param lat: latitud de la coordenada
    :param lon: longitud de la coordenada
    :return: lista paginada
    """
    # calcula la distancia aproximada en km por formula haversine
    distancia = haversine(lat, lon, PuntoAcceso.latitud, PuntoAcceso.longitud)
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
