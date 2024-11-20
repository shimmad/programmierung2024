from flask import Flask
from rutas.ruta_libros import libros_blueprint
#importo rutas

app = Flask(__name__)#creo una instancia dela nclase flas
app.register_blueprint(libros_blueprint) #registro ruta

if __name__=="__main__":
    app.run(debug=True)
