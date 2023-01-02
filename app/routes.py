from typing import List

from fastapi import APIRouter

from app.schemas import PuntoAcesoSchema
from app.services import listar

router = APIRouter()

@router.get("/", response_model=List[PuntoAcesoSchema])
def puntos_acceso():
  return listar()
