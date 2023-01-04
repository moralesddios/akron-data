from typing import Optional
from pydantic import BaseModel, Field, condecimal


class PuntoAceso(BaseModel):
  id: str
  programa: str
  fecha_instalacion: str
  latitud: condecimal(max_digits=15, decimal_places=9)
  longitud: condecimal(max_digits=15, decimal_places=9)
  colonia: Optional[str] = None
  alcaldia: Optional[str] = None

  class Config:
    orm_mode = True

class PuntoDistancia(BaseModel):
  id: str
  programa: str
  fecha_instalacion: str
  latitud: condecimal(max_digits=15, decimal_places=9)
  longitud: condecimal(max_digits=15, decimal_places=9)
  colonia: Optional[str] = None
  alcaldia: Optional[str] = None
  distancia: condecimal(max_digits=24, decimal_places=18) = Field(default=0)
