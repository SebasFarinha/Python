"""Crear una funcion que reciba una lista y otro argumento ASC o DESC, y ordene la lista de forma ascendente o descendente
según el argumento recibido."""

#Crear la funcion
#ordenar la lista de forma ascendente
def ordenar_asc(lista):
    for x in range (len(lista)-1):
        for y in range (len(lista)-1):
            if lista[y] > lista[y+1]:
                aux = lista[y+1]
                lista[y+1]= lista[y]
                lista[y]= aux
    return lista

#ordenar la lista de forma descendente
def ordenar_desc(lista):
    for x in range (len(lista)-1):
        for y in range (len(lista)-1):
            if lista[y] < lista[y+1]:
                aux = lista[y+1]
                lista[y+1]= lista[y]
                lista[y]= aux
    return lista


#Ordenar de forma ascendente o descendente dependiendo del orden solicitado
def orden (lista, orden_de_lista):
    if (orden_de_lista == "ASC"):
        ordenar_asc (lista_original)
        return lista_original
    elif (orden_de_lista== "DESC"):
        ordenar_desc(lista_original)
        return lista_original 
    else:
        return "El orden solo puede ser ASC o DESC"
    

lista_original = [2,88,7,5,99,8,2,4,4,44,6,88,7,6,3,4,77,4,25]
print("Lista orginal: ", lista_original)
lista_original = orden(lista_original,"ASC")
print("Lista ordenadada forma ascendente: ", lista_original)


lista_original = orden(lista_original,"DESC")
print("Lista ordenadada forma descendente: ", lista_original)