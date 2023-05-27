class Carrera:
    __Codigo: str
    __Nombre: str
    __Fecha_inicio: str
    __Duracion: str
    __Titulo: str
    
    def __init__(self,codigo,nombre,fecha,duracion,titulo) -> None:
        self.__Codigo = codigo
        self.__Nombre = nombre
        self.__Fecha_inicio = fecha
        self.__Duracion = duracion
        self.__Titulo = titulo
        pass

    def getcodigo(self):
        return self.__Codigo
    
    def getnombre(self):
        return self.__Nombre
    
    def mostrar(self):
        return print('Codigo: {}, Nombre: {}, Fecha de inicio: {}, Duracion: {}, Titulo: {}' .format(self.getcodigo(),self.__Nombre,self.__Fecha_inicio,self.__Duracion,self.__Titulo))