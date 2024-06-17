
from flask import Flask, Request, jsonify


app = Flask(__name__)

@app.route("/") #cuando es vacio se encuentra en home
def hello_world():
    return "Bienvenidos a casa"

@app.route("/Apruebo")
def hello_world():
    return "estamos en mantenimiento"

@app.route("/comprobado")
def hello_world():
    return "ya logre correr"

if __name__=="__main_":
    app.run()
    

