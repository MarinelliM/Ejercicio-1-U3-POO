from ManejadorFacultades import ManejaFacultad
from Menu import menu
if __name__ == '__main__':
    Manejador = ManejaFacultad() 
    Manejador.initmf()
    Manejador.test()
    menu(Manejador)
