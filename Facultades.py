from Carreras import Carrera
class Facultad:
    __Codigo: str
    __Nombre: str
    __Direccion: str
    __Localidad: str
    __Telefono: int
    __Carrera: list[Carrera]

    def __init__(self,Codigo,Nombre,Direccion,Localidad,Telefono) -> None:
        self.__Codigo = Codigo
        self.__Nombre = Nombre
        self.__Direccion = Direccion
        self.__Localidad = Localidad
        self.__Telefono =Telefono
        self.__Carrera = []
        pass

    def agregarcarrera(self, carrera):
        self.__Carrera.append(carrera)

    def getNombre(self):
        return self.__Nombre
    
    def getcod(self):
        return self.__Codigo
    
    def getlocalidad(self):
        return self.__Localidad
    
    def mostrar(self):
        print('Facultad:')
        print('Codigo: {}, Nombre: {}, Direccion: {}, Localidad: {}, Telefono: {}'.format(self.__Codigo,self.getNombre(),self.__Direccion,self.__Localidad,self.__Telefono))
        print('-'.center(30,'-'))
        for e in self.__Carrera:
            print('Carrera:')
            e.mostrar()

    def mostrar_carreras(self):
        for i in self.__Carrera:
            print('Carrera:') 
            i.mostrar()
            print('\n')

    def getcarreras(self):
        return self.__Carrera

    # def buscarcarrera(self,nomcar):
    #     i = 0
    #     while i < len(self.__Carrera):
    #         if nomcar == self.__Carrera[i].getnombre():
    #             cod = self.__Carrera[i].getcodigo()
    #             i = len(self.__Carrera)
    #             return cod
    #         else: i+=1
        