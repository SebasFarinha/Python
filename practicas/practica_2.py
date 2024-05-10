"""
Escriba un programa para validar si los datos de acceso (usuario y contraseña) se encuentran en el diccionario.
Validar a solo 3 intentos erroneos de contraseña utilizando ciclo while.
"""
registro= {}
#Agregar usuario y pass al diccionario
def agregar_user (usuario,contraseña):
    registro[usuario]= contraseña
agregar_user("sebaa","sispe")
#Validar solo 3 intentos
intentos = 0
while(intentos <= 3):
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")

    if user in registro and password == registro [user]:
        print("Usuario Correcto")
        break
    else:
        print("Datos incorrectos, volver a intentar!!")
        intentos +=1
#si pasa los 3 intentos
if (intentos > 3):
    print("Demasiados intentos fallidos!!!")
    












