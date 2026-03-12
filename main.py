from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

asistencia = {
    "total": 0,
    "servicio": "Servicio dominical"
}

@app.get("/asistencia")
def obtener_asistencia():
    return asistencia

@app.post("/asistencia/agregar")
def agregar_persona():
    asistencia["total"] += 1
    return asistencia

@app.post("/asistencia/restar")
def restar_persona():
    if asistencia["total"] > 0:
        asistencia["total"] -= 1
    return asistencia

@app.post("/asistencia/resetear")
def resetear():
    asistencia["total"] = 0
    return asistencia