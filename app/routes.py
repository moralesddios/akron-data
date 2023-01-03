from fastapi import APIRouter
from fastapi_pagination import Page

from app.schemas import PuntoAcesoSchema
from app.services import listar

router = APIRouter()

@router.get("/", response_model=Page[PuntoAcesoSchema])
def puntos_acceso():
  return listar()
