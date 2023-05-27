def menu(m):
    print('1 - Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.')
    print('2 - Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.')
    print('0 - Salir')
    op = int(input('Ingrese la opcion a buscar:'))
    while op != 0:
        if op == 1:
           codF = int(input('Ingrese el codigo de la facultad:'))
           print('\n')
           m.buscarfacultad(codF)
        elif op == 2:
            nombre_carrera = str(input('Ingrese nombre de la Carrera:'))
            m.buscarporcarrera(nombre_carrera)
            print('\n')
        else:
            print('Opcion incorrecta')
            op = int(input('Ingrese la opcion a buscar:'))
        print('1 - Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.')
        print('2 - Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.')
        print('0 - Salir')
        op = int(input('Ingrese la opcion a buscar:'))
    print('Fin del programa')