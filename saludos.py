from flask import Flask
app = Flask(__name__)

@app.route('/')#decorador / esta en home
def WORLD(): #renderiza todo el contenido
    return 'Hola mundo, ya lo subi a GitHub'

@app.route('/Prueba')#decorador
def prueba(): #renderiza todo el contenido
    return 'Seccion en mantenimiento'
    

@app.route('/Aprueba')#decorador
def aprueba(): #renderiza todo el contenido
    return 'sitio seguro'

#arranca el servidor local
if __name__ == "__main__":
    app.run(port=5001)
    app.run(debug=True) #actualiza el sito sin tener que parar el servidor
