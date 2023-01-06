from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_list():
  response = client.get("/aps")
  assert response.status_code == 200
  assert len(response.json()['items'])>0

def test_list_filter():
  response = client.get("/aps?colonia=ZONA ESCOLAR ORIENTE")
  assert response.status_code == 200
  assert len(response.json()['items'])>0

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

def test_detail_not_found():
  response = client.get("/aps/detail?id=0")
  assert response.status_code == 404
  assert response.json() == {"message": "No encontrado", "exception": None}

def test_nearby():
  response = client.get("/aps/nearby?lat=19.53974&lon=-99.14251")
  assert response.status_code == 200
  assert len(response.json()['items'])>0
