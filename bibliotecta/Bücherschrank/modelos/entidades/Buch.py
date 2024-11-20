class Libro:
    @classmethod
    def from_dicc(cls, dicc: dict):
        return cls(dicc['titulo'], dicc['autor'], dicc['ISBN'], dicc['anio_publicacion'], dicc['genero'])
    def __init__(self, titulo, autor, ISBN, anio_publicacion, genero):
        if not isinstance(titulo, str) or titulo== "" or titulo.isspace():
            raise ValueError("El título del libro debe ser un string no vacío")
        if not isinstance(autor, str) or autor== "" or autor.isspace():
            raise ValueError("El autor del libro debe ser un string no vacío")
        if not isinstance(ISBN, int) or ISBN < 0 :
            raise ValueError("El ISBN del libro debe ser un número positivo")
        if not isinstance(anio_publicacion, int):
            raise ValueError("El año de publicación del libro debe ser un número")
        if not isinstance(genero, str) or genero== "" or genero.isspace():
            raise ValueError("El género del libro debe ser un string no vacío")
        self.__titulo = titulo
        self.__autor = autor
        self.__ISBN = ISBN
        self.__anio_publicacion = anio_publicacion
        self.__genero = genero
        
    def estab_titulo(self, titulo:str):
        if not isinstance(titulo, str) or titulo== "" or titulo.isspace():
            raise ValueError("El título del libro debe ser un string no vacío")
        self.__titulo = titulo
    def estab_autor(self, autor:str):
        if not isinstance(autor, str) or autor== "" or autor.isspace():
            raise ValueError("El autor del libro debe ser un string no vacío")
        self.__autor = autor
    def estab_anio(self, anio:int):
        if not isinstance(anio, int):
            raise ValueError("El año de publicación del libro debe ser un número")
        self.__anio_publicacion = anio
    def estab_genero(self, genero:str):
        if not isinstance(genero, str) or genero== "" or genero.isspace():
            raise ValueError("El género del libro debe ser un string no vacío")
        self.__genero = genero
   
        
    
    def obt_titulo(self):
        return self.__titulo
    def obt_autor(self):
        return self.__autor
    def obt_ISBN(self):
        return self.__ISBN
    def obt_anio_publicacion(self):
        return self.__anio_publicacion
    def obt_genero(self):
        return self.__genero
    def __str__(self):
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nISBN: {self.__ISBN}\nAño de publicación: {self.__anio_publicacion}\nGénero: {self.__genero}"
    def to_dicc(self):
        dict= {"titulo": self.__titulo, "autor": self.__autor, "ISBN": self.__ISBN, "anio_publicacion": self.__anio_publicacion,"genero": self.__genero}
        return dict        
    
    
        