
from flask import Flask,render_template # type: ignore
from flask_bootstrap import Bootstrap # type: ignore

app = Flask(__name__)
Bootstrap(app)

app.template_folder = 'G:\\UCE\\DESAROLLO\\World'

@app.route('/')  # decorador / esta en home
def world():  # renderiza todo el contenido
    with app.app_context():
        return render_template('index.html')                    #'Hola mundo, ya me funsiono'


@app.route('/Prueba')#decorador
def prueba(): #renderiza todo el contenido
    return 'seccion en desarrollo.'
    

@app.route('/Aprueba')#decorador
def aprueba(): #renderiza todo el contenido
    return 'sitio seguro'

#arranca el servidor local
if __name__ == "__main__":
    app.run(port=5001,debug=True) #actualiza el sito sin tener que parar el servidor

    
