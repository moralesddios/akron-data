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
  """ Lista paginada """
  return service.list(colonia)

@router.get("/detail", response_model=PuntoAceso)
def detalle_por_id(id: str):
  """ Detalle por id """
  return service.get(id)

@router.get("/nearby", response_model=Page[PuntoDistancia])
def lista_paginada_orden_cercano(
    lat: condecimal(max_digits=15, decimal_places=9), lon: condecimal(max_digits=15, decimal_places=9)):
  """ Distancia aproximada en KM """
  return service.nearby(lat, lon)
