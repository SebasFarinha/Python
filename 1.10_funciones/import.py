#Importar y bibliotecas
import os
#Menu
respuesta = -1
while (respuesta != 0):
    print("Elija una opción")
    print("1. Calculadora ")
    print("2. Ver mi IP ")
    print("3. Administrador de tareas ")
    print("4. Apagar equipo en 5 minutos ")
    print("Cancelar apagado ")
    print("0. Salir del programa ")
    respuesta= int(input(" "))
    if (respuesta==1):
        os.system('calc')
    elif (respuesta==2):
        os.system('ipconfig')
    elif (respuesta==3):
        os.system('taskmgr')
    elif (respuesta==4):
        os.system(' shutdown -s -t 300 ')
    elif (respuesta==5):
        os.system('shutdown -a')
    elif(respuesta==0):
        pass
    else:
        print("No se ha seleccionado una opción válida")
        print("Favor volver a seleccionar!")
        