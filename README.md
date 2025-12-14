# Autores:
Jauregui Lorda Maria Lina, 
Lara Gonzalo Francisco 

# Trabajo Final – Análisis de Películas (TMDB)

Trabajo final de la cursada de **Lenguajes 2025 (UCALP)**.  
Autores: **María Lina Jauregui Lorda** – **Gonzalo Francisco Lara**

---

## Descripción general

Este proyecto tiene como objetivo aplicar técnicas de **análisis de datos y programación en Python** para extraer conocimiento significativo a partir de datasets reales de la industria cinematográfica.

Se trabajó con el dataset **TMDB 5000 Movies**, integrando conceptos de:

- Preprocesamiento y limpieza de datos
- Análisis exploratorio de datos (EDA)
- Estadística descriptiva
- Visualización
- Exposición de resultados mediante una **mini-API local**

El trabajo se compone de un notebook de análisis, un informe académico y una mini-API desarrollada con **FastAPI**.

---

## Objetivos del proyecto

### Objetivo general
Aplicar técnicas de análisis de datos y programación para transformar datos crudos en información valiosa, integrando los contenidos vistos a lo largo de la materia.

### Objetivos específicos
- Realizar limpieza y preprocesamiento de datos.
- Utilizar estadística descriptiva y visualizaciones.
- Analizar relaciones entre género, presupuesto, revenue, popularidad, rating y duración.
- Elaborar un informe académico con estructura formal.
- Publicar los principales resultados mediante una mini-API local.

---

## Dataset utilizado

Se trabajó con los siguientes archivos, disponibles públicamente en Kaggle:

- **tmdb_5000_movies.csv**  
  Información general de las películas: presupuesto, recaudación, duración, géneros, popularidad y puntuación promedio.

- **tmdb_5000_credits.csv**  
  Información del elenco y equipo técnico, utilizada para identificar directores.

Fuente:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## Ejes de análisis desarrollados

El análisis se estructuró en torno a cuatro preguntas principales:

1. **Rentabilidad (ROI) y ROI por género**  
   Se definió el ROI como `revenue / budget` y se analizaron valores promedio por género, considerando y excluyendo outliers.

2. **Relación entre budget, revenue, popularidad y rating**  
   Se construyó una matriz de correlación utilizando los coeficientes de **Pearson** y **Spearman**.

3. **Evolución de la duración de las películas en los últimos 50 años**  
   Análisis por décadas utilizando promedios, medianas, gráficos de dispersión y regresión lineal.

4. **Directores con mejor rating promedio**  
   Se analizaron directores con un mínimo de 10 películas dirigidas para obtener métricas comparables.

Los resultados y su interpretación se desarrollan en detalle en el informe académico.

---

## Metodología resumida

- Exploración inicial de los datasets.
- Limpieza de valores nulos y atípicos.
- Filtrado de películas con estado *Released*.
- Transformación de la columna `genres` en variables binarias (one-hot encoding).
- Extracción y limpieza del director desde el dataset de créditos.
- Integración de datasets mediante `INNER JOIN`.
- Generación de datasets finales listos para análisis.
- Exportación de resultados resumidos en formato JSON para la API.

---

## Mini-API local

Como cierre integrador del trabajo, se desarrolló una **mini-API REST** utilizando **FastAPI**, cuyo objetivo es exponer los principales resultados del análisis sin recalcular los datos.

La API consume archivos JSON generados previamente durante el análisis y los devuelve a través de endpoints HTTP.

### Endpoints disponibles

- **GET `/roi_por_genero`**  
  Devuelve el **top 3 de géneros** ordenados por ROI promedio.

- **GET `/top_directores`**  
  Devuelve el **top 3 de directores mejor valorados**, considerando únicamente aquellos con al menos 10 películas dirigidas.

---

## Estructura del repositorio
trabajo-final-lenguajes-tmdb/
│
├── notebook/
│ └── analisis_tmdb.ipynb
│
├── informe/
│ └── informe_final.pdf
│
├── api/
│ ├── app.py
│ ├── requirements.txt
│ └── data/
│ ├── roi_por_genero.json
│ └── top_directores.json
│
├── video.txt
└── README.md


---

## Cómo ejecutar la mini-API

1. Instalar dependencias:
  pip install fastapi uvicorn
2. Ejecutar el servidor desde la carpeta api:
  python -m uvicorn app:app --reload
3. Acceder a la API en:
  http://127.0.0.1:8000

Tecnologías utilizadas
  Python 3
  Pandas
  NumPy
  Matplotlib / Seaborn
  FastAPI
  Uvicorn
  JSON

Contexto académico

Este proyecto fue desarrollado como Trabajo Final Integrador de la materia Lenguajes 2025 (UCALP), cumpliendo con los requisitos de análisis de datos, documentación académica y exposición de resultados mediante una API local.
