"""
Implementar un traductor de palabras del español a inglés usando la estructura de diccionario. 
Debe solicitar una palabra al usuario y verificar si existe en el diccionario y mostrar la traducción.
En caso de no existir la palabra en el diccionario, solicitar si desea agregar al diccionario.
El diccionario se detiene al introducir 0
"""
tradcutor = {"casa" : "house", "manzana": "apple"}

while True:

    palabra = input("Ingrese la palabra a traducir: ")

    if palabra in tradcutor:
        print(tradcutor[palabra])
    elif palabra == "0":
        break
    else:
        resp = input("La palabra no existe en el Traductor, desea agregarlo? r: s/n ")
        if (resp == "s"):
            traduccion = input(f"Ingrese la traduccion de {palabra}: ")
            tradcutor [palabra] = traduccion
        
