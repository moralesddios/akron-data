# Arkon Data - Pipeline Puntos de acceso WiFi CDMX

requirements:

- Python 3.7
- Docker

## Run ETL locally

Create .env file and configure postgres database url.

```sh
$ mv .env.example .env
$ vim .env
```

Install Python libraries in Pyhton or venv.

```sh
$ pip install -r requirements.txt
```

Run.

```sh
$ python etl/job.py
```

## Run API services or tests locally

Create .env file and configure postgres database url.

```sh
$ mv .env.example .env
$ vim .env
```

Install Python libraries in Pyhton or venv.

```sh
$ pip install -r requirements.txt
```

Run tests.

```sh
$ cd api
$ pytest
```

Run local.

```sh
$ cd api
$ uvicorn main:app --reload
```

OpenAPI -> http://localhost:8000/docs

## Run PostgreSQL with Docker (Optional)

Run postgres.

```sh
$ docker run -d
  --name postgres
  -p 5432:5432
  -e POSTGRES_PASSWORD=secret
  -v postgres:/var/lib/postgresql/data
  --net=arkon
  postgres:14
```

Connect to postgres.

```sh
$ psql -h localhost -U postgres
```

Create database.

```sh
postgres=\# create database arkon;
```

## Run ETL with Docker

Build docker image.

```sh
$ docker build --no-cache -t arkon-etl ./etl
```

Run docker container.

```sh
$ docker run -d
  --name arkon-etl
  --net=arkon
  --env DATABASE_URL=postgresql://postgres:secret@postgres/arkon
  arkon-etl
```

## Run API with Docker

Build docker image.

```sh
$ docker build --no-cache -t arkon-api ./api
```

Run docker container.

```sh
$ docker run -d
  --name arkon-api
  -p 8080:80
  --net=arkon
  --env DATABASE_URL=postgresql://postgres:secret@postgres/arkon
  arkon-api
```

Run all with docker-compose.

```sh
$ docker-compose up --build --force-recreate --no-deps -d
```

Stop all with docker-compose.

```sh
$ docker-compose down --volumes
```