from fastapi import FastAPI
import json

app = FastAPI()

# Cargar las rúbricas desde el archivo JSON
with open("rubricas_speaking_cambridge.json", "r", encoding="utf-8") as f:
    rubricas = json.load(f)

@app.get("/")
def home():
    return {"mensaje": "API de rúbricas Cambridge activa."}

@app.get("/rubrica/{nivel}")
def obtener_rubricas_por_nivel(nivel: str):
    nivel = nivel.upper()
    if nivel in rubricas:
        return rubricas[nivel]
    return {"error": f"No se encontró el nivel {nivel}"}

@app.get("/rubrica/{nivel}/{criterio}")
def obtener_rubrica_especifica(nivel: str, criterio: str):
    nivel = nivel.upper()
    criterio = criterio.title()
    if nivel in rubricas and criterio in rubricas[nivel]:
        return {criterio: rubricas[nivel][criterio]}
    return {"error": "Nivel o criterio no encontrados"}
# Cargar los modelos de respuesta desde el archivo JSON
with open("modelos_respuesta.json", "r", encoding="utf-8") as f:
    respuestas = json.load(f)

@app.get("/respuesta/{nivel}")
def obtener_respuestas_por_nivel(nivel: str):
    nivel = nivel.upper()
    if nivel in respuestas:
        return respuestas[nivel]
    return {"error": f"No se encontró el nivel {nivel}"}

@app.get("/respuesta/{nivel}/{parte}")
def obtener_respuesta_por_parte(nivel: str, parte: str):
    nivel = nivel.upper()
    parte = parte.title()
    if nivel in respuestas and parte in respuestas[nivel]:
        return {parte: respuestas[nivel][parte]}
    return {"error": "Nivel o parte no encontrados"}
# Cargar los errores frecuentes desde el archivo JSON
with open("errores_comunes.json", "r", encoding="utf-8") as f:
    errores = json.load(f)

@app.get("/errores/{nivel}")
def obtener_errores_por_nivel(nivel: str):
    nivel = nivel.upper()
    if nivel in errores:
        return errores[nivel]
    return {"error": f"No se encontró el nivel {nivel}"}

@app.get("/errores/{nivel}/{categoria}")
def obtener_errores_por_categoria(nivel: str, categoria: str):
    nivel = nivel.upper()
    categoria = categoria.lower()
    if nivel in errores and categoria in errores[nivel]:
        return {categoria: errores[nivel][categoria]}
    return {"error": "Nivel o categoría no encontrados"}

# Cargar expresiones útiles desde el archivo JSON
with open("expresiones_utiles.json", "r", encoding="utf-8") as f:
    expresiones = json.load(f)

@app.get("/expresiones/{nivel}")
def obtener_expresiones_por_nivel(nivel: str):
    nivel = nivel.upper()
    if nivel in expresiones:
        return expresiones[nivel]
    return {"error": f"No se encontró el nivel {nivel}"}

@app.get("/expresiones/{nivel}/{parte}")
def obtener_expresiones_por_parte(nivel: str, parte: str):
    nivel = nivel.upper()
    parte = parte.title()
    if nivel in expresiones and parte in expresiones[nivel]:
        return {parte: expresiones[nivel][parte]}
    return {"error": "Nivel o parte no encontrados"}


# Cargar plantilla de informe desde archivo JSON
with open("plantilla_informe.json", "r", encoding="utf-8") as f:
    informe_base = json.load(f)

@app.get("/informe/plantilla")
def obtener_plantilla_informe():
    return informe_base




