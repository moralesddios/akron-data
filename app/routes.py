from typing import Optional

from fastapi import APIRouter
from fastapi_pagination import Page
from pydantic import condecimal

from app.schemas import PuntoAceso, PuntoDistancia
from app.services import APServices

router = APIRouter()
service = APServices()

@router.get("/", response_model=Page[PuntoAceso])
def lista_paginada(colonia: Optional[str] = None):
  return service.list(colonia)

@router.get("/detalle", response_model=PuntoAceso)
def detalle_por_id(id: str):
  return service.get(id)

@router.get("/cercanos", response_model=Page[PuntoDistancia])
def lista_paginada_orden_cercano(
    lat: condecimal(max_digits=15, decimal_places=9), long: condecimal(max_digits=15, decimal_places=9)):
  return service.nearby(lat, long)
