Movie Analysis API

API local desarrollada con FastAPI para exponer los resultados de un análisis de películas realizado en Python.
La API consume archivos JSON generados previamente a partir del análisis de datos y los sirve mediante endpoints HTTP.

Descripción general

Esta API permite consultar:

ROI promedio por género

Directores mejor valorados, considerando únicamente aquellos con un mínimo de 10 películas dirigidas

Los datos ya se encuentran procesados y almacenados en archivos JSON dentro del proyecto.

Tecnologías utilizadas

Python 3

FastAPI

Uvicorn

JSON

Pathlib

Estructura del proyecto
project/
│
├── app.py
├── README.md
├── data/
│   ├── roi_por_genero.json
│   └── top_directores.json
└── requirements.txt

Cómo ejecutar la API
1. Instalar dependencias
pip install fastapi uvicorn


Opcionalmente, se puede utilizar un entorno virtual.

2. Ejecutar el servidor

Desde la carpeta raíz del proyecto:

python -m uvicorn app:app --reload


La API quedará disponible en:

http://127.0.0.1:8000

Documentación interactiva

FastAPI genera documentación automáticamente:

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

Endpoints disponibles
/

Método: GET
Descripción: Endpoint de inicio. Devuelve un mensaje de bienvenida y la lista de endpoints disponibles.

Respuesta ejemplo:

{
  "message": "API de análisis de películas",
  "endpoints": [
    "/roi_por_genero",
    "/top_directores"
  ]
}

/roi_por_genero

Método: GET
Descripción: Devuelve el top 3 de géneros ordenados por ROI promedio, calculado previamente durante el análisis.

Respuesta ejemplo:

[
  {
    "genre": "Horror",
    "roi_mean": 5.23,
    "movie_count": 120
  },
  {
    "genre": "Thriller",
    "roi_mean": 4.10,
    "movie_count": 95
  },
  {
    "genre": "Comedy",
    "roi_mean": 3.87,
    "movie_count": 210
  }
]

/top_directores

Método: GET
Descripción: Devuelve el top 3 de directores mejor valorados, considerando únicamente aquellos con al menos 10 películas, ordenados por vote_average promedio.

Respuesta ejemplo:

[
  {
    "director": "Christopher Nolan",
    "avg_vote": 8.4,
    "movie_count": 11
  },
  {
    "director": "Quentin Tarantino",
    "avg_vote": 8.2,
    "movie_count": 10
  },
  {
    "director": "Martin Scorsese",
    "avg_vote": 8.1,
    "movie_count": 12
  }
]

Notas importantes

La API no recalcula datos; únicamente expone resultados previamente procesados.

Los archivos JSON deben existir dentro de la carpeta data.

Los endpoints devuelven únicamente los tres primeros registros (top 3).

Contexto académico

Esta API fue desarrollada como parte de un trabajo práctico o proyecto final, con el objetivo de:

Aplicar técnicas de análisis de datos en Python

Persistir resultados en formato JSON

Exponer resultados mediante una API REST simple