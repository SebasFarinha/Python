from biblioteca import Biblioteca
from libro import Libro

if __name__ == "__main__":
    ejecutar = True
    print("- - -  BIENVENIDO AL SISTEMA BIBLIOTECARIO - - - ")
    while ejecutar:
        
        opcion = int(
            input('Que desea hacer?: \n1-Crear Biblioteca   \n2-Agregar libro \n3-Ver catálogo \n4- Quitar libro \n5- Salir\n:'
                  )
        )
        if opcion ==1:
            nombre = input("Ingrese el nombre para la biblioteca: ")
            biblioteca= Biblioteca(nombre)

            print("Se creo la biblioteca: ", biblioteca.consultar_nombre_de_biblioteca()
             )
        elif opcion== 2:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            cantidad_de_paginas = input("Cantidad de paginas: ")
            genero = input("Género: ")
            sipnosis= input("Sipnosis: ")

            libro = Libro(titulo,autor,cantidad_de_paginas,genero,sipnosis)
            biblioteca.agg_libros(libro)

        elif opcion== 3:
            print("Catálogo de libros: ")
            for i in biblioteca.consultar_libros():
                print(i)

        elif opcion== 4:
                indice = int(input("ID del libro a eliminar"))
                biblioteca.quitar_libro(indice)

        elif opcion== 5:
             ejecutar = False

        else:
             print("FAVOR ELIJA UNA OPCIÓN VÁLIDA!!!")
