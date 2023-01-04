from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from app.exceptions import MessageException
from app.routes import router as routes

def init_router(app: FastAPI):
  """
  Initialise the FastAPI router with all existing routers
  :param app: app to initialise
  :return: None - Include router of app
  """
  app.include_router(routes, prefix='/aps', tags=['aps'])

def init_app() -> FastAPI:
  _app = FastAPI(
    title="Akron REST API",
    description="Servicios REST - Puntos de acceso Wi-Fi CDMX",
    version="1.0.0"
  )
  init_router(_app)
  add_pagination(_app)

  return _app

app = init_app()

@app.exception_handler(MessageException)
async def unicorn_exception_handler(request: Request, exc: MessageException):
  return JSONResponse(
    status_code=exc.code,
    content={"message": exc.message},
  )
