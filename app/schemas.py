from typing import Optional
from pydantic import BaseModel, Field, condecimal


class PuntoAcesoSchema(BaseModel):
  id: str
  programa: str
  fecha_instalacion: str
  latitud: condecimal(max_digits=15, decimal_places=9) = Field(default=0)
  longitud: condecimal(max_digits=15, decimal_places=9) = Field(default=0)
  colonia: Optional[str] = None
  alcaldia: Optional[str] = None

  class Config:
    orm_mode = True
