from modelos.repositorios.repo_libros import Repositorio_Libro
repo_libro = None

def obtenerRepoLibro()-> Repositorio_Libro:
    global repo_libro
    if not isinstance(repo_libro, Repositorio_Libro):
        repo_libro = Repositorio_Libro()
    return repo_libro
