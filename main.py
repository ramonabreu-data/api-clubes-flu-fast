from fastapi import FastApi
from pydantic import BaseModel

app = FastApi()

#Rota raiz

@app.get("/")
def raiz():
    return{"olá mundo"}