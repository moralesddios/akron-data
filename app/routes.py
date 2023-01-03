from typing import Optional
from fastapi import APIRouter
from fastapi_pagination import Page

from app.schemas import PuntoAcesoSchema
from app.services import APServices

router = APIRouter()
service = APServices()

@router.get("/", response_model=Page[PuntoAcesoSchema])
def lista_paginada(colonia: Optional[str] = None):
  return service.list(colonia)

@router.get("/detalle", response_model=PuntoAcesoSchema)
def detalle_por_id(id: str):
  return service.get(id)
