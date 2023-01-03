from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from app.exceptions import MessageException
from app.routes import router as routes

app = FastAPI(
  title="Akron REST API",
  description="Servicios REST - Puntos de acceso Wi-Fi CDMX",
  version="1.0.0"
)

@app.exception_handler(MessageException)
async def unicorn_exception_handler(request: Request, exc: MessageException):
  return JSONResponse(
    status_code=exc.code,
    content={"message": exc.message},
  )

@app.on_event("startup")
async def app_init():
  """Inicializa la aplicación"""
  app.include_router(routes, tags=['Puntos de acceso Wi-Fi'])
  add_pagination(app)
