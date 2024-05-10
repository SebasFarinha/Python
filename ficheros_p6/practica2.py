'''Crear un programa Python que cree un programa Python y que lo ejecute. El código puede ser sobre cualquier cosa'''
texto= input("Nombre del archivo: ")
nombre_fichero = texto+ 'py'
f = open(nombre_fichero, 'w') #apertura w= write r= read, a = append

x=0
for i in range(100):
    x +=1
    
    f.write(f'{x}, ')
f.close()