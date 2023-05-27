from Carreras import Carrera
from Facultades import Facultad
import csv

class ManejaFacultad:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []
        pass

    def initmf(self):
        with open('facultades.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            cod = -1
            for fila in reader:
                if int(fila[0]) == cod:
                    carrera = Carrera(int(fila[1]),fila[2],fila[3],fila[4],fila[5])
                    self.__lista[cod-1].agregarcarrera(carrera)
                else: 
                    cod = int(fila[0])
                    facultad = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                    self.__lista.append(facultad)
        archivo.close()
    
    def test(self):
        for e in self.__lista:
            print('\n')
            e.mostrar()
        print('\n')

    def buscarfacultad(self,codf):
        i =0
        while i < len(self.__lista):
            if codf == self.__lista[i].getcod():
                self.__lista[i].mostrar_carreras()
                i = len(self.__lista)
            else: i+=1

    def buscarporcarrera(self,carrera):
        i = 0
        cod = -1
        while i < len(self.__lista):
            carreras = self.__lista[i].getcarreras()
            a = 0
            while a < len(carreras):
                if carrera == carreras[a].getnombre():
                    cod = carreras[a].getcodigo()
                    a = len(carreras)
                else: a+=1
            
            if cod > 0:
                cf = self.__lista[i].getcod()
                nomf = self.__lista[i].getNombre()
                loc = self.__lista[i].getlocalidad()
                i = len(self.__lista)
            else: i+=1
        print('\n')
        print('Codigo Facultad: {}, Codigo Carrera: {}' .format(cf,cod))
        print('Nombre de Facultad: {}, Localidad: {}' .format(nomf,loc))
    

    

