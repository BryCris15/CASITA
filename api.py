# Para esta practica hay que instalar fastapi y uvicorn (uvicorn es el servidor que nos va a permitir mostrar el app de FastAPI)
# para la instalación usaremos los siguiente comandos dentro de un terminal: pip install fastapi y pip install uvicorn


# Una vez instalado importamos la libreria de FastAPI
from fastapi import FastAPI

#creamos el objeto de la clase
app = FastAPI()   

#creando el decorador y peticion tipo get
@app.get('/')     

#crando la funcion
def hello_world():
    return { "helo": "world" }  

#creando el servidor
# en un terminal colocar lo siguiente: uvicorn api:app