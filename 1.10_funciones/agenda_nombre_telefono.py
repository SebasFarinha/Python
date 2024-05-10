#Crear un diccionario global
agenda ={}

def agregar_contacto(nombre, contacto):
    agenda [nombre]= contacto

#es para ver la agenda como diccionario
""""def ver_contacto():
    print(agenda)
"""
#Ver la agenda mas ordenada
def ver_agenda():
    print("Lista de contactos")
    for nombre, contc in agenda.items():
        print(f"{nombre} : {contc}")


#Prueba
if __name__ == "__main__":
    agregar_contacto("Sebas","972553191")
    agregar_contacto("Denis","0983556677")
   # ver_contacto()
    ver_agenda()