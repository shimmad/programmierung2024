from flask import Blueprint, request,jsonify
from modelos.repositorios.repo_general import obtenerRepoLibro
from modelos.entidades.Buch import Libro

libros_blueprint = Blueprint('libros', __name__)
repo_libros= obtenerRepoLibro()

@libros_blueprint.route('/libros/', methods=['GET']) # corregir si no hay ningun libro cargado
def obtener_libros():
    lista_dicc=[]
    for lib in repo_libros.obt_libros():
        lista_dicc.append(lib.to_dicc())
    return jsonify(lista_dicc), 200

@libros_blueprint.route('/libros/<int:ISBN>', methods=['GET'])

def obtener_libro_por_num(ISBN: int):
    libro = repo_libros.buscar_libro(ISBN)
    if libro:
        return jsonify(libro.to_dicc()), 200
    return jsonify({"mensaje": "Libro no encontrado"}), 404

@libros_blueprint.route('/libros/', methods=['POST'])
def agregar_libro():
    if request.is_json:
        datos = request.json
        try:
            lib = Libro.from_dicc(datos)
            print("Datos recibidos:", datos)
            print("Libro creado:", lib)
            print("¿Existe el libro?:", repo_libros.exsiste_libro(lib.obt_ISBN()))
        except Exception as e:
            return jsonify({"error":"No se pudo crear el libro con los datos recibidos.\n" + str(e)}),400
        if not repo_libros.exsiste_libro(lib.obt_ISBN()):
            if repo_libros.agregar_libro(lib):
                return jsonify({"mesaje":"Se agregó con éxito", "libro": datos}), 201
            else:
                 return jsonify({"mesaje":"Error al agregar el libro"}), 400
        else:
            return jsonify({"mesaje":"El ISBN ya se encuentra registrado"}),400
    else: 
        return jsonify({"mesaje":"Error, los datos deben estar en formato json"}),400
    
@libros_blueprint.route('/libros/<int:ISBN>', methods=['PUT'])
def modificar_libro(ISBN: int):
    if request.is_json:
        nuevos_datos = request.json
        try:
            if repo_libros.modificar_libro(ISBN, nuevos_datos):
                return jsonify({"mensaje": "El libro fue modificado con éxito"}), 200
            else:
                return jsonify({"mensaje": "No se encontró el libro con el ISBN proporcionado"}), 404
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"mensaje": "Los datos deben estar en formato JSON"}), 400

    
@libros_blueprint.route('/libros/<int:ISBN>', methods=['DELETE'])
def eliminar_libro(ISBN:int):
    if repo_libros.exsiste_libro(ISBN):
        if repo_libros.eliminar_libro(ISBN):
            return jsonify({"mesaje":"Se eliminó con éxito"}), 200
        else:
            return jsonify({"mesaje":"Error al eliminar el libro"}), 400
    else:
        return jsonify({"mesaje":"El ISBN no se encuentra registrado"}),400