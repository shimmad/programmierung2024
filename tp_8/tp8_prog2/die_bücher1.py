import json
class Libro:
    def __init__(self,titulo:str,autor:str,genero:str,publicado:int,isbn:int) -> None:
        if not isinstance (titulo,str) or titulo=="" or titulo.isspace():
            raise ValueError
        if not isinstance (autor,str) or autor=="" or autor.isspace():
            raise ValueError
        if not isinstance (genero,str) or genero=="" or genero.isspace():
            raise ValueError
        if not isinstance (publicado, int) or publicado < 0:
            raise ValueError
        if not isinstance (isbn, int) or isbn <= 0:
            raise ValueError
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__publicado = publicado
        self.__isbn = isbn

    def to_json(self):
        """
        return Libro object as a JSON string.
        """
        return json.dumps({
            'titulo': self.__titulo,
            'autor': self.__autor,
            'genero': self.__genero,
            'publicado': self.__publicado,
            'isbn': self.__isbn
        })
    @classmethod
    def from_json(cls, json_str: str):
        """
        return a Libro object from a JSON string.
        """
        data = json.loads(json_str)
        return cls(data['titulo'], data['autor'], data['genero'], data['publicado'], data['isbn'])
    
    def obt_titulo(self):
        return self.__titulo
    
    def obt_autor(self):
        return self.__autor
    
    def obt_genero(self):
        return self.__genero
    
    def obt_publicado(self):
        return self.__publicado
    
    def obt_isbn(self):
        return self.__isbn
    def __str__(self) -> str:
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nGénero: {self.__genero}\nPublicado: {self.__publicado}\nISBN: {self.__isbn}"
        

class Test:
    @staticmethod
    def inicio():
        try:
            #cargo los datos del archivo libros.json
            with open('libros.json') as json_file:
                libros_data = json.load(json_file) #creo diccionario

            # la expresión json.dumps(libro) convierte el diccionario libro en una cadena JSON,
            # y se la manda al metodo from_json de la clase libro para construir un objeto Libro a partir de esa cadena.
            #conversión JSON a cadena y luego de cadena a objeto.
            biblioteca = [Libro.from_json(json.dumps(libro)) for libro in libros_data["libros"]]
            #  construir el objeto Libro usando el diccionario:
            #biblioteca = [Libro(libro['titulo'], libro['autor'], libro['genero'], libro['publicado'], libro['isbn']) for libro in libros_data["libros"]] 
            #la clave "libros" contiene una lista de diccionarios, donde cada diccionario representa un libro con las claaves de los atributos

            
            print("Libros en la biblioteca:")
            for libro in biblioteca:
                print(libro) 
        
            usuario = int(input("\nIngrese un año de publicación para buscar libros publicados ese año: "))
        
            #filtrar y mostrar los libros publicados en el año ingresado
            publicados = [libro for libro in biblioteca if libro.obt_publicado() == usuario]
        
            if publicados:
                print(f"\nLista de libros publicados en {usuario}:")
                for libro in publicados:
                    print(libro) 
                
            else:
                print(f"\nNo se encontraron libros publicados en el año {usuario}.")
        
        except FileNotFoundError:
            print("El archivo 'libros.json' no fue encontrado.")
        except json.JSONDecodeError:
            print("Error al decodificar el JSON.")
        except KeyError:
            print("Error: La clave 'libros' no existe en el archivo JSON.")
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número entero para el año.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    Test.inicio()