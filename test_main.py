from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_healthcheck():
  response = client.get("/aps")
  assert response.status_code == 200
  # assert response.json() == {"status": "OK"}

def test_detail():
  response = client.get("/aps/detail?id=Cuautepec")
  assert response.status_code == 200
  assert response.json() == {
    "id": "Cuautepec",
    "programa": "Sitios Publicos",
    "fecha_instalacion": "2018-12-15",
    "latitud": 19.53974,
    "longitud": -99.14251,
    "colonia": "ZONA ESCOLAR ORIENTE",
    "alcaldia": "GUSTAVO A. MADERO"
  }
