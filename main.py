from ManejadorFacultades import ManejaFacultad
from Menu import menu
if __name__ == '__main__':
    Manejador = ManejaFacultad() 
    Manejador.initmf()
    a = input('ingrese un valor:')
    Manejador.test()
    menu(Manejador)