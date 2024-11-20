from modelos.entidades.Buch import Libro
import json

class Repositorio_Libro:
    __ruta_archivo="datos/libro.json"
    def __init__(self):
        self.__libros= self.__cargarTodos()
        

    def __cargarTodos(self)->list:
        #leer todo el contenido del archivo
        #convertirlo en lista de diccinoarios
        #convertir la lista de diccionarios en lista de objetos Alumno
        lista_objetos = []
        try:
            lista_dicc = []
            with open(Repositorio_Libro.__ruta_archivo, "r", encoding="UTF-8") as archivo:
                diccionarioDatos = json.load(archivo)
            lista_dicc = diccionarioDatos["libros"]
            for dicc in lista_dicc:
                lista_objetos.append(Libro.from_dicc(dicc))
        except:
            print("Error al abrir el archivo alumnos.json")
        return lista_objetos
    def __guardar_libros(self):
        try:
            with open(Repositorio_Libro.__ruta_archivo, "w", encoding="UTF8") as archivo:
                # Crear una lista de diccionarios a partir de los libros
                lista_dic = [libro.to_dicc() for libro in self.__libros]
                
                # Crear un diccionario que contenga la lista
                diccionario_datos = {
                    "libros": lista_dic
                }
                
                # Guardar el diccionario en el archivo JSON
                json.dump(diccionario_datos, archivo, ensure_ascii=False, indent=4)
            print("Datos de los libros guardados correctamente.")
        except Exception as e:
            print(f"Error guardando los datos de los libros: {e}")
    def obt_libros(self):
        return self.__libros
    def exsiste_libro(self,num:int): #devuelve un bool, lo busca con el ISBN
        if not isinstance(num,int):
            raise ValueError("El ISBN debe ser un número entero.")
        return num in [Libro.obt_ISBN(libro) for libro in self.__libros]
    
    def agregar_libro(self, libro: Libro):
        if not self.exsiste_libro(libro.obt_ISBN()):
            self.__libros.append(libro)
            self.__guardar_libros()
        else:
            print(f"El libro con ISBN {libro.obt_ISBN()} ya existe.")
            
    def buscar_libro(self, num: int):
        if not isinstance(num, int):
            raise ValueError("El ISBN debe ser un número entero.")
        else: 
            for libro in self.__libros:
                if libro.obt_ISBN() == num:
                    return libro
                return None
    def modificar_libro(self, ISBN: int, nuevos_datos: dict):
        """
    Modifica un libro existente con los nuevos datos proporcionados.
    """
        if not isinstance(ISBN, int):
            raise ValueError("El ISBN debe ser un número entero.")
        libro = self.buscar_libro(ISBN)  # Busca el libro por ISBN
        if libro:
            # Verifica y actualiza los campos según los datos nuevos proporcionados
            if "titulo" in nuevos_datos:
                libro.estab_titulo(nuevos_datos["titulo"])
            if "autor" in nuevos_datos:
                libro.estab_autor(nuevos_datos["autor"])
            if "anio_publicacion" in nuevos_datos:
                libro.estab_anio(nuevos_datos["anio_publicacion"])
            if "genero" in nuevos_datos:
                libro.estab_genero(nuevos_datos["genero"])
            
            self.__guardar_libros()  # Guarda los cambios en el archivo
            return True
        else:
            return False


   
    def eliminar_libro(self, num: int):
        libro_buscado=self.__buscar_libro(num)
        if libro_buscado:
            self.__libros.remove(libro_buscado)
            self.__guardar_libros()
            print ("se elimino el libro: {libro_buscado}")
        else:
            print(f"No se encontro el libro con ISBN {num}.")

