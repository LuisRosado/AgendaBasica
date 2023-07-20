# AgendaBasica
Una agenda de contactos basica hecha con listas

Este código en Python es una agenda simple que permite agregar, mostrar, buscar, modificar y eliminar contactos. A continuación, te explico cada parte del código:

SALIR, AGREGAR, MOSTRAR, BUSCAR, MODIFICAR, ELIMINAR: Son constantes enteras que representan las opciones del menú de la agenda.

-MostrarMenu(): Función que muestra el menú de opciones disponibles en la agenda.

-AgregarContacto(agenda): Función que permite agregar un nuevo contacto a la agenda. Se solicita al usuario ingresar el nombre, y si el contacto ya existe, se muestra un mensaje de que ya existe. De lo contrario, se solicitan el teléfono, el email y la categoría, y se agrega el contacto a la agenda.

-MostrarContactos(agenda): Función que muestra todos los contactos almacenados en la agenda, si hay alguno. Se recorren los elementos del diccionario agenda y se imprime la información de cada contacto.

-BuscarContacto(agenda): Función que permite buscar un contacto por su nombre en la agenda. Se solicita al usuario que ingrese el nombre del contacto a buscar, y se muestran todos los contactos cuyo nombre coincida parcialmente con el ingresado.

-ModificarContacto(agenda): Función que permite modificar los datos de un contacto existente en la agenda. Se solicita al usuario que ingrese el nombre del contacto a modificar, si el contacto existe, se muestra su información y se le permite ingresar nuevos datos para actualizar la información.

-EliminarContacto(agenda): Función que permite eliminar un contacto de la agenda. Se solicita al usuario que ingrese el nombre del contacto a eliminar, y si el contacto existe, se elimina de la agenda.

-main(): Función principal del programa. Inicializa la agenda como un diccionario vacío y muestra el menú de opciones. Según la opción seleccionada por el usuario, se ejecutan las funciones correspondientes. El bucle while permite seguir interactuando con la agenda hasta que el usuario decida salir.

En resumen, este programa es una sencilla agenda que permite al usuario agregar, mostrar, buscar, modificar y eliminar contactos. Los datos de los contactos se almacenan en un diccionario llamado Agenda, donde el nombre del contacto es la clave y los datos del contacto (teléfono, email y categoría) son una tupla asociada a esa clave.
