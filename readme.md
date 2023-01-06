# Akron Data - Pipeline Puntos de acceso WiFi CDMX

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
  --net=akron
  postgres:14
```

Connect to postgres.

```sh
$ psql -h localhost -U postgres
```

Create database.

```sh
postgres=\# create database akron;
```

## Run ETL with Docker

Build docker image.

```sh
$ docker build --no-cache --build-arg -t akron-etl ./etl
```

Run docker container.

```sh
$ docker run -d
  --name akron-etl
  --net=akron
  --env DATABASE_URL=postgresql://postgres:secret@postgres/akron
  akron-etl
```

## Run API with Docker

Build docker image.

```sh
$ docker build --no-cache -t akron-api ./api
```

Run docker container.

```sh
$ docker run -d
  --name akron-api
  -p 8080:80
  --net=akron
  --env DATABASE_URL=postgresql://postgres:secret@postgres/akron
  akron-api
```