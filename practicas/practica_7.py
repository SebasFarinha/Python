



import mysql.connector
mydb= mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='',
    database='bd_traductor_seba'
)

cursor= mydb.cursor()
while True:
    palabra=input("Ingrese la palabra a traducir: ")
    sentencia=f"select ingles from traductor where espanol like '{palabra}'"
    cursor.execute(sentencia)


    resultado = cursor.fetchall()
 
    if palabra == '0':
        break
    
    elif len(resultado) > 0:
        for x in resultado:
                print(x)
    else:
        resp= input("La palabra no existe en el traductor. Desea agregarlo? y/n: ")
        if resp == 'y':
            traduccion=input(f"ingrese la traduccion de: {palabra}: ")
            agregar =f"INSERT INTO `traductor`(`ID`, `ESPANOL`, `INGLES`) VALUES (DEFAULT,'{palabra}','{traduccion}')"
            cursor.execute(agregar)
            mydb.commit() #sirve para confirmar la accion(en este caso agregar a la bd)
        
             

         
         
         
         
         
         
         
    
   
   