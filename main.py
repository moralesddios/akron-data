from fastapi import FastAPI

from app.routes import router as routes

app = FastAPI(
  title="Akron REST API",
  description="Servicios REST - Puntos de acceso Wi-Fi CDMX",
  version="1.0.0"
)


@app.on_event("startup")
async def app_init():
  """Inicializa la aplicación"""
  app.include_router(routes, tags=['Puntos de acceso Wi-Fi'])
