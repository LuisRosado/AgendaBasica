import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5

def MostrarMenu():
    os.system('cls')
    print(f'''               Agenda\n
{AGREGAR})Agregar Contactos
{MOSTRAR})Mostrar todos los Contactos
{BUSCAR})Buscar un Contacto
{MODIFICAR})Modificar un Contacto
{ELIMINAR})Eliminar Contactos
{SALIR})Salir\n''')

def AgregarContacto(agenda):
    os.system('cls')
    print('                        Agregar Contacto')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('\nEse Contacto Ya Existe')
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        categoria = input('Categoria: ')
        agenda.setdefault(nombre, (telefono, email, categoria))
        print('\nSe ha agregado a tu lista de contactos con exito.')

def MostrarContactos(agenda):
    os.system('cls')
    print('                        Mostar Contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print(f'Categoria: {datos[2]}')
            print('-'*50)
    else:
        print('\nNo tienes ningun Contacto.')

def BuscarContacto(agenda):
    os.system('cls')
    print('                        Buscar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                print(f'Categoria: {datos[2]}')
                print('-'*50)
                encontrados += 1
        if encontrados == 0:
            print('\nContacto No Encontrado.')
        else:
            print(f'\nSe encontraron {encontrados} contactos')
    else:
        print('\nNo hay Contactos Registrados.')

def ModificarContacto(agenda):
    os.system('cls')
    print('                        Modificar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print('Contacto Encontrado:')
            print(f'Nombre: {nombre}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print(f'Categoria: {datos[2]}')
            print('-'*50)
            print('Ingresa los nuevos datos')
            telefono = input('Telefono: ')
            email = input('Email: ')
            categoria = input('Categoria: ')
            agenda[nombre] = (telefono, email, categoria)
            print('\nSe ha actualizado con exito')
        else:
            print('\nNo existe el Conatcto')
    else:
        print('\nNo hay contactos registrados')

def EliminarContacto(agenda):
        os.system('cls')
        print('                        Eliminar Contacto')
        if len(agenda) > 0:
            nombre = input('Nombre: ')
            if agenda.get(nombre):
                agenda.pop(nombre)
                print('\nContacto Eliminado')
            else:
                print('\nNo existe el contacto')
        else:
            print('\nNo hay contactos registrados')

def main():
    continuar = True
    Agenda = {}
    while continuar:
        MostrarMenu()
        opc = int(input('Seleccione una opcion: '))

        if opc == AGREGAR:
            AgregarContacto(Agenda)
        elif opc ==MOSTRAR:
            MostrarContactos(Agenda)
        elif opc == BUSCAR:
            BuscarContacto(Agenda)
        elif opc == MODIFICAR:
            ModificarContacto(Agenda)
        elif opc == ELIMINAR:
            EliminarContacto(Agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida...')
        input('Presiona enter para continuar')

if __name__ == '__main__':
    main()
