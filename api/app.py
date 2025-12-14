from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI(
    title="API – Movie Analysis",
    description="API local para exponer resultados del análisis de películas",
    version="1.0"
)

DATA_PATH = Path("data")

def load_json(filename):
    file_path = DATA_PATH / filename
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def home():
    return {
        "message": "API de análisis de películas",
        "endpoints": [
            "/roi_por_genero",
            "/top_directores"
        ]
    }

@app.get("/roi_por_genero")
def roi_por_genero():
    """
    Devuelve el ROI promedio por género.
    Los valores fueron calculados previamente en el análisis.
    """
    data = load_json("roi_por_genero.json")
    return data[:3]
@app.get("/top_directores")
def top_directores():
    """
    Devuelve los directores mejor valorados (mínimo 10 películas),
    ordenados por vote_average promedio.
    """
    data = load_json("top_directores.json")
    return data[:3]
