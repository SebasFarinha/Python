#Cargar e imprimir una lista con funciones
#definir una lista vacia
lista=[]
#definir un def para cargar la lista
def cargar_lista(dato):
    lista.append(dato)
#Recibir un indeterminado nro de argumentos
def cargar_lista(*args):
    for arg in args:
         lista.append(arg)
#Imprimir la lista
def imprimir_lista ():
    for item in lista:
        print(item, end= " | ")
#Prueba del programa
if __name__ == "__main__":

    cargar_lista(25)
    cargar_lista(50)
    cargar_lista(80)
    cargar_lista(55,66)

    
    imprimir_lista()