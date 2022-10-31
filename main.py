from typing import Union
from fastapi import FastAPI

# Creacion de una aplicacion FastAPI:

app = FastAPI()

@app.get('/')
def hola_mundo():
    return {'hola': 'mundo!!'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}     

@app.get('/calculadora')
def calcular(operado_1: float, operado_2: float):
    return {'suma': operado_1 + operado_2}    