from database import Base
from sqlalchemy import Column, Numeric, String


class PuntoAcceso(Base):
  id = Column(String(64), primary_key=True, index=True)
  programa = Column(String(64))
  fecha_instalacion = Column(String(64))
  latitud =  Column(Numeric(precision=9, scale=6))
  longitud =  Column(Numeric(precision=9, scale=6))
  colonia = Column(String(64))
  alcaldia = Column(String(64))

  __tablename__ = "access_points"
