from database import Base
from sqlalchemy import Column, Numeric, String


class PuntoAcceso(Base):
  id = Column(String(64), primary_key=True, index=True)
  programa = Column(String(64))
  fecha_instalacion = Column(String(64))
  latitud =  Column(Numeric(precision=None))
  longitud =  Column(Numeric(precision=None))
  colonia = Column(String(64))
  alcaldia = Column(String(64))

  __tablename__ = "access_points"
