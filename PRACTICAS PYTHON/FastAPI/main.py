from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class cupones(BaseModel):
    nombre: str
    descuento: str
    precioOG: str
    tienda: str
    Fvencimiento: str


@app.get("/")
def index():
    return {"mensage" : "Hola, mundo (っ ͡❛ ͜ʖ ͡❛)っ"}

@app.get("/cupones/{id}")
def mostrar_cupones(id: int):
    return{"data" : id}

@app.post("/cupones")
def insertar_cupon(cupones: cupones):
    return{"mensage": f"cupon {cupones.nombre} vence el {cupones.Fvencimiento} su precio original fue de {cupones.precioOG} pero tuvo un descuento de {cupones.descuento} este cupon llega gracias a nuestros amigos de {cupones.tienda} ʕ•́ᴥ•̀ʔっ♡"}
